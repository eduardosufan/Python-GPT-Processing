'''
Created on 27 feb. 2019

@author: esufan
@brief: process ALOS SLC images with a given SNAP batch process.
Check abd configure all parameters in module. You can optionally apply processing and/or subset, just
configuring APPLY_PROCESSING and APPLY_SUBSET flags.

Subset area can be defined using the following site:
#https://arthur-e.github.io/Wicket/sandbox-gmaps3.html
'''

import os
import utils

# General parameters:
gpt_path        = "/home/esufan/snap/bin/gpt -e "

# Process CSK SLC >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

APPLY_PROCESSING = True # False
path_batch       = "/media/esufan/DATOS/CONAE/FusionSAR/Productos/CorregistroGrueso/batches/"
filename_batch   = "ALOS_1_PRE_PROC_DANILO_SPK_python.xml"
path_input       = "/media/esufan/DATOS/CONAE/FusionSAR/Productos/ALOS1/Level_1.1/"
extension_input  = "zip" #"1__A" 
start_input      = "" #"VOL" 
path_output      = "/media/esufan/DATOS/CONAE/FusionSAR/Productos/CorregistroGrueso/GPT_test/"
band             = "" #Sigma_0
extension_output = "BEAM-DIMAP"#"GeoTIFF" #"HDF5"

# Multilook:
n_looks_range   = "1"
n_looks_azimuth = "2"
square_pixel    = "True"

# Speckle filter:
spk_filter         = '"Lee Sigma"'
n_looks            = "1"
window_size        = "7x7"
sigma              = "0.9"
target_window_size = "3x3"

# SAR-simulation:
DEM            = '"SRTM 1Sec HGT"'
dem_resampling = "BICUBIC_INTERPOLATION"

# Cross-correlation:
n_gcps                = "2000"
coarse_window_width   = "128"
coarse_window_height  = "128"
row_interp_factor     = "2"
col_interp_factor     = "2"
max_iteration         = "10"
gcp_tolerance         = "0.5"
test_GCPs_are_on_land = "false"

# SARSim-Terrain-Correction:
rms_threshold         = "0.5"
pol_warp_order        = "1"
img_resampling_method = "CUBIC_CONVOLUTION"
pixel_spacing_meters  = "7.46"


#-------------------------------------------------------------------------------------------------------------
# Subset:
APPLY_SUBSET = False # True
filename_batch_subset   = "CSK_processed_subset_python.xml"
path_input_subset       = "/media/esufan/DATOS/CONAE/FusionSAR/Productos/CorregistroGrueso/GPT_test/"
extension_input_subset  = "dim" #"GeoTIFF" #"HDF5"
path_output_subset      = "/media/esufan/DATOS/CONAE/FusionSAR/Productos/CorregistroGrueso/GPT_test/subsets/"
extension_output_subset = "GeoTIFF" #"HDF5" #"BEAM-DIMAP"
polygon_subset          = '"POLYGON((-64.53433267374544 -31.303739922598623,-64.3729709794095 -31.303739922598623,-64.3729709794095 -31.43506609553863,-64.53433267374544 -31.43506609553863,-64.53433267374544 -31.303739922598623))"'
#Use polygon defined by https://arthur-e.github.io/Wicket/sandbox-gmaps3.html

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


def subset_image_directory():
    """
    Apply subset to all images in directory specified in path_input.
    """

    print("Subsetting all ", extension_input_subset, "files in ", path_input_subset)
    images = utils.get_dir_files(path_input_subset, extension_input_subset)

    for image in images:
        subset_image(image)

    print("End of subsetting.")

def subset_image(image_input):
    """
    Process ALOS SLC image data given a SNAP batch.
    You must configure parameters below above in module.
    Processed image is written into path_output directory.
    
    Parameters
    ----------
    image_input: str
      Image filename to be processed.

    Returns
    -------
    None.
    """

    image_output_name = "subset_" + image_input.split(".")[0]

    # Check if directory exists. If not, creates directory.
    if not os.path.exists(path_output_subset):
        print("Creating subset output directory.")
        os.makedirs(path_output_subset)

    # Create gpt command to run process.
    gpt_command = gpt_path + path_batch + filename_batch_subset + ' -Pinput=' + path_input_subset + image_input + ' -Ppolygon=' + polygon_subset + ' -Poutput=' + path_output_subset + image_output_name + ' -Pextension_output=' + extension_output_subset
    print("Executing: ", gpt_command)

    os.system(gpt_command)

def process_image_directory():
    """
    Process all images in directory specified in path_input.
    """

    print("Processing all ", extension_input, "files in ", path_input)
    images = utils.get_dir_files(path_input, extension_input, start_input)

    for image in images:
        processs_ALOS(image)
        
    print("End of processing.")

def processs_ALOS(image_input):
    """
    Process ALOS SLC image data given a SNAP batch.
    You must configure parameters below above in module.
    Processed image is written into path_output directory.
    
    Parameters
    ----------
    image_input: str
      Image filename to be processed.

    Returns
    -------
    None.
    """

    image_output_name = image_input.split(".")[0] + "_ML_CAL_SPK_TC"

    # Check if directory exists. If not, creates directory.
    if not os.path.exists(path_output):
        print("Creating output directory.")
        os.makedirs(path_output)

    # Create gpt command to run process.
    gpt_command = gpt_path + path_batch + filename_batch + ' -Pinput=' + path_input + image_input + ' -Pn_looks_range=' + n_looks_range + ' -Pn_looks_azimuth=' + n_looks_azimuth + ' -Psquare_pixel=' + square_pixel + ' -PDEM=' + DEM + ' -Pdem_resampling=' + dem_resampling + ' -Pn_gcps=' + n_gcps + ' -Pcoarse_window_width=' + coarse_window_width + ' -Pcoarse_window_height=' + coarse_window_height + ' -Prow_interp_factor=' + row_interp_factor + ' -Pcol_interp_factor=' + col_interp_factor + ' -Pmax_iteration=' + max_iteration + ' -Pgcp_tolerance=' + gcp_tolerance + ' -Prms_threshold=' + rms_threshold + ' -Ppol_warp_order=' + pol_warp_order + ' -Pimg_resampling_method=' + img_resampling_method + ' -Ppixel_spacing_meters=' + pixel_spacing_meters+ ' -Pspk_filter=' + spk_filter + ' -Pn_looks=' + n_looks + ' -Pwindow_size=' + window_size + ' -Psigma=' + sigma + ' -Ptarget_window_size=' + target_window_size + ' -Poutput=' + path_output + image_output_name + ' -Pformat_output=' + extension_output
    print("Executing: ", gpt_command)

    os.system(gpt_command)

    #WINDOWS
    #system(['gpt NEST_HI.xml ',' -Pinput=',input,' -Pnlook=',num2str(nlooks),' -PAncho=',num2str(Ancho),' -PAlto=',num2str(Alto), ' -PBordeX=',num2str(BordeX), ' -PBordeY=',num2str(BordeY),' -Poutput=',output,' -PBand=',band])  


if __name__ == '__main__':

    if APPLY_PROCESSING:
        process_image_directory()
    if APPLY_SUBSET:
        subset_image_directory()

