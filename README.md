# TIFF to PNG Converter

This is a simple Python script that converts TIFF images to PNG format.

## Features

- Converts TIFF images to PNG format.
- Supports batch conversion of multiple TIFF images in a folder.
- Provides a graphical user interface (GUI) for selecting input and output folders.
- Handles compatibility issues by converting the image mode to RGBA before saving as PNG.
- Displays conversion status and error messages.

## Requirements

- Python 3.6 or above
- Pillow package (for image processing)

## Installation

1. Clone or download this repository.

2. Install the required packages by running the following command:

   ```bash
   pip install Pillow
   
## Usage

1. Open a terminal or command prompt.

2. Navigate to the project directory.

3. Run the following command to start the converter:

   ```bash
   python convert_tiff_to_png.py

4. The GUI window will open.

5. Select the input folder containing the TIFF images by clicking the "Select Input Folder" button.

6. Select the output folder where the converted PNG images will be saved by clicking the "Select Output Folder" button.

7. Click the "Convert" button to start the conversion process.

8. The conversion progress will be displayed in the GUI window, and the converted PNG images will be saved in the output folder.

## Limitations
Large TIFF images with dimensions exceeding 89478485 pixels may trigger a warning. This is a security measure to prevent potential decompression bomb DOS attacks. If you encounter this warning, proceed with caution and ensure the TIFF images are from trusted sources.
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please create an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
```bash
Feel free to use this updated version in your README file.
