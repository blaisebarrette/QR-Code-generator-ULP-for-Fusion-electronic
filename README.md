# QR Code Generator ULP for Fusion Electronics

A User Language Program (ULP) for generating QR codes directly on PCB layers in Autodesk Fusion Electronics / Eagle.

![Interface preview](<https://github.com/blaisebarrette/QRCode-ULP-for-Fusion-electronics/blob/main/Media/Interface%20preview.jpg>)

## Features

- QR code generation from URLs
- Automatic placement in the upper-left quadrant
- Support for multiple layers:
  - Top Silkscreen (tPlace)
  - Bottom Silkscreen (bPlace)
  - Top Documentation (tDocu)
  - Bottom Documentation (bDocu)
  - Document (Docu)
- Customizable size (250-5000 mils)
- Cloud-based generation using PythonAnywhere
- Automatic version checking and updates notification
- Multi-language support:
  - English
  - French
  - German
  - Spanish
  - Italian
  - Japanese
  - Korean
  - Chinese
- No local installation required

## System Requirements

Choose the appropriate version for your operating system:
- `qrcode_generator_mac.ulp` for MacOS systems
- `qrcode_generator_win.ulp` for Windows systems

## Installation

1. Download the appropriate ULP file for your operating system.
2. Create a folder named `ULP` in your `Documents/Autodesk` directory.
3. Place the ULP file in the `ULP` folder you just created.
4. Follow this <a href="https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-change-the-directory-path-for-ULPs-in-Fusion-360-Electronics.html" target="_blank">link</a> to learn how to link Fusion Electronics to the ULP folder. You can place future ULP files in this folder for easy access from Fusion Electronics.

That's it! No need to install Python or other dependencies.

## Usage

1. Open your PCB design in Eagle/Fusion360 Electronics.
2. Click the `Run ULP` icon on the 2D PCB `AUTOMATE` toolbar.
3. In the ULP browser, select `qrcode_generator_mac` for MacOS or `qrcode_generator_win` for Windows.
4. Double-click the selected ULP to execute it.
5. Alternatively, type `run` in the command line and press Enter to open the ULP browser.
6. You can also type `RUN qrcode_generator_mac` for MacOS or `RUN qrcode_generator_win` for Windows in the command line and press Enter.
7. In the dialog box:
   - Input the URL for the QR code.
   - Specify the size (in mils).
   - Choose the destination layer.

The QR code will be placed automatically in the upper-left quadrant of your board.

## important

Important Note on URL Length:
Generating a QR code from a long URL increases its complexity. Highly complex QR codes may become difficult to scan if printed too small. If your PCB design has limited space for the QR code, consider using a service like bitly.com to shorten the URL before generating the QR code. This reduces the code’s complexity, making it easier to scan when printed.

Example:

Here is a comparison between QR codes of different sizes, generated from long (left) and short (right) URLs:

![URL size vs complexity](<https://github.com/blaisebarrette/QRCode-ULP-for-Fusion-electronics/blob/main/Media/URL_size_vs_complexity.png>)

## Technical Notes

- QR code is generated via a secure cloud service
- Minimum size: 250 mils
- Maximum size: 5000 mils
- Version checking ensures compatibility
- Automatic mirroring for bottom layers
- Language selection based on system settings

## Error Handling

The ULP includes comprehensive error handling for:
- Network connectivity issues
- API availability
- Version compatibility
- Invalid responses
- File operations

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests
- Add new language translations
- Fix the QR code size accuracy issue
- Add new features
- Improve error handling

## Version History

See [version_history.md](version_history.md) for complete version history and release notes.

## License

This project is licensed under the MIT License.

## Authors

- Blaise Barrette - Initial design and development

## Acknowledgments

- Thanks to <a href="https://github.com/lincolnloop/python-qrcode/tree/main">Pure python QR Code generator</a> for developping thos great and easy to use library
- Thanks to the PythonAnywhere team for hosting the QR code generation service
- Thanks to the Eagle/Fusion360 community for feedback and suggestions
- Thanks to all contributors for language translations
