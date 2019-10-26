class Home():
    def home():
        paths = [
            {
                "titulo": "Simple QR Code",
                "definicao": "Generate a simple QRCode in png",
                "link": "/qrcode?data=<data>",
                "argumento": "Data: QR Code information"
            },
            {
                "titulo": "Logo QR Code",
                "definicao": "Generate a QRCode with logo in png",
                "link": "/qrcodeLogo?data=<data>&image=<image>",
                "argumento": "Data: QR Code Information; Image: Image to add to QR Code"
            }
        ]
        return paths