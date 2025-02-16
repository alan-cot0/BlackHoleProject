from flask import Flask, request, render_template, send_file
import os
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import io

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('FlaskTEST.html')
# Ensure the 'static' folder exists
if not os.path.exists('static'):
    os.makedirs('static')

# Endpoint to handle the FITS file upload and redshift input
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded FITS file
        fits_file = request.files['fits_file']
        redshift = float(request.form['redshift'])

        # Save the uploaded FITS file
        fits_path = os.path.join('static', 'uploaded.fits')
        fits_file.save(fits_path)

        # Process the FITS file and generate the plot
        plot_path = generate_spectrum_plot(fits_path, redshift)

        return send_file(plot_path, mimetype='image/png')

    return render_template('FlaskTEST.html')


def generate_spectrum_plot(fits_path, redshift):
    with fits.open(fits_path) as hdul:
        if len(hdul) < 2 or hdul[1].data is None:
            raise ValueError("No valid data in the FITS file.")
        data = hdul[1].data
        wave_col = 'wave' if 'wave' in data.columns.names else 'wavelength'
        flux_col = 'flux'

        wavelength = data[wave_col] * 1e4  # Convert micrometers to Angstroms !!!
        flux = data[flux_col]

        # Convert to rest-frame wavelength (must do due to redshift)
        lambda_rest = wavelength / (1 + redshift)

        plt.figure(figsize=(10, 6))
        plt.plot(lambda_rest, flux, label=f"Redshift (z) = {redshift:.4f}", color='blue')
        plt.xlabel("Rest Wavelength (Angstroms)")
        plt.ylabel("Flux")
        plt.title("FITS Spectrum (Wave vs. Flux)")
        plt.legend()
        plt.grid(True)

        # Save the plot as a PNG image
        plot_path = 'static/spectrum_plot.png'
        plt.savefig(plot_path, format="png", bbox_inches='tight')
        plt.close()

        return plot_path


if __name__ == '__main__':
    app.run(debug=True)