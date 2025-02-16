import numpy as np
import csv
import random
import os

# Function to generate randomized black hole spectra
def generate_multiple_random_smbh_spectra(num_files=10, output_dir="C:/Users/23rou/Downloads/blackholedata/agns"):
    # Different SMBH names (fictional or inspired by real ones)
    smbh_names = [
        "QuasarX", "HyperionA", "CygnusPrime", "AndromedaCore", "CentauriVoid",
        "BlackfireX", "Vortex8", "Messier9", "DraconisA", "VoidShadow"
    ]
    
    generated_files = []
    for i in range(num_files):
        output_filename = os.path.join(output_dir, f"smbh_{smbh_names[i]}.fits")

        # Define wavelength range (in Angstroms)
        wave_min, wave_max, num_points = 3000, 10000, 5000
        wavelengths = np.linspace(wave_min, wave_max, num_points)

        # Randomize the power-law continuum index (to model accretion disks)
        power_law_index = -1.5 + random.uniform(-0.5, 0.5)  # Varies per SMBH
        flux_continuum = (wavelengths / wave_min) ** power_law_index  

        # Add small random noise
        noise = np.random.normal(scale=random.uniform(0.01, 0.07), size=num_points)
        flux = flux_continuum + noise

        # Random emission line properties (broader for quasars, narrower for Seyferts)
        emission_lines = [
            (random.choice([6563, 4861, 2798, 6400, 5007]),  # Hα, Hβ, Mg II, Fe Kα, O III
             random.uniform(30, 100),  # Broad or narrow emission
             random.uniform(0.5, 3.0))  # Variable strength
            for _ in range(random.randint(3, 6))  # Each SMBH has 3-6 strong lines
        ]

        # Random absorption lines (different ISM conditions per galaxy)
        absorption_lines = [
            (random.choice([7600, 5890, 4300, 5170]),  # O2, Na I D, CH, Mg b
             random.uniform(10, 40),  # Width variation
             random.uniform(0.3, 1.0))  # Strength variation
            for _ in range(random.randint(2, 4))  # Each SMBH has 2-4 absorption features
        ]

        # Apply emission and absorption lines
        for center, width, height in emission_lines:
            flux += height * np.exp(-0.5 * ((wavelengths - center) / width) ** 2)
        for center, width, depth in absorption_lines:
            flux -= depth * np.exp(-0.5 * ((wavelengths - center) / width) ** 2)

        # Save the FITS file (this can be done with astropy or custom methods)
        # For simplicity, we're assuming the FITS file is being saved elsewhere in your code.
        generated_files.append(output_filename)

    return generated_files

# Function to create the CSV with FITS file paths and object type labels
def create_fits_label_csv(galaxy_fits_files, black_hole_fits_files, output_filename="fits_labels.csv"):
    # Open a new CSV file to write the data
    with open(output_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(["FITS File Path", "Object Type"])

        # Write galaxy FITS file paths with label 0
        for galaxy_file in galaxy_fits_files:
            writer.writerow([galaxy_file, 0])

        # Write black hole FITS file paths with label 1
        for black_hole_file in black_hole_fits_files:
            writer.writerow([black_hole_file, 1])

    print(f"CSV file '{output_filename}' created successfully!")

# List of galaxy FITS file paths (replace with actual paths)
galaxy_fits_files = [
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_12.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_13.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_14.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_15.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_16.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_17.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_18.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_19.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_20.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_21.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_22.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_23.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_24.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_25.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_26.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_27.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_28.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_29.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/quiescent_galaxy_Galaxy_30.fits"
]

# List of named black hole FITS file paths
black_hole_fits_files = [
    "C:/Users/23rou/Downloads/blackholedata/agns/smbh_QuasarX.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/smbh_HyperionA.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/smbh_CygnusPrime.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/smbh_AndromedaCore.fits",
    "C:/Users/23rou/Downloads/blackholedata/agns/smbh_CentauriVoid.fits"
]

# Generate 10 randomized black hole spectra and get the paths
random_black_hole_files = generate_multiple_random_smbh_spectra(num_files=10)

# Combine all black hole FITS file paths
all_black_hole_files = black_hole_fits_files + random_black_hole_files

# Call the function to create the CSV with the file paths and labels
output_csv_path = "C:/Users/23rou/Downloads/blackholedata/agns/fits_labels.csv"
create_fits_label_csv(galaxy_fits_files, all_black_hole_files)
