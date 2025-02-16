import numpy as np
from astropy.io import fits
from astropy.table import Table
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
from astropy.utils.data import download_file


event_filename = 'C:/Users/23rou/Downloads/gds-barrufet-s67-v2_prism-clear_2198_8777.spec.fits'
hdu_list = fits.open(event_filename, memmap=True)
hdu_list.info()
print(hdu_list)
from astropy.io import fits
from astropy.table import Table

def show_fits_table(file_path, extension=1):
    """
    Reads a FITS file and displays its data as a table.
    
    Parameters:
    file_path (str): Path to the FITS file.
    extension (int): HDU extension number containing the table (default is 1).
    
    Returns:
    astropy.table.Table: The table representation of the FITS file.
    """
    with fits.open(file_path) as hdul:
        hdul.info()  # Display FITS file structure
        if len(hdul) > extension:
            data = Table(hdul[extension].data)

            print(data)
            return data
        else:
            print(f"Extension {extension} not found in the FITS file.")

from astropy.io import fits
from astropy.table import Table
import numpy as np

def show_fits_table_filtered(file_path, extension=1, flux_column="FLUX", wave_column='WAVE'):
    """
    Reads a FITS file, filters out rows where the FLUX column is NaN, 
    converts wavelength to angstroms, and displays the data as a table.
    
    Parameters:
    file_path (str): Path to the FITS file.
    extension (int): HDU extension number containing the table (default is 1).
    flux_column (str): Name of the flux column to filter NaN values.
    wave_column (str): Name of the wavelength column to convert to angstroms.
    wave_unit (str): Unit of the wavelength column (default is 'nm', converted to angstroms).
    
    Returns:
    astropy.table.Table: The processed table.
    """
    with fits.open(file_path) as hdul:
        hdul.info()  # Display FITS file structure
        if len(hdul) > extension:
            data = Table(hdul[extension].data)
            
            # Filter out NaN flux values
            if flux_column in data.colnames:
                mask = ~np.isnan(data[flux_column])
                data = data[mask]
            else:
                print(f"Column '{flux_column}' not found in the FITS file.")
                return
            
            # Convert wavelength to angstroms if the column exists
            if wave_column in data.colnames:
                  # Convert units (microns to Å)
                data[wave_column] = data[wave_column] * 1000
            
            print(data)
            return data
        else:
            print(f"Extension {extension} not found in the FITS file.")


show_fits_table_filtered("C:/Users/23rou/Downloads/icnk04020_drc.fits/icnk04020_drc.fits")
# TO-DO: REPLACE
