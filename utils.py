'''
Created on 25 feb. 2019

@author: esufan
'''

import os

def get_dir_files(directory, extension, start=""):
    """
    Get list containing all files with "extension" in specified directory.

    Parameters
    ----------
    directory: str
      Path to directory containing image files to be listed.
    extension: str
      Desired extension file to be listed.
    start: str
      Firts characters into filename string. For example for ALOS 1 set as "VOL"

    Returns
    -------
    files: str
      List containing all files with extension.
    """
    
    files = []
    for f in os.listdir(directory):
        if f.endswith(extension) and f.startswith(start): 
            #files.append(os.path.join(directory, f))
            files.append(f)

    return files