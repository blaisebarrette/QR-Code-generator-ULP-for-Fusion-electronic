from flask import Flask, request, make_response
import qrcode
from io import StringIO

app = Flask(__name__)

@app.route('/')
def home():
    return 'QR Code Generator Service is running!'

@app.route('/generate-qr')
def generate_qr():
    # Get parameters from URL
    url = request.args.get('url', '')
    size = int(request.args.get('size', '500'))
    
    if not url:
        return 'Error: No URL provided', 400
        
    try:
        # Calculate QR version and box size
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=1,
            border=0,
        )
        
        # Add data
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create matrix
        matrix = qr.get_matrix()
        
        # Convert to string
        output = StringIO()
        for row in matrix:
            output.write(''.join('1' if cell else '0' for cell in row) + '\n')
        
        # Create response
        response = make_response(output.getvalue())
        response.headers["Content-Type"] = "text/plain"
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response
        
    except Exception as e:
        return f'Error: {str(e)}', 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001) 