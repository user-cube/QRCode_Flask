class Home():
    def home(self):
        paths = [
            {
                "titulo": "Simple QR Code",
                "definicao": "Generate a simple QRCode in png",
                "link": "/qrcode",
                "argumento": "Data: QR Code information"
            },
            {
                "titulo": "Logo QR Code",
                "definicao": "Generate a QRCode with logo in png",
                "link": "/qrcodeLogo",
                "argumento": "None"
            }
        ]
        return paths