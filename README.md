# QR Code Generator ULP for Fusion Electronics

A User Language Program (ULP) for generating QR codes in Autodesk Fusion Electronics (formerly Eagle).

## Requirements
- curl (usually pre-installed on Mac/Linux)
- Internet connection (to access the QR code generator)

## Installation
1. Download `qrcode_generator.ulp`
2. Place it in your ULP directory or any accessible location

## Usage
1. Run the ULP in Fusion Electronics
2. Enter the URL you want to encode
3. Select size and layer
4. Position the QR code as needed
5. Click OK to generate

## How it Works
The ULP uses a web-based QR code generator to create the matrix, then converts it to rectangles in your PCB design.

## Files
- `qrcode_generator.ulp` - Main ULP file
- `qr_generator.html` - Web-based QR code generator