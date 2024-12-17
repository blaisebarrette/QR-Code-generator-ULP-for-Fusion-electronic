@app.route('/generate-qr', methods=['GET', 'OPTIONS'])
def generate_qr():
    try:
        # Get and decode URL parameter
        url = unquote(request.args.get('url', ''))
        size = int(request.args.get('size', 1000))
        
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
        
def build_cors_response(content, status_code=200):
    response = Response(content)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Content-Type'] = 'text/plain'
    response.status_code = status_code
    return response 