var system = require('system');
var page = require('webpage').create();

var url = system.args[1];
var size = system.args[2] || 1000;

page.open('https://blaisebarrette.com/ulp_qrcode_generator/qr_generator.html?url=' + encodeURIComponent(url) + '&size=' + size, function(status) {
    if (status === 'success') {
        // Wait for JavaScript execution
        setTimeout(function() {
            var content = page.content;
            console.log(content);
            phantom.exit();
        }, 1000);
    } else {
        console.log('Failed to load page');
        phantom.exit(1);
    }
}); 