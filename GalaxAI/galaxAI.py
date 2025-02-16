import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import glob
import os

# Load the CSV containing the file paths and labels
data_path = 'C:/Users/23rou/Downloads/blackholedata/correctCSV/file_paths_with_objects.csv'
data = pd.read_csv(data_path)

# Function to load and process the spectroscopic data (FITS or CSV)
def load_and_process_file(file_path):
    try:
        # Assuming these files are CSVs, but adjust this depending on your data type
        df = pd.read_csv(file_path)

        # Example feature extraction: computing basic statistics (mean, std, etc.) from the data
        # You might want to replace this with something specific to your data format
        features = df.describe().loc[['mean', 'std']].values.flatten()
        
        # Return a flattened array of statistics as features
        return features
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return np.zeros(10)  # Return a vector of zeros if there's an error

# Create feature matrix X and labels y
X = []
y = []

for index, row in data.iterrows():
    file_path = row['FITS File Path']
    label = row['Object Type']
    
    # Load the file and extract features
    features = load_and_process_file(file_path)
    X.append(features)
    
    # Append the label (0 for 'AGN', 1 for 'galaxy')
    y.append(0 if label == 'AGN' else 1)

# Convert to numpy arrays
X = np.array(X)
y = np.array(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Print the classification report
print(classification_report(y_test, y_pred, target_names=['AGN', 'galaxy']))

# Function to predict labels for new data
def predict(file_path):
    features = load_and_process_file(file_path)
    prediction = clf.predict([features])
    return 'AGN' if prediction == 0 else 'galaxy'

# Example usage: Predict the label for a new file
new_file_path = 'C:/Users/23rou/Downloads/blackholedata/agns/smbh_CentauriVoid.csv'
prediction = predict(new_file_path)
print(f"The prediction for {new_file_path} is: {prediction}")
