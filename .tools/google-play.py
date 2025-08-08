from google_play_scraper import app

url = 'com.tomtom.speedcams.android.map'

result = app(url)
print(result['developer'])  # Developer name
print(result['developerEmail'])  # Developer email
print(result['developerWebsite'])  # Developer website

 
import zipfile
from cryptography.hazmat.primitives import hashes
#from cryptography.hazmat.primitives.serialization import load_der_x509_certificate
from cryptography.x509 import load_der_x509_certificate

def extract_certificate(apk_path):
    try:
        # Open the APK file (ZIP format)
        with zipfile.ZipFile(apk_path, 'r') as apk:
            # Look for the certificate file in META-INF/
            cert_file = next(
                (f for f in apk.namelist() if f.startswith('META-INF/') and f.endswith('.RSA')),
                None
            )
            if not cert_file:
                raise FileNotFoundError("Certificate file not found in APK.")

            # Extract the certificate file
            cert_data = apk.read(cert_file)

            # Parse the certificate (DER format)
            cert = load_der_x509_certificate(cert_data)

            # Extract SHA-1 and SHA-256 fingerprints
            sha1_fingerprint = cert.fingerprint(hashes.SHA1()).hex()
            sha256_fingerprint = cert.fingerprint(hashes.SHA256()).hex()

            return {
                "issuer": cert.issuer.rfc4514_string(),
                "subject": cert.subject.rfc4514_string(),
                "sha1": sha1_fingerprint,
                "sha256": sha256_fingerprint,
            }

    except Exception as e:
        print(f"An error occurred: {e}")
        return None



import subprocess
import os

def download_apk(app_id, output_dir):
    try:
        # Command to run playstore-downloader
        command = [
            "playstore-downloader",
            "-d", app_id,       # App ID (package name)
            "-o", output_dir    # Output directory for APK
        ]

        # Run the command
        result = subprocess.run(command, capture_output=True, text=True)

        # Check for errors
        if result.returncode == 0:
            print("APK downloaded successfully!")
            
            # Extract the APK file path from the output
            output_lines = result.stdout.splitlines()
            for line in output_lines:
                if line.startswith("Saved to:"):  # Look for the line that indicates file path
                    apk_path = line.split("Saved to:")[-1].strip()
                    print(f"APK Path: {apk_path}")
                    return apk_path
            
            print("Could not determine the APK file path from the output.")
            return None
        else:
            print("Error downloading APK:")
            print(result.stderr)  # Error output
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
# Example usage
app_id = url  # Replace with the app's package name
output_dir = "./apks"    # Replace with your desired output directory

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

apk_path = download_apk(app_id, output_dir)
if apk_path:
    print(f"APK downloaded to: {apk_path}")

result = extract_certificate(apk_path)
if result:
    print("Certificate Details:")
    print(f"Issuer: {result['issuer']}")
    print(f"Subject: {result['subject']}")
    print(f"SHA-1 Fingerprint: {result['sha1']}")
    print(f"SHA-256 Fingerprint: {result['sha256']}")