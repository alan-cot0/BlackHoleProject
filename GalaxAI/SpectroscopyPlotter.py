import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

prominent_features = {
    "Ca II H min": 3968,
    "Ca II K": 3934,
    "H-Delta": 4102,
    "H-Gamma": 4340,
    "H-Beta": 4861,
    "O III": 5007,
    "Mg I": 5175,
    "Fe I": 5270,
    "Na I": 5893,
    "H-alpha + N II": 6563,
    "S II": 6716,
}

def process_fits_file(fits_file, redshift):
    with fits.open(fits_file) as hdul:
        data = hdul[1].data
        wavelength = data['wave'] * 1e4  # Convert micrometers to Angstroms - DO NOT EDIT THIS LINE
        flux = data['flux']

    # Here, we convert to rest frame to standardize our spectrums.
    lambda_rest = wavelength / (1 + redshift)
    return lambda_rest, flux

def plot_quiescent_spectra(fits_files, redshifts):
    """
    Plots quiescent galaxy spectra from all of the FITS files you add to the list (fits_files),
    sorted by redshifts which you add to the other list (redshifts). Make sure to keep the redshifts
    in the same order that your files are so they correspond correctly.
    """
    plt.figure(figsize=(10, 8))

    #Here, we plot the spectrums themselves; wavelength versus flux.
    #If the lines are too close together, change offset to be larger.
    for i, (fits_file, z) in enumerate(zip(fits_files, redshifts)):
        offset = 2 #This is where you can change the offset value if you need.
        lambda_rest, flux = process_fits_file(fits_file, z)
        offset = i * offset
        plt.plot(lambda_rest, flux + offset, label=f"z = {z:.2f}")

    # Here we add vertical lines at the locations of all of the significant wavelengths.
    for feature, wavelength in prominent_features.items():
        plt.axvline(x=wavelength, color='gray', linestyle='--', alpha=0.7)
        plt.text(wavelength, 2.85 * len(fits_files), feature, rotation=90, verticalalignment='bottom', fontsize=8, alpha=0.7)

    # Plot everything.
    plt.xlabel("Rest Wavelength (Angstroms)")
    plt.xlim(0, 8000)
    plt.ylabel("Flux + Offset")
    plt.title("Quiescent Galaxy Spectra Sorted by Redshift")
    plt.legend(loc='upper right', fontsize=8)
    plt.grid(False)
    plt.tight_layout()
    plt.show()

# Run the code!
fits_files = ["C:/Users/23rou/Downloads/glazebrook-cos-obs3-v2_prism-clear_2565_20115.spec (2).fits"] #replace this with a list of your own files, or edit the example_files list which appeared under the "Downloaded Data" section.
redshifts = [3.7118] #replace this with a list of your own values which correspond with the files you downloaded; this information is the z-spec column on the DJA.
plot_quiescent_spectra(fits_files, redshifts)