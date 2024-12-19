# Certificate_Rename-in-bulk

This script generates personalized certificates for participants using a predefined template. The script reads participant names from a CSV file and places them on the certificate template, outputting individual certificate images.

## Requirements

- Python 3.x
- `Pillow` library for image manipulation (Install via `pip install Pillow`).
- A CSV file containing participant names.
- A certificate template image (`.jpeg`, `.png`, etc.) with a placeholder for the participant's name.
- A font file (e.g., `.ttf`) for the text on the certificate.

## Files

- **`certificate_generator.py`**: The Python script to generate the certificates.
- **`names.csv`**: A CSV file containing a list of participants' full names.
- **`template.jpeg`**: A certificate template image with a placeholder for the participant's name.
- **`ProductSans-Medium.ttf`**: The font file used for rendering text (modify the path in the script if necessary).
- **`output/`**: The folder where generated certificates will be saved.

## Setup

1. Place the `certificate_generator.py`, `names.csv`, and the certificate template image in the same directory.
2. Make sure to update the `FONT_PATH` and `CERTIFICATE_TEMPLATE` variables in the script:
   - **`FONT_PATH`**: The path to your `.ttf` font file.
   - **`CERTIFICATE_TEMPLATE`**: The file name or path to your certificate template image.
3. Modify the `CSV_FILE` variable to point to your `names.csv` file.

## CSV Format

The `names.csv` file should have the following format:

```csv
Full Name
John Doe
Jane Smith
...

