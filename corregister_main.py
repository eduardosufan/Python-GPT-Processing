'''
Created on 27 feb. 2019

@author: esufan
@brief: coregister CSK and ALOS images with a SNAP GPT batch.
'''

import os


# General parameters:
gpt_path        = "/home/esufan/snap/bin/gpt -e "

# Coregister CSK and ALOS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

path_batch        = "/media/esufan/DATOS/CONAE/FusionSAR/Productos/CorregistroGrueso/batches/"
filename_batch    = "Coregister_CSK_ALOS1_new_python.xml"
path_input        = "/media/esufan/DATOS/CONAE/FusionSAR/Productos/CorregistroGrueso/GPT_test/subsets/"
extension_input   = "tif"
path_output       = "/media/esufan/DATOS/CONAE/FusionSAR/Productos/CorregistroGrueso/GPT_test/subsets/coregistered/"
band              = "" #Sigma_0
image_output_name = "coregistered_CSK_CSK"
extension_output  = "GeoTIFF" #"BEAM-DIMAP" #"HDF5"

# ProductSet-Reader: 
# WARNING: you have to put ProductSet-Reader on top of xml code, to avoid GPT error.
#input_list = "/media/esufan/DATOS/CONAE/FusionSAR/Productos/CorregistroGrueso/GPT_test/subsets/subset_CSKS2_SCS_B_HI_09_HH_RA_SF_20140319104632_20140319104641_ML_CAL_SPK_TC.tif,/media/esufan/DATOS/CONAE/FusionSAR/Productos/CorregistroGrueso/GPT_test/subsets/subset_ALPSRP273806550-L1_ML_CAL_SPK_TC.tif"
#input_list = "/media/esufan/DATOS/CONAE/FusionSAR/Productos/CorregistroGrueso/GPT_test/subsets/subset_CSKS3_SCS_B_HI_08_HH_RA_SF_20160512104404_20160512104411_ML_CAL_SPK_TC.tif,/media/esufan/DATOS/CONAE/FusionSAR/Productos/CorregistroGrueso/GPT_test/subsets/subset_CSKS2_SCS_B_HI_08_HH_RA_SF_20160511104402_20160511104409_ML_CAL_SPK_TC.tif"
input_list = "/media/esufan/DATOS/CONAE/FusionSAR/Productos/CorregistroGrueso/GPT_test/subsets/subset_CSKS3_SCS_B_HI_08_HH_RA_SF_20160512104404_20160512104411_ML_CAL_SPK_TC.tif,/media/esufan/DATOS/CONAE/FusionSAR/Productos/CorregistroGrueso/GPT_test/subsets/subset_CSKS2_SCS_B_HI_09_HH_RA_SF_20140319104632_20140319104641_ML_CAL_SPK_TC.tif"

# CreateStack:
resampling_type       = "BICUBIC_INTERPOLATION"
initial_offset_method = "Orbit"
output_extents        = "Minimum" #Maximum #Master

# Cross-Correlation:
n_gcps                            = "2000"
coarse_registration_window_width  = "128"
coarse_registration_window_height = "128"
row_interp_factor                 = "2"
col_interp_factor                 = "2"
max_interation                    = "10"
gcp_tolerance                     = "0.5"
only_GCPs_on_land                 = "false"

# Warp:
rms_threshold         = "0.05"
warp_polynomial_order = "1"
interpolation_method  = '"Cubic convolution (6 points)"'
open_residuals_file   = "true"



def coregister_CSK_ALOS():
    """
    Coregister CSK and ALOS 1 images specified in filenames.
    You must configure parameters below above in module.
    Processed image is written into path_output directory.
    WARNING: you have to put ProductSet-Reader on top of xml code, to avoid GPT error.
    
    Parameters
    ----------
    -.

    Returns
    -------
    -.
    """

    print("Starting coregistration")
    
    # Check if directory exists. If not, creates directory.
    if not os.path.exists(path_output):
        print("Creating output directory.")
        os.makedirs(path_output)

    # Create gpt command to run process.
    gpt_command = gpt_path + path_batch + filename_batch + ' -Pinput_list=' + input_list + ' -Presampling_type=' + resampling_type + ' -Pinitial_offset_method=' + initial_offset_method + ' -Poutput_extents=' + output_extents + ' -Pn_gcps=' + n_gcps + ' -Pcoarse_registration_window_width=' + coarse_registration_window_width + ' -Pcoarse_registration_window_height=' + coarse_registration_window_height + ' -Prow_interp_factor=' + row_interp_factor + ' -Pcol_interp_factor=' + col_interp_factor + ' -Pmax_interation=' + max_interation + ' -Pgcp_tolerance=' + gcp_tolerance + ' -Ponly_GCPs_on_land=' + only_GCPs_on_land + ' -Prms_threshold=' + rms_threshold + ' -Pwarp_polynomial_order=' + warp_polynomial_order + ' -Pinterpolation_method=' + interpolation_method + ' -Popen_residuals_file=' + open_residuals_file + ' -Pfilename_output=' + path_output + image_output_name + ' -Pextension_output=' + extension_output
    print("Executing: ", gpt_command)

    os.system(gpt_command)

    print("End of coregistration.")
    #WINDOWS
    #system(['gpt NEST_HI.xml ',' -Pinput=',input,' -Pnlook=',num2str(nlooks),' -PAncho=',num2str(Ancho),' -PAlto=',num2str(Alto), ' -PBordeX=',num2str(BordeX), ' -PBordeY=',num2str(BordeY),' -Poutput=',output,' -PBand=',band])  


if __name__ == '__main__':

    coregister_CSK_ALOS()