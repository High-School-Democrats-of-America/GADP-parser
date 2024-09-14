# GADP-parser

## Description

This project provides a Python script to extract text from images of Georgia driver's permits using Optical Character Recognition (OCR) with Tesseract-OCR. The script enhances the image, extracts text, and saves the text to a CSV file.

## Features

- Image enhancement using OpenCV
- OCR text extraction with Tesseract-OCR
- Saves extracted text to a CSV file
- Sample image from the Georgia DDS provided for demonstration

## Disclaimer

This project is independent of the Georgia Department of Driver Services (DDS) and is not officially endorsed by or affiliated with DDS. The information provided in this project is for educational and informational purposes only. DDS is not responsible for any errors or omissions in the data or for any consequences arising from the use of this information.

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

- [Georgia DDS](https://dds.georgia.gov/license-card-information): Sample image used in this project.
- [OpenCV](https://opencv.org/) - Computer vision library (Apache License 2.0)
- [Pytesseract](https://github.com/madmaze/pytesseract) - Python wrapper for Tesseract (Apache License 2.0)
- [Pandas](https://pandas.pydata.org/) - Data analysis library (BSD 3-Clause License)
- [Pillow](https://python-pillow.org/) - Image processing library (HPND License)


### Additional Files

- **`requirements.txt`**: List of dependencies: 
   - opencv-python
   - pytesseract
   - pandas
   - Pillow

