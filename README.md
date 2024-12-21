# QR Code Generator ULP for Fusion Electronics

A User Language Program (ULP) for generating QR codes directly on PCB layers in Autodesk Fusion Electronics / Eagle.

![Interface preview](<Interface preview.jpg>)

## Features

- QR code generation from URLs
- Automatic placement in the lower-left quadrant
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

1. Download the appropriate ULP file for your operating system
2. Place it in an accessible folder

That's it! No need to install Python or other dependencies.

## Usage

1. In Eagle/Fusion360 Electronics, open your PCB design
2. Run the ULP file:
   - Type `RUN qrcode_generator_mac` (for MacOS)
   - Or `RUN qrcode_generator_win` (for Windows)
3. In the dialog:
   - Enter the URL for your QR code
   - Choose the size (in mils)
   - Select the destination layer
   
The QR code will be automatically placed in the lower-left quadrant of your board.

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

## Known Issues

### QR Code Size Accuracy
Currently, there is a known issue where the generated QR codes appear slightly smaller than the requested size. This affects all QR code versions and sizes:

- The difference is more noticeable with larger sizes
- The QR code maintains its proportions and remains readable
- The issue appears to be related to the way module sizes are calculated and positioned

We are actively working on resolving this issue. If you have experience with Eagle/Fusion ULP development and would like to contribute to solving this problem, please feel free to:
1. Submit a pull request with a proposed solution
2. Open an issue with your findings or suggestions
3. Contact the maintainers directly

### Technical Details of the Issue
- QR codes of different versions (21x21 to 177x177 modules) require different module sizes
- Current calculation attempts to adjust the total size to be perfectly divisible by the number of modules
- Despite correct calculations, the final rendered size is consistently smaller than requested
- Debug information is available in the generated script comments

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

- Thanks to the PythonAnywhere team for hosting the QR code generation service
- Thanks to the Eagle/Fusion360 community for feedback and suggestions
- Thanks to all contributors for language translations
