# QR Code Generator Server

This is the server component of the QR Code Generator ULP for Eagle/Fusion 360. It's currently hosted on PythonAnywhere.

## Overview
The server provides a simple REST API endpoint that converts URLs into QR codes in a format compatible with Eagle/Fusion 360's ULP system.

## API Endpoint
- **URL**: `https://blaisebarrette.pythonanywhere.com/generate-qr`
- **Method**: GET
- **Parameters**:
  - `url`: The URL to encode (URL-encoded)
  - `size`: Size of the QR code (default: 1000)

## Dependencies
- Flask==3.0.2
- qrcode==7.4.2

## Local Development
To run the server locally:
1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `python server.py`
3. Server will start on `http://127.0.0.1:5001`

## Deployment
Currently deployed on PythonAnywhere at `blaisebarrette.pythonanywhere.com` 