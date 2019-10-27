from flask import Flask, render_template, request, send_file
from flask_qrcode import QRcode
import home

app = Flask(__name__)
qrcode = QRcode(app)
paths = home.Home.home(app)

@app.route("/")
@app.route('/home')
def index():
    return render_template("home.html", paths=paths)

@app.route('/qrcode')
def qrcodeGenerator():
    return render_template("qrcode.html")

@app.route('/qrcodeLogo')
def qrcodeLogo():
    return render_template("qrcodeLogo.html")

@app.route("/genqrcode", methods=["GET"])
def get_qrcode():
    data = request.args.get("data", "")
    return send_file(qrcode(data, mode="raw", box_size=100, error_correction='H'), mimetype="image/png")

@app.route("/genqrcodeLogo", methods=["GET"])
def get_qrcodeImage():
    data = request.args.get("data", "")
    image = request.args.get("image", "")
    return send_file(qrcode(data, mode="raw", box_size=100, error_correction='H', icon_img=image), mimetype="image/png")

if __name__ == "__main__":
    app.run()