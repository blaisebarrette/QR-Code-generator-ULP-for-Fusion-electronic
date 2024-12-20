# QR Code Generator ULP for Fusion Electronics

A User Language Program (ULP) for generating QR codes directly on PCB layers in Autodesk Fusion Electronics / Eagle.

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

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests
- Add new language translations

## Version History

See [versions.csv](versions.csv) for complete version history and release notes.

## License

This project is licensed under the MIT License.

## Authors

- Blaise Barrette - Initial design and development

## Acknowledgments

- Thanks to the PythonAnywhere team for hosting the QR code generation service
- Thanks to the Eagle/Fusion360 community for feedback and suggestions
- Thanks to all contributors for language translations