from PIL import Image, ImageDraw, ImageFont
import csv
import os

# Configuration
CSV_FILE = "names.csv"
CERTIFICATE_TEMPLATE = "template.jpeg"  # Certificate template without "Participant Name"
OUTPUT_FOLDER = "output"
FONT_PATH = "./ProductSans-Medium.ttf"  # Replace with the path to your font
FONT_SIZE = 50  # Updated font size
TEXT_COLOR = "black"  # Text color for the participant's name

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def generate_certificate(template_file, output_file, participant_name):
    try:
        # Open the certificate template
        image = Image.open(template_file)
        draw = ImageDraw.Draw(image)

        # Load the font
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

        # Get image dimensions
        image_width, image_height = image.size

        # Calculate the bounding box of the participant's name
        text_bbox = draw.textbbox((0, 0), participant_name, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Define text position (centered horizontally and approximate vertical alignment)
        text_x = (image_width - text_width) // 2
        text_y = int(image_height * 0.42)  # Adjust multiplier for vertical positioning

        # Draw the participant's name directly
        draw.text((text_x, text_y), participant_name, fill=TEXT_COLOR, font=font)

        # Save the modified certificate
        image.save(output_file)
        print(f"Certificate generated for: {participant_name}")
    except Exception as e:
        print(f"Error generating certificate for {participant_name}: {e}")

# Read names from the CSV file
with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        participant_name = row['Full Name'].strip()
        output_file = os.path.join(OUTPUT_FOLDER, f"{participant_name}_certificate.png")
        generate_certificate(CERTIFICATE_TEMPLATE, output_file, participant_name)
