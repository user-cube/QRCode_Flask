# coding=utf-8
from flask import Flask, render_template, request, send_file
from flask_qrcode import QRcode
import home

app = Flask(__name__)
qrcode = QRcode(app)

@app.route("/")
@app.route('/home')
def index():
    paths = home.Home.home()
    return render_template("qrcode.html", paths=paths)


@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    data = request.args.get("data", "")
    return send_file(qrcode(data, mode="raw", box_size=100, error_correction='H'), mimetype="image/png")

@app.route("/qrcodeLogo", methods=["GET"])
def get_qrcodeImage():
    data = request.args.get("data", "")
    image = request.args.get("image", "")
    return send_file(qrcode(data, mode="raw", box_size=100, error_correction='H', icon_img=image), mimetype="image/png")

if __name__ == "__main__":
    app.run()