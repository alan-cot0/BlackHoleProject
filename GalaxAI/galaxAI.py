import pandas as pd
import numpy as np
import astropy.io.fits as fits
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def load_and_preprocess_data(csv_path):
    df = pd.read_csv(csv_path)
    df = df[['zspec', 'Spectroscopy FITS', 'Quiescent Galaxy (0) or Supermassive Black Hole (1)']]
    
    prominent_features = {
        "H-alpha": (6545, 6585),
        "H-beta": (4845, 4885),
        "H-delta": (4080, 4115),
        "H-gamma": (4320, 4365),
        "O-II": (3710, 3750),
        "O-IIIa": (4940, 4975),
        "O-IIIb": (4990, 5030),
        "N-IIa": (6530, 6565),
        "N-IIb": (6565, 6605)
    }
    
    features = []
    labels = []
    
    for _, row in df.iterrows():
        fits_path = row['Spectroscopy FITS']
        zspec = row['zspec']
        label = row['Quiescent Galaxy (0) or Supermassive Black Hole (1)']
        
        if os.path.exists(fits_path):
            with fits.open(fits_path) as hdul:
                spectrum = hdul[0].data  # Assuming first extension contains the spectrum
                wave = np.arange(len(spectrum))  # Placeholder - ***reminder to return
                
                # Redshift correction
                wave_corrected = wave / (1 + zspec)
                
                feature_vector = []
                
                for feature, (min_wl, max_wl) in prominent_features.items():
                    mask = (wave_corrected >= min_wl) & (wave_corrected <= max_wl)
                    filtered_spectrum = spectrum[mask]
                    
                    if len(filtered_spectrum) > 0:
                        feature_vector.extend([
                            np.mean(filtered_spectrum),
                            np.std(filtered_spectrum),
                            np.max(filtered_spectrum),
                            np.min(filtered_spectrum)
                        ])
                    else:
                        feature_vector.extend([0, 0, 0, 0])  # Placeholder if no data in range
                
                features.append(feature_vector)
                labels.append(label)
    
    return np.array(features), np.array(labels)

def train_and_evaluate(features, labels):
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

if __name__ == "__main__":
    csv_path = "C:/Users/23rou/Documents/Black Holes Versus Quiescent Galaxies/trainingData.csv"  
    features, labels = load_and_preprocess_data(csv_path)
    train_and_evaluate(features, labels)