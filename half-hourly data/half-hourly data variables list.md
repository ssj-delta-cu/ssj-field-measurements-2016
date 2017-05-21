## Delta Crop Consumptive Water Use Field Measurements Half-Hourly Data README file

This document provides background information on the provided data including a description of all variables. 

Half-hourly measurements and data are provided for each station as .csv files. 

Throughout this document, flux densities are referred to as fluxes for convenience.

## Half-hourly Data

* **HalfHourlyData_StationName.csv**  - contains half-hourly measurements and calculated variables

Units are listed at the end of each variable description.  All variables may not be included in file for a particular station depending on sensors deployed for that particular station. 

## Basic Information

*	**rDateTime** – date and time of half-hour of measurements. The time listed represents the end of the half-hour of measurements: 13:30 represents measurements from 13:00:01 to 13:30:00. All times are given in GMT -7 (PDT) 
* **stationName** – name of the ET station
*	**BattVolt_Avg** – Average datalogger battery voltage over the half-hour (V)
*	**Tpanel** – temperature measured inside the datalogger (°C)
*	**Tpanel_qc** – temperature measured inside the datalogger  with quality control procedures applied (bad data removed) – includes de-spiking and removal of intermittent or anomalous measurements associated with issues such as low battery power (°C)

## Net Radiation related variables

*	**Rn_Avg** – Average net radiation measured by net radiometer (W m-2)
*	**Rn_Avg_qc** – Rn_Avg with quality control procedures applied (bad data removed) – includes de-spiking and removal of intermittent or anomalous measurements associated with issues such as low battery power or sensor damage (W m-2)
*	**Rn_Avg_qc_mm** - Rn_Avg_qc converted to units of evapotranspiration (mm hh-1)
*	**Rn_Avg_gf** – Rn_Avg_qc with missing half-hours (up to five consecutive half-hours) gap-filled by linear interpolation (W m-2)
*	**Rn_Avg_gf_mm** - Rn_Avg_gf converted to units of evapotranspiration (mm hh-1)

## Ground Heat Flux related variables

*	**HFP_1** – ground heat flux measured by heat flux plate 1 (W m-2)
*	**HFP_1_qc** – HFP_1 with quality control procedures applied (bad data removed) – includes de-spiking and removal of intermittent or anomalous measurements associated with issues such as low battery power or sensor damage (W m-2)
*	**HFP_2** – ground heat flux measured by heat flux plate 2 (W m-2)
*	**HFP_2_qc** – HFP_2 with quality control procedures applied (bad data removed) – includes de-spiking and removal of intermittent or anomalous measurements associated with issues such as low battery power or sensor damage (W m-2)
*	**ST** – soil temperature measured by a set of TCAV-averaging soil thermocouples (°C)
*	**ST_gf** – ST with missing half-hours (up to five consecutive half-hours) gap-filled by linear interpolation (°C)
*	**ST_qc** – ST_gf with quality control procedures applied (bad data removed) – includes de-spiking and removal of intermittent or anomalous measurements associated with issues such as low battery power or sensor damage (°C)
*	**CV** – estimation of the soil volumetric heat capacity in the surface layer based on an estimated soil bulk density of 1.2 Mg m-3 and a volumetric water content in the surface of 0.2 m3 m-3
*	**STdiff_gf** – difference in soil temperature from one half-hour to the next with missing half-hours (up to five consecutive half-hours) gap-filled by linear interpolation (°C)
*	**STdiff_qc** – difference in soil temperature from one half-hour to the next with quality control procedures applied (bad data removed) – includes de-spiking and removal of intermittent or anomalous measurements associated with issues such as low battery power or sensor damage (°C)
*	**TfTi_gf** – estimated storage contribution to the ground heat flux with missing half-hours (up to five consecutive half-hours) gap-filled by linear interpolation
*	**TfTi_qc** – estimated storage contribution to the ground heat flux with quality control procedures applied
*	**G_1_qc** – HFP_1_qc with storage added and quality control procedures applied
*	**G_2_qc** – HFP_2_qc with storage added and quality control procedures applied
*	**G_qc** – average of G_1_qc and G_2_qc
*	**G_qc_mm** – G_qc converted to units of evapotranspiration (mm hh-1)
* **G_gf** - 
* **G_gf_mm** - 

## Surface Renewal and Thermocouple related variables (including residual ET)

*	**Tc0_Avg** – Average temperature measured by first thermocouple, Tc (°C)  
*	**Tc0_Avg_qc** – Tc0_Avg with quality control procedures applied (°C)  
*	**Tc0m5sq_Avg** – Average 2nd  order structure function of the Tc temperature signal used in the surface renewal heat flux calculation (°C)^2
*	**Tc0m5sq_Avg_qc** – Tc0m5sq_Avg with quality control procedures applied (°C)^2
*	**Tc0m5cu_Avg** – Average 3rd order structure function of the Tc temperature signal used in the surface renewal heat flux calculation (°C)^3
*	**Tc0m5cu_Avg_qc** – Tc0m5cu_Avg with quality control procedures applied (°C)^3
*	**Tc0m5fi_Avg** – Average 5th  order structure function of the Tc temperature signal used in the surface renewal heat flux calculation (°C)^5
*	**Tc0m5fi_Avg_qc** – Tc0m5fi_Avg with quality control procedures applied (°C)^5
*	**Tc_H** – uncalibrated sensible heat flux calculated using by thermocouple Tc (W m-2)
*	**Tc_H_qc** – uncalibrated sensible heat flux calculated using by thermocouple Tc with quality control procedures applied (bad data removed) – includes de-spiking and removal of intermittent or anomalous measurements associated with issues such as low battery power or sensor damage (W m-2)
*	**Tc_H_gf** – Tc_H_qc with missing half-hours (up to five consecutive half-hours) gap-filled by linear interpolation (W m-2)
*	**Tc_H_qc_mm** – Tc_H_qc converted to units of evapotranspiration (mm hh-1)
*	**Tc_H_gf_mm** – Tc_H_gf converted to units of evapotranspiration (mm hh-1)
*	**Tc_alpha_pos** – calibration coefficient used to calibrate positive sensible heat fluxes derived from Tc
*	**Tc_alpha_neg** – calibration coefficient used to calibrate negative sensible heat fluxes derived from Tc
*	**Tc_aH_qc** – Tc_H_qc multiplied by the calibration coefficient (W m-2)
*	**Tc_aH_qc_count** – running count of times quality control procedure was applied to Tc_aH_qc
*	**Tc_aH_gf** – Tc_H_gf multiplied by the calibration coefficient with missing half-hours (up to five consecutive half-hours) gap-filled by linear interpolation (W m-2)
*	**Tc_aH_gf_count** – running count of times gap-filling procedure was applied to Tc_aH_gf 
*	**Tc_aH_qc_mm**  – Tc_aH_qc converted to units of evapotranspiration (mm hh-1)
*	**Tc_aH_gf_mm**  –  Tc_aH_gf converted to units of evapotranspiration (mm hh-1)
*	**LE_Tc_aH_qc**  – latent energy flux derived as the residual of Rn_Avg_qc, Tc_aH_qc, and G_qc where available
*	**LE_Tc_aH_gf**  –  latent energy flux derived as the residual of Rn_Avg_gf, Tc_aH_gf, and G_gf where available
*	**ET_Tc_aH_qc** –  LE_Tc_aH_qc converted to units of evapotranspiration (mm hh-1)
*	**ET_Tc_aH_gf**  – LE_Tc_aH_gf converted to units of evapotranspiration (mm hh-1)

*	**Tn0_Avg** – Average temperature measured by second thermocouple, Tn (°C)  
*	**Tn0_Avg_qc** – Tn0_Avg with quality control procedures applied (°C) 
*	**Tn0m5sq_Avg** – Average 2nd  order structure function of the Tn temperature signal used in the surface renewal heat flux calculation (°C)^2
*	**Tn0m5sq_Avg_qc** – Tn0m5sq_Avg with quality control procedures applied (°C)^2
*	**Tn0m5cu_Avg** – Average 3rd order structure function of the Tn temperature signal used in the surface renewal heat flux calculation (°C)^3
*	**Tn0m5cu_Avg_qc** – Tn0m5cu_Avg with quality control procedures applied (°C)^3
*	**Tn0m5fi_Avg** – Average 5th  order structure function of the Tn temperature signal used in the surface renewal heat flux calculation (°C)^5
*	**Tn0m5fi_Avg_qc** – Tn0m5fi_Avg with quality control procedures applied (°C)^5
*	**Tn_H** – uncalibrated sensible heat flux calculated using by thermocouple Tn (W m-2)
*	**Tn_H_qc** – uncalibrated sensible heat flux calculated using by thermocouple Tn with quality control procedures applied (bad data removed) – includes de-spiking and removal of intermittent or anomalous measurements associated with issues such as low battery power or sensor damage (W m-2)
*	**Tn_H_gf** – Tn_H_qc with missing half-hours (up to five consecutive half-hours) gap-filled by linear interpolation (W m-2)
*	**Tn_H_qc_mm** – Tn_H_qc converted to units of evapotranspiration (mm hh-1)
*	**Tn_H_gf_mm** – Tn_H_gf converted to units of evapotranspiration (mm hh-1)
*	**Tn_alpha_pos** – calibration coefficient used to calibrate positive sensible heat fluxes derived from Tn
*	**Tn_alpha_neg** – calibration coefficient used to calibrate negative sensible heat fluxes derived from Tn
*	**Tn_aH_qc** – Tn_H_qc multiplied by the calibration coefficients (W m-2)
*	**Tn_aH_qc_count** – running count of times quality control procedure was applied to Tn_aH_qc
*	**Tn_aH_gf** – Tn_H_gf multiplied by the calibration coefficients (W m-2)
*	**Tn_aH_gf_count** – running count of times gap-filling procedure was applied to Tn_aH_gf
*	**Tn_aH_qc_mm** - Tn_aH_qc converted to units of evapotranspiration (mm hh-1)
*	**Tn_aH_gf_mm** - Tn_aH_gf converted to units of evapotranspiration (mm hh-1)
*	**LE_Tn_aH_qc** – latent energy flux derived as the residual of Rn_Avg_qc, Tn_aH_qc, and G_qc where available
*	**LE_Tn_aH_gf** – latent energy flux derived as the residual of Rn_Avg_gf, Tn_aH_gf, and G_gf where available
*	**ET_Tn_aH_qc** -  LE_Tn_aH_qc converted to units of evapotranspiration (mm hh-1)
*	**ET_Tn_aH_gf** -  LE_Tn_aH_gf converted to units of evapotranspiration (mm hh-1)

*	**SR_H_qc** – average of uncalibrated quality controlled sensible heat flux from both thermocouples
*	**SR_H_gf** – average of uncalibrated gap filled sensible heat flux from both thermocouples
*	**SR_alpha_pos** - calibration coefficient used to calibrate positive sensible heat fluxes derived from an average of both thermocouples
*	**SR_alpha_neg** - calibration coefficient used to calibrate negative sensible heat fluxes derived from an average of both thermocouples
*	**SR_aH_qc** - SR_H_Avg_qc multiplied by the calibration coefficients (W m-2)
*	**SR_aH_gf** - SR_H_Avg_gf multiplied by the calibration coefficients (W m-2)
*	**SR_aH_qc_mm** - SR_aH_Avg_qc converted to units of evapotranspiration (mm hh-1)
*	**SR_aH_gf_mm** - SR_aH_Avg_gf converted to units of evapotranspiration (mm hh-1)
*	**LE_SR_aH_qc** - latent energy flux derived as the residual of Rn_Avg_qc, SR_aH_qc, and G_qc where available
*	**LE_SR_aH_gf** - latent energy flux derived as the residual of Rn_Avg_gf, SR_aH_gf, and G_gf where available
*	**ET_SR_aH_qc** -  LE_SR_aH_qc converted to units of evapotranspiration (mm hh-1)
*	**ET_SR_aH_gf** -  LE_SR_aH_gf converted to units of evapotranspiration (mm hh-1)

## Eddy Covariance and Sonic Anemometer related variables (including residual ET)

*	**H_ECraw** – eddy covariance sensible heat flux without coordinate rotation
*	**H_ECraw** – H_ECraw with quality control procedures applied
*	**H_ECrot** – eddy covariance sensible heat flux with 2D coordinate rotation applied
*	**H_ECrot_cor** – H_ECrot with transducer shadowing correction (Kochendorfer et al. 2012, Horst et al. 2016) and typical spectral correction (Kochendorfer and Paw U 2011). 
*	**H_ECrot_qc** - H_ECrot with quality control procedures applied
*	**H_ECrot_gf** - H_ECrot_qc with gaps filled
*	**H_ECrot_qc_mm** - H_ECrot_qc converted to units of evapotranspiration (mm hh-1)
*	**H_ECrot_gf_mm** - H_ECrot_gf converted to units of evapotranspiration (mm hh-1)
*	**LE_EC_qc** - latent energy flux derived as the residual of Rn_Avg_qc, H_ECrot_qc, and G_qc where available
*	**LE_EC_gf** - latent energy flux derived as the residual of Rn_Avg_gf, H_ECrot_gf, and G_gf where available
*	**ET_EC_qc** -  LE_EC_qc converted to units of evapotranspiration (mm hh-1)
*	**ET_EC_gf** -  LE_EC_gf converted to units of evapotranspiration (mm hh-1)

*	**u_bar** – mean wind speed over the half-hour (calculated from the mean U, V, and W wind components) (m s-1)
*	**u_bar_qc** – u_bar with quality control procedure applied (m s-1)
*	**ustar** – friction velocity (m s-1)
*	**ustar_qc** – ustar with quality control procedure applied (m s-1)
*	**Ux_Avg** – mean wind speed measured along the x-direction (m s-1)
* **Ux_Avg_qc**  – mean wind speed measured along the x-direction with quality control procedure applied (m s-1)
*	**Uy_Avg** – mean wind speed measured along the y-direction (m s-1)
*	**Uy_Avg_qc**  – mean wind speed measured along the y-direction with quality control procedure applied (m s-1)
*	**Uz_Avg** – mean wind speed measured along the z-direction (m s-1)
*	**Uz_Avg_qc**  – mean wind speed measured along the z-direction with quality control procedure applied (m s-1)
*	**Wdir_Avg** – wind direction calculated based on average u and v wind components (degrees from north)
*	**Wdir_cor** – corrected wind direction (degrees from north)
*	**Wdir_qc** – wind direction with quality control procedure applied (degrees from north)
*	**tke** – turbulence kinetic energy (per unit mass, units are m2 s-2)
*	**tke_qc** – turbulence kinetic energy  with quality control procedure applied (per unit mass, units are m2 s-2)
*	**tau** – momentum flux (m2 s-2)
*	**tau_qc** – momentum flux with quality control procedure applied (m2 s-2)
*	**pitch** – pitch angle (degrees)
*	**pitch_qc** – pitch angle with quality control procedure applied (degrees)

*	**cov_uu** – variance of the U wind speed component over the half-hour (m2 s-2)
*	**cov_uu_qc** –  cov_uu with quality control procedure applied (m2 s-2)
*	**cov_uv** – covariance of U and V wind speed components over the half-hour (m2 s-2)
*	**cov_uv_qc** – cov_uv with quality control procedure applied (m2 s-2)
*	**cov_uw** – covariance of U and W wind speed components over the half-hour (m2 s-2)
*	**cov_uw_qc** – cov_uw with quality control procedure applied (m2 s-2)
*	**cov_uT** – covariance of U component with sonic temperature over the half-hour (m s-1 K)
*	**cov_uT_qc** – cov_uT with quality control procedure applied (m s-1 K)
*	**cov_vv** - variance of the V wind speed component over the half-hour (m2 s-2)
*	**cov_vv_qc** – cov_vv with quality control procedure applied (m2 s-2)
*	**cov_vw** – covariance of V and W wind speed components over the half-hour (m2 s-2)
*	**cov_vw_qc** – cov_vw with quality control procedure applied (m2 s-2)
*	**cov_vT** – covariance of V component  with sonic temperature over the half-hour (m s-1 K)
*	**cov_vT_qc** – cov_vT with quality control procedure applied (m s-1 K)
*	**cov_ww** – variance of the vertical wind speed component over the half-hour (m2 s-2)
*	**cov_ww_qc** – cov_ww with quality control procedure applied (m2 s-2)
*	**cov_wT** – covariance of vertical wind speed with sonic temperature over the half-hour (m s-1 K)
*	**cov_wT_qc** – cov_wT with quality control procedure applied (m s-1 K)
*	**cov_TT** – variance of sonic temperature over the half-hour (m2 s-2)
*	**cov_TT_qc** – cov_TT with quality control procedure applied (m2 s-2)


## Volumetric Water Content related variables

*	**PA_uS_1** – output period from CS616 1
*	**PA_uS_2** – output period from CS616 2
*	**PA_uS_3** – output period from CS616 3
*	**PA_uS_4** – output period from CS616 4
*	**PA_uS_5** – output period from CS616 5
*	**PA_uS_1_qc** - PA_uS_1 with quality control procedure applied
*	**PA_uS_2_qc** - PA_uS_2 with quality control procedure applied
*	**PA_uS_3_qc** - PA_uS_3 with quality control procedure applied
*	**PA_uS_4_qc** - PA_uS_4 with quality control procedure applied
*	**PA_uS_5_qc** - PA_uS_5 with quality control procedure applied
*	**VW_1** – uncalibrated volumetric water content measured by CS616 1 (depth given in .html file for each station)
*	**VW_2** – uncalibrated volumetric water content measured by CS616 2 (depth given in .html file for each station)
*	**VW_3** – uncalibrated volumetric water content measured by CS616 3 (depth given in .html file for each station)
*	**VW_4** – uncalibrated volumetric water content measured by CS616 4 (depth given in .html file for each station)
*	**VW_5** – uncalibrated volumetric water content measured by CS616 5 (depth given in .html file for each station)
*	**VW_1_qc** – VW_1 with quality control procedure applied
*	**VW_2_qc** – VW_2 with quality control procedure applied
*	**VW_3_qc** – VW_3 with quality control procedure applied
*	**VW_4_qc** – VW_4 with quality control procedure applied
*	**VW_5_qc** – VW_5 with quality control procedure applied

## Relative Humidity and Temperature related variables

*	**RH** – relative humidity (percent)
*	**RH_qc** – relative humidity with quality control procedure applied (percent)
*	**Ta_Avg** – mean air temperature measured in the cover of a naturally-aspirated radiation shield (°C)  
*	**Ta_Avg_qc** – mean air temperature measured in the cover of a naturally-aspirated radiation shield with quality control procedures applied (bad data removed) – includes de-spiking and removal of intermittent or anomalous measurements associated with issues such as low battery power or sensor damage (W m-2)(°C)  
*	**Td_Avg** – mean dewpoint temperature measured (°C) 
*	**Td_Avg_qc** – mean dewpoint temperature measured with quality control procedures applied (bad data removed) – includes de-spiking and removal of intermittent or anomalous measurements associated with issues such as low battery power or sensor damage (W m-2) (°C) 

## IRGASON station-specific variables

* **IRGASON_LE** - latent energy flux measured by the IRGASON using eddy covariance
* **IRGASON_LE_WPL** - IRGASON_LE with the Webb, Pearman, and Leuning (1980) correction applied
* **IRGASON_LE_WPL_cor** - IRGASON_LE_WPL multiplied by 1.08 to correct for transducer shadowing (Horst et al. 2016) and typical spectral correction (Kochendorfer and Paw U 2011). 
* **IRGASON_LE_WPL_qc** - IRGASON_LE_WPL_cor with quality control procedures applied. The IRGASON had a lot more problems with spikes than most of the other variables and required extra quality control measures. Incomplete half-hours where the number samples taken by the IRGASON was less than 18000 were removed. Values below -50 W/m^2 were removed due to the possibility of condensation interfering with the measurements. Likewise, half-hours where precipitation was recorded were removed. Half-hours when wind direction was within 45 degrees from south were removed to avoid periods when the sampling volume was downwind of the sensor body (since the IRGASON is not omni-directional like the R.M. Young 81000RE used at the other stations). Half-hours when net radiation was less than zero, but the IRGASON registered LE values greater than 200 W/m^2 were removed as suspect. Finally if a moving median (29 half-hours) and the difference between the IRGASON_LE and the median was calculated. Half-hour values where this difference fell more than three standard deviations away from the median were removed as suspect. (W/m^2)
* **IRGASON_ET_WPL_qc** - IRGASON_LE_WPL_qc coverted into units of ET (mm/half-hour)
* **IRGASON_LE_WPL_gf** - IRGASON_LE_WPL_qc with gaps filled (up to 5 consecuative half-hours) (W/m^2)
* **IRGASON_ET_WPL_gf** - IRGASON_LE_WPL_qc coverted into units of ET (mm/half-hour)

* **n_obs_csat** - number of samples from the IRGASON sonic anemometer used in the half-hourly stats (18000 for a complete half-hour at 10Hz)  
* **n_obs_licor** - number of samples from the IRGASON gas analyzer used in the half-hourly stats (18000 for a complete half-hour at 10Hz)  

* **CNR4TC_Avg** - average temperature of the CNR4 radiometer (°C)
* **LDn_Avg** - longwave radiation measured by the lower pyrgeometer on the CNR4, uncorrected for instrument temperature (W/m^2) 
* **LDnCo_Avg** - longwave radiation measured by the lower pyrgeometer on the CNR4,corrected for instrument temperature (W/m^2)
* **LUp_Avg** - longwave radiation measured by the upper pyrgeometer on the CNR4, uncorrected for instrument temperature (W/m^2)
* **LUpCo_Avg** - longwave radiation measured by the upper pyrgeometer on the CNR4,corrected for instrument temperature (W/m^2)
* **SDn_Avg** - shortwave radiation measured by the lower pyranometer on the CNR4 (W/m^2) 
* **SUpt_Avg** - shortwave radiation measured by the upper pyranometer on the CNR4 (W/m^2) 
* **RlNet_Avg** - net longwave radiation measured by the CNR4  (W/m^2) 
* **RsNet_Avg** - net shortwave radiation measured by the CNR4  (W/m^2) 

* **Pcp_Tot** - preciptation measured by rain-gauge (mm/half-hour)

* **ST1** - soil temperature measured by first set of TCAV-averaging soil thermocouples (°C)
* **ST1_qc** - ST1 with quality control procedure applied (°C) 
* **ST2** - soil temperature measured by second set of TCAV-averaging soil thermocouples (°C)
* **ST2_qc** - ST2 with quality control procedure applied (°C) 
* **ST3** - soil temperature measured by third set of TCAV-averaging soil thermocouples (°C) 
* **ST3_qc** - ST3 with quality control procedure applied (°C) 





