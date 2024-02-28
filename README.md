# Anti-Virus-Software

## Anti Virus Application

### Features

1. **Main Window:**
   - The main window of the Anti Virus application displays the title "Anti Virus Software."
   - It includes three buttons: "EXIT," "SCAN NOW," and "SCHEDULE SCAN."

2. **Exit Button:**
   - Clicking the "EXIT" button terminates the application.

3. **Scan Now Button:**
   - Clicking the "SCAN NOW" button initiates a scan using the `MalwareScanner` class.

4. **Schedule Scan Button:**
   - Clicking the "SCHEDULE SCAN" button opens a new window allowing users to schedule a future scan.

5. **Schedule Scan Window:**
   - Users can input a time and choose the unit (seconds, minutes, or hours) to schedule a scan.
   - Clicking the "Schedule Scan" button sets a timer for the scheduled scan.
   - If a scan is already scheduled, it cancels the previous schedule.

### Schedule Scan Logic
- The schedule scan logic converts the user input into seconds and uses the Tkinter `after` method to schedule a scan.
- Users are asked to confirm the scan before it starts.

## Malware Scanner

### Features

1. **Main Window:**
   - The Malware Scanner has a title "Anti Virus Software."
   - Users can choose to scan a directory or a specific file.

2. **Scan Directory:**
   - Clicking "Scan a Directory" allows users to choose a directory for scanning.
   - The application recursively scans all files in the selected directory.

3. **Scan File:**
   - Clicking "Scan a File" allows users to choose a specific file for scanning.

4. **Scan Results:**
   - If a file is identified as malicious based on predefined hashes, an alert is shown.
   - If a file is not identified as malicious, an information message is displayed.

5. **Hashing Algorithm:**
   - The scanner uses various hashing algorithms (MD5, SHA-1, SHA-256) to compare file hashes against a predefined list of known malicious file hashes.

### Malicious Hashes
- The `malicious_hashes` dictionary contains sample malicious file hashes. Replace these with actual hashes for real-world use.

### Output
  - <img width="456" alt="image" src="https://github.com/GOVINDFROMINDIA/Anti-Virus-Software/assets/79012314/27c6623f-7bbc-4fb8-bb21-e1a61c549421">
  
  - <img width="299" alt="image" src="https://github.com/GOVINDFROMINDIA/Anti-Virus-Software/assets/79012314/db92d0d4-4fb9-4b88-9c2a-dce7c0c22ec3">
  
  - <img width="455" alt="image" src="https://github.com/GOVINDFROMINDIA/Anti-Virus-Software/assets/79012314/b14f69b2-da82-468f-ab60-127f8dbd8ba1">
  
  - <img width="449" alt="image" src="https://github.com/GOVINDFROMINDIA/Anti-Virus-Software/assets/79012314/30627a6d-0bcb-43f8-80bd-b322cf68a99d">
  
  - <img width="452" alt="image" src="https://github.com/GOVINDFROMINDIA/Anti-Virus-Software/assets/79012314/a2de1e5a-864e-4386-8afd-42b59f2c139f">

### Tools Used
- https://virusshare.com/
- https://gist.github.com/adulau/4191d44e30fc01df38f1d5fe605fa920
- https://visualtk.com/



