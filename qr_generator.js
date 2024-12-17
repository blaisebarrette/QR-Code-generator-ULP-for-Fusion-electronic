// Import QR code library
const QRCode = require('qrcode-generator');

// Get URL from command line argument
const url = process.argv[2];
const size = parseInt(process.argv[3]) || 1000;

if (url) {
    // Create QR Code
    const qr = QRCode(1, 'L');
    qr.addData(url);
    qr.make();

    // Get the matrix and output directly
    const moduleCount = qr.getModuleCount();
    for (let row = 0; row < moduleCount; row++) {
        let line = '';
        for (let col = 0; col < moduleCount; col++) {
            line += qr.isDark(row, col) ? '1' : '0';
        }
        console.log(line);
    }
} 