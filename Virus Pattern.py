import os
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Define a directory containing your dataset of known good files (whitelist).
whitelist_dir = "known_good_files/"

# Define a directory containing your dataset of potential malware files.
malware_dir = "potential_malware_files/"


whitelist_files = [os.path.join(whitelist_dir, file) for file in os.listdir(whitelist_dir)]
malware_files = [os.path.join(malware_dir, file) for file in os.listdir(malware_dir)]

whitelist_sizes = np.array([os.path.getsize(file) for file in whitelist_files]).reshape(-1, 1)
malware_sizes = np.array([os.path.getsize(file) for file in malware_files]).reshape(-1, 1)

X = np.vstack((whitelist_sizes, malware_sizes))
y = np.array([0] * len(whitelist_files) + [1] * len(malware_files))

scaler = StandardScaler()
X = scaler.fit_transform(X)

model = IsolationForest(contamination='auto', random_state=42)
model.fit(X)

new_file_path = "new_potential_malware.exe"
new_file_size = np.array([os.path.getsize(new_file_path)]).reshape(1, -1)
new_file_size = scaler.transform(new_file_size)
prediction = model.predict(new_file_size)

if prediction == 1:
    print(f"The file {new_file_path} is flagged as potential malware.")
else:
    print(f"The file {new_file_path} is not considered malware.")

