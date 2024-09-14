# GADP-parser

## Description

This project provides a Python script to extract text from images of Georgia driver's permits using Optical Character Recognition (OCR) with Tesseract-OCR. The script enhances the image, extracts text, and saves the text to a CSV file.

## Features

- Image enhancement using OpenCV
- OCR text extraction with Tesseract-OCR
- Saves extracted text to a CSV file
- Sample image provided for demonstration

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
3. Ensure Tesseract-OCR is installed. Download it from [here](https://github.com/tesseract-ocr/tesseract) and update the PATH in the script (if necessary):

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo

## Usage

1. Place the image of the driver's license in the same directory as the script or provide the path to the image.
2. Run the script:

   ```bash
   python 1-write.py

3. The extracted text will be saved to ``drivers_license_data.csv``

   ```bash
   your-repo/
   │
   ├── README.md
   ├── requirements.txt
   ├── 1-write.py
   ├── drivers_license.jpg
   ├── enhanced_image.jpg (generated in the program)
   └── drivers-license_data.csv (generated in the program)


## Sample Output

The extracted text from the driver's license will be saved in ``drivers_license_data.csv``, with each line representing a separate piece of text extracted from the image.

## Contributing

1. Fork the repository.
2. Create a feature branch (git checkout -b feature-branch).
3. Commit your changes (git commit -am 'Add new feature').
   -Make frequent and small commits!
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.
   -Once your request is approved you are now a contributor!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Acknowledgements

- Georgia DDS: For the sample image used in this project.
- OpenCV: For image processing capabilities.
- Tesseract-OCR: For optical character recognition.
- Pandas: For data handling and CSV operations.
- Pillow: For image manipulation.


### Additional Files

- **`requirements.txt`**: List of dependencies: 
   - opencv-python
   - pytesseract
   - pandas
   - Pillow

