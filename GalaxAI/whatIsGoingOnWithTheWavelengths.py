from astropy.io import fits

# Load the FITS file
fits_image_filename = 'C:/Users/23rou/Downloads/gds-barrufet-s67-v2_prism-clear_2198_8777.spec.fits'
hdul = fits.open(fits_image_filename)

# Iterate through HDUs to find table data
for hdu in hdul:
    if isinstance(hdu, fits.BinTableHDU) or isinstance(hdu, fits.TableHDU):
        print("Column names:", hdu.columns.names)
        break  # Stop after finding the first table

# Close the FITS file
hdul.close()


"""
def inspect_fits_file(fits_file):
    with fits.open(fits_file) as hdul:
        data = hdul[1].data
        wavelength = data['wave']  # Wavelength column
        flux = data['flux']  # Flux column

        print("Wavelength Range:")
        print(f"Min: {wavelength.min()} µm")
        print(f"Max: {wavelength.max()} µm")
        print(f"Number of data points: {len(wavelength)}")

# Example usage
fits_files = [
    r"C:/Users/23rou/Downloads/gds-deep-hr-v1_g395h-f290lp_1210_10639.spec.fits",
    r"C:/Users/23rou/Downloads/gds-barrufet-s67-v2_prism-clear_2198_8777.spec.fits",
    r"C:/Users/23rou/Downloads/gds-barrufet-s67-v2_prism-clear_2198_8777.spec.fits"
]

for fits_file in fits_files:
    print(f"Inspecting {fits_file}:")
    inspect_fits_file(fits_file)
    print("\n" + "="*40 + "\n")
"""