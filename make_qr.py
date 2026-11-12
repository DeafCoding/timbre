import os
import sys
import qrcode
from dotenv import load_dotenv

load_dotenv()
RING_ID = os.environ["RING_ID"]

if len(sys.argv) < 2:
    print("Usage: python make_qr.py <base_url>")
    sys.exit(1)

base_url = sys.argv[1]
full_url = f"{base_url}/ring/{RING_ID}"

img = qrcode.make(full_url)
img.save("qr.png")
print(f"QR saved for: {full_url}")