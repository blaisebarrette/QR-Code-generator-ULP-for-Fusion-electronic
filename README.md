# QR Code Generator ULP for Fusion Electronics

⚠️ **MACOS ONLY** - This tool currently works exclusively on macOS systems ⚠️

A simple and efficient tool to generate QR codes directly in Eagle/Fusion360 Electronics.

## System Requirements

- **Operating System**: macOS only
- Eagle/Fusion360 Electronics
- Internet connection

## Features

- QR code generation from URLs
- Smart automatic placement on PCB
- Support for multiple layers (Silkscreen, Documentation)
- Customizable size (250-5000 mils)
- Manual positioning with X,Y coordinates
- Cloud-based generation using PythonAnywhere
- No local installation required

## Installation

1. Download the `qrcode_generator.ulp` file
2. Place it in an accessible folder

That's it! No need to install Python or other dependencies.

## Usage

1. In Eagle/Fusion360 Electronics, open your PCB design
2. Run the ULP script:
   - In Eagle: `File > Run ULP > qrcode_generator.ulp`
   - In Fusion360: `Tools > Run ULP > qrcode_generator.ulp`

3. In the dialog window:
   - Enter the URL for your QR code
   - Choose the size (in mils)
   - Select the destination layer
   - Default position will be calculated automatically
   - You can adjust the position manually if needed

4. Click OK to generate the QR code

## Supported Layers

- Top Silkscreen (tPlace)
- Bottom Silkscreen (bPlace)
- Top Documentation (tDocu)

## Automatic Positioning

The QR code is automatically positioned to avoid conflicts with your design:
- Default position = -(size + 1000) in X and Y
- Example: For a 500 mils QR code, position = -1500,-1500
- This position can be adjusted with the "Update Position" button

## Technical Notes

- QR code is generated via a secure cloud service (PythonAnywhere)
- Minimum size: 250 mils
- Maximum size: 5000 mils
- Positioning range: -50000 to +50000 mils

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

## License

This project is licensed under the MIT License.

## Authors

- Blaise Barrette - Initial design and development
- With help from the Cursor AI team