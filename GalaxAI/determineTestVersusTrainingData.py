import pandas as pd
from sklearn.model_selection import train_test_split

# Define the dataset
data = [
    ("jwst2198", 4.3563, "path1.fits", 0),
    ("jwst2198", 4.6563, "path2.fits", 0),
    ("jwst2198", 3.4713, "path3.fits", 0),
    ("jwst2565", 3.1962, "path4.fits", 0),
    ("jwst2565", 3.1979, "path5.fits", 0),
    ("jwst2565", 3.6921, "path6.fits", 0),
    ("jwst2565", 3.543, "path7.fits", 0),
    ("3C273", 0.158, "path8.fits", 1),
    ("Centaurus-A", 0.00183, "path9.fits", 1),
    ("H1821+643", 0.297, "path10.fits", 1),
    ("IC1101", 0.0777, "path11.fits", 1),
    ("MARKARIAN501", 0.034, "path12.fits", 1),
    ("MESSIER160", 0.01736, "path13.fits", 1),
    ("MESSIER60", 0.00506, "path14.fits", 1),
    ("NGC1600", 0.0156, "path15.fits", 1),
    ("NGC4151", 0.00332, "path16.fits", 1),
    ("NGC5548", 0.01718, "path17.fits", 1),
    ("OJ287", 0.306, "path18.fits", 1),
    ("S50014+81", 3.366, "path19.fits", 1),
    ("SAGITTARIUS-A", 0, "path20.fits", 1),
    ("SOMBRERO", 0.0034, "path21.fits", 1)
]

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Name", "zspec", "FITS_Path", "Label"])

# Group by Name (to prevent data leakage)
grouped = df.groupby("Name")

# Perform stratified split while keeping objects together
train_groups, test_groups = train_test_split(
    list(grouped.groups.keys()), test_size=0.2, stratify=[df[df["Name"] == name]["Label"].values[0] for name in grouped.groups]
)

# Split DataFrame
train_df = df[df["Name"].isin(train_groups)]
test_df = df[df["Name"].isin(test_groups)]

# Display results
print("Training Set:")
print(train_df)

print("\nTest Set:")
print(test_df)

# Save to CSV if needed
train_df.to_csv("train_data.csv", index=False)
test_df.to_csv("test_data.csv", index=False)