import cv2
import pytesseract
import pandas as pd
import os
from PIL import Image

# Set the path to the Tesseract-OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path as needed

def enhance_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Denoise (optional, can be adjusted based on the image)
    denoised = cv2.fastNlMeansDenoising(thresh, None, 30, 7, 21)

    return denoised

def extract_text_from_image(image_path):
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"The file at {image_path} does not exist.")

    # Load image using OpenCV
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Failed to load image. Check the file format or path.")

    # Enhance the image
    img_enhanced = enhance_image(img)

    # Save the enhanced image to a file (for viewing purposes)
    enhanced_image_path = 'enhanced_image.png'
    cv2.imwrite(enhanced_image_path, img_enhanced)
    print(f"Enhanced image saved as {enhanced_image_path}")

    # Display the enhanced image
    cv2.imshow('Enhanced Image', img_enhanced)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Use pytesseract to do OCR on the enhanced image with LSTM only
    custom_config = r'--oem 1'
    text = pytesseract.image_to_string(img_enhanced, lang='eng', config=custom_config)
    return text


def save_lines_to_csv(text, csv_filename):
    # Split the text into lines
    lines = text.split('\n')

    # Remove empty lines if desired
    lines = [line for line in lines if line.strip() != '']

    # Create a DataFrame where each line is a row
    df = pd.DataFrame(lines, columns=['Extracted Text'])

    # Save the DataFrame to a CSV file
    df.to_csv(csv_filename, index=False)

def main(image_path, csv_filename):
    try:
        # Extract text from the image
        text = extract_text_from_image(image_path)

        # Print the extracted text for debugging
        print("Extracted Text:")
        print(text)

        # Save each line of text to a CSV file
        save_lines_to_csv(text, csv_filename)
        print(f"Data has been saved to {csv_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Sample image provided by the Georgia Department of Driver Services (DDS)
image_path = 'drivers_license.jpg'  # Path to the image file of the driver's license
csv_filename = 'drivers_license_data.csv'  # Output CSV filename
main(image_path, csv_filename)