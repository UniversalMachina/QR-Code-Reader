import qrcode
import cv2
from pyzbar.pyzbar import decode
import webbrowser
import re

# Generate a QR code
def generate_qr_code(data, output_file):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

# Read a QR code
def read_qr_code(image_path):
    img = cv2.imread(image_path)
    decoded_data = decode(img)

    if decoded_data:
        return decoded_data[0].data.decode('utf-8')
    else:
        return None

def is_url(string):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    return url_pattern.match(string)

# Test the QR code reader
image_path = "QR.png"
decoded_data = read_qr_code(image_path)

if decoded_data:
    print(f"Decoded data: {decoded_data}")

    if is_url(decoded_data):
        print("Opening the link in the web browser...")
        webbrowser.open(decoded_data)
    else:
        print("The decoded data is not a link.")
else:
    print("No QR code detected.")