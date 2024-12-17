from flask import Flask, request, Response
import qrcode
from io import StringIO
from urllib.parse import unquote
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    return "QR Code Generator Server is running!"

@app.route('/generate-qr', methods=['GET', 'OPTIONS'])
def generate_qr():
    # Log the incoming request
    logger.debug(f"Received request with args: {request.args}")
    
    # Handle CORS preflight request
    if request.method == 'OPTIONS':
        return build_cors_response('')

    try:
        # Get and decode URL parameter
        url = unquote(request.args.get('url', ''))
        size = int(request.args.get('size', 1000))
        
        logger.debug(f"Processing URL: {url}, Size: {size}")
        
        # Create QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        
        # Convert QR code to ASCII art (1s and 0s)
        matrix = qr.get_matrix()
        output = StringIO()
        for row in matrix:
            output.write(''.join('1' if cell else '0' for cell in row))
            output.write('\n')
        
        return build_cors_response(output.getvalue())
        
    except Exception as e:
        logger.error(f"Error generating QR code: {str(e)}")
        return build_cors_response(f"Error: {str(e)}", 500)

def build_cors_response(content, status_code=200):
    response = Response(content)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Content-Type'] = 'text/plain'
    response.status_code = status_code
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) 