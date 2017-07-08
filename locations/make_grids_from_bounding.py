"""
Makes a cartographic grid from the 3x3 bounding boxes
"""

import os

import arcpy

base_path = os.path.split(os.path.abspath(__file__))[0]
bounding_boxes = r"C:\Users\dsx\Documents\ArcGIS\Default.gdb\FieldEquipment_2016_3x3_grid_all"
land_use_data = r"C:\Users\dsx\Projects\ssj-delta-cu\CALSIMETAW_land_use\landuse_2016.tif"  # needed because we'll align our grid to it
scratch_gdb = os.path.join(base_path, "scratch.gdb")

def clear_workspace(workspace):
	"""
		Delete and recreate the workspace because we'll need to read the list of features in it at one point
	:return:
	"""

	arcpy.Delete_management(workspace)
	name_parts = os.path.split(workspace)
	arcpy.CreateFileGDB_management(name_parts[0], name_parts[1])
	arcpy.env.workspace = scratch_gdb

def split(feature_class, attribute, names, workspace):
	"""
		Given a feature class, an attribute, and a set of values for that attribute that should be made into new feature
		classes, splits the feature into multiple feature classes in workspace, one per attribute
	:param feature_class:
	:param attribute:
	:param names:
	:param workspace:
	:return:
	"""
	features = []
	feature_layer = "boxes_layer"
	arcpy.MakeFeatureLayer_management(feature_class, feature_layer)

	for value in names:
		expression = "{} = '{}'".format(attribute, value)
		print(expression)
		arcpy.SelectLayerByAttribute_management(feature_layer, "NEW_SELECTION", expression)
		new_name = arcpy.CreateUniqueName("split_box_{}".format(value), workspace)
		arcpy.CopyFeatures_management(feature_layer, new_name)
		features.append(new_name)

	return features


def get_grid(bounding_box, land_use):
	"""
		Given a bounding box and a snap raster (land use), creates a cell grid as polygons
	:param bounding_box:
	:param land_use:
	:return:
	"""

	# we need to create a random raster, then convert it to an integer grid with unique values
	random_grid = arcpy.sa.CreateRandomRaster("1251", 30, arcpy.Describe(bounding_box).extent)
	integer_grid = arcpy.sa.Int(random_grid * 100000)  # 100000 is high enough to give us unique values in almost all situations
	extracted_grid = arcpy.sa.ExtractByMask(integer_grid, bounding_box)  # then extract it to the box because random raster will make it one cell wider in every direction

	new_name = arcpy.CreateUniqueName("grid_cells", scratch_gdb)
	extracted_grid.save(new_name)  # save it out

	final_name = "{}_grid".format(new_name)
	arcpy.RasterToPolygon_conversion(new_name, final_name, simplify=False)

	return final_name

if __name__ == "__main__":

	arcpy.env.coordinateSystem = arcpy.SpatialReference(3310)

	arcpy.CheckOutExtension("Spatial")
	try:
		clear_workspace(scratch_gdb)

		# split them out so we can operate one by one

		names = ["D01", "D02", "D03", "D04", "D05", "D06", "D07", "D08", "D09", "D10", "D11", "D12", "D13", "D14"]
		attribute = "Station_ID"
		all_bounds = split(bounding_boxes, attribute=attribute, names=names, workspace=scratch_gdb)

		grids = []
		for bounding_box in all_bounds:
			print("Processing {}".format(bounding_box))
			grids.append(get_grid(bounding_box, land_use_data))

		arcpy.Merge_management(grids, "merged_grids")
	finally:
		arcpy.CheckInExtension("Spatial")
