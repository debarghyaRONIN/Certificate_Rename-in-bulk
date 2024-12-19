# Certificate_Rename-in-bulk


This script generates certificates with participant names by overlaying text on a certificate template image. The script reads participant names from a CSV file and creates personalized certificates for each participant.

Features

Generates certificates from a pre-defined template.

Uses customizable font settings (font type, size, and color).

Supports batch processing of participant names from a CSV file.

Automatically saves certificates as PNG files in a specified output folder.

Requirements

Prerequisites

Ensure the following are installed on your system:

Python 3.6+

Pillow (PIL) library

Installation

Install Python dependencies:

pip install pillow

Configuration

The script uses the following configuration variables:

CSV_FILE: The path to the CSV file containing participant names. Default: names.csv

CERTIFICATE_TEMPLATE: The path to the certificate template image (JPEG format). Default: template.jpeg

OUTPUT_FOLDER: The folder where generated certificates will be saved. Default: output

FONT_PATH: Path to the .ttf font file used for text. Replace with the path to your font file. Default: ./ProductSans-Medium.ttf

FONT_SIZE: Font size for the participant names. Default: 50

TEXT_COLOR: Text color for the participant names. Default: black

Usage

Prepare the Input CSV File:
The CSV file should include a column titled Full Name, containing the names of the participants. Example:

Full Name
John Doe
Jane Smith
Alice Johnson

Prepare the Certificate Template:
Create a certificate template image (JPEG format) with an empty space for the participant name.

Run the Script:
Execute the script by running:

python script_name.py

View Generated Certificates:
Generated certificates will be saved in the output folder. The filenames will follow the format: ParticipantName_certificate.png.

Script Overview

Main Functionality

Opens the certificate template image.

Loads the participant name from the CSV file.

Centers the participant name on the template.

Saves the personalized certificate to the output folder.

Error Handling

The script includes error handling for issues such as missing font files or invalid CSV inputs. Any errors encountered during the certificate generation process are logged to the console.

Troubleshooting

Font Not Found: Ensure the FONT_PATH is set to the correct path of your .ttf font file.

Template File Missing: Verify the path to the CERTIFICATE_TEMPLATE image.

Invalid CSV File: Ensure the input CSV file contains a Full Name column and is formatted correctly.

Example Output

The generated certificates will be in PNG format and include the participant's name positioned in the designated space on the template. Example file name:

John_Doe_certificate.png

License

This script is free to use and modify for personal or educational purposes.
