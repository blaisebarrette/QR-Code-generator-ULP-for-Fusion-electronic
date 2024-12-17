#!/usr/bin/env python3
import cgi
import cgitb
import os
import sys

# Enable detailed error reporting
cgitb.enable()

print("Content-Type: text/plain")
print()

# Print environment info for debugging
print("Python Version:", sys.version)
print("Script Path:", os.path.abspath(__file__))
print("Working Directory:", os.getcwd())

try:
    import qrcode
    from io import StringIO
    
    def generate_qr(url, size=500):
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
            
            return output.getvalue()
            
        except Exception as e:
            return f'Error in generate_qr: {str(e)}'

    def main():
        try:
            # Get form fields
            form = cgi.FieldStorage()
            
            # Get URL and size parameters
            url = form.getvalue('url', '')
            try:
                size = int(form.getvalue('size', '500'))
            except:
                size = 500
            
            print("Received parameters:")
            print(f"URL: {url}")
            print(f"Size: {size}")
            
            if not url:
                print('Error: No URL provided')
                return
            
            # Generate and output QR code
            result = generate_qr(url, size)
            print(result)
            
        except Exception as e:
            print(f"Error in main: {str(e)}")

    if __name__ == "__main__":
        main()
        
except Exception as e:
    print(f"Critical error: {str(e)}") 