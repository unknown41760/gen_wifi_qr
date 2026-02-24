# gen_wifi_qr

A simple Python tool to generate WiFi QR codes for easy network sharing.

## Features

- Generate QR codes for WiFi networks
- Support for WPA2, WEP, and open networks
- Customizable output filename
- High error correction for reliable scanning

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python generate_wifi_qr.py -s "YourNetwork" -p "YourPassword" -t WPA2 -o wifi_qr.png
```

### Arguments

- `-s, --ssid`: WiFi network name (SSID) [required]
- `-p, --password`: WiFi password [required]
- `-t, --type`: Security type - WPA2, WEP, or nopass [default: WPA2]
- `-o, --output`: Output filename [default: wifi_qr.png]

### Examples

**WPA2 Network (default):**
```bash
python generate_wifi_qr.py -s "MyHomeWiFi" -p "secret123"
```

**WEP Network:**
```bash
python generate_wifi_qr.py -s "OldNetwork" -p "password" -t WEP
```

**Open Network (no password):**
```bash
python generate_wifi_qr.py -s "GuestWiFi" -p "" -t nopass
```

**Custom output filename:**
```bash
python generate_wifi_qr.py -s "MyNetwork" -p "mypass" -o guest_wifi.png
```

## QR Code Format

The generated QR codes follow the standard WiFi QR format:
```
WIFI:S:<SSID>;T:<WPA|WEP|nopass>;P:<password>;;
```

## Dependencies

- Python 3.x
- qrcode[pil]>=7.0

## License

MIT License