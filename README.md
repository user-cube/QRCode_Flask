# QRCode - Flask API

A simple Flask API to generate QRCodes.

## Setup
First we need to generate the virtual environment based on:
```requirements.txt
Flask-QRcode
Flask
```
To setup we need to run:
```shell script
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Paths
<table style="width:100%">
      <tr>
          <th>Title</th>
          <th>Description</th>
          <th>Link</th>
          <th>Arguments/th>
      </tr>
        <tr>
            <th>Simple QR Code</th>
            <th>Generate a simple QRCode in png</th>
            <th><a href="/qrcode?data=<data>" target="_blank">/qrcode?data=<data></a></th>
            <th>Data: QR Code information</th>
        </tr>
        <tr>
            <th>Logo QR Code</th>
            <th>Generate a QRCode with logo in png</th>
            <th><a href="/qrcodeLogo?data=<data>&image=<image>" target="_blank">/qrcodeLogo?data=<data>&image=<image></a></th>
            <th>Data: QR Code Information; Image: Image to add to QR Code</th>
        </tr>
</table>
