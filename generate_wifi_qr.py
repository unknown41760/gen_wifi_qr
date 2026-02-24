#!/usr/bin/env python3
"""
Generate WiFi QR codes
Usage: python generate_wifi_qr.py -s "SSID" -p "password" -t WPA -o wifi_qr.png
"""

import argparse

import qrcode
from qrcode.constants import ERROR_CORRECT_H


def create_wifi_qr(
    ssid: str, password: str, security: str = "WPA2", filename: str = "wifi_qr.png"
):
    """
    Generate a QR code for WiFi connection.

    Args:
        ssid: WiFi network name
        password: WiFi password
        security: Security type (WPA, WEP, or nopass)
        filename: Output filename for the QR code image
    """
    # WiFi QR code format: WIFI:S:<SSID>;T:<WPA|WEP|nopass>;P:<password>;;
    wifi_data = f"WIFI:S:{ssid};T:{security};P:{password};;"

    # Create QR code instance
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Add data
    qr.add_data(wifi_data)
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(filename)
    print(f"WiFi QR code saved to: {filename}")
    print(f"Network: {ssid}")
    print(f"Security: {security}")


def main():
    parser = argparse.ArgumentParser(description="Generate WiFi QR codes")
    parser.add_argument("-s", "--ssid", required=True, help="WiFi network name (SSID)")
    parser.add_argument("-p", "--password", required=True, help="WiFi password")
    parser.add_argument(
        "-t",
        "--type",
        default="WPA2",
        choices=["WPA2", "WEP", "nopass"],
        help="Security type (default: WPA2)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="wifi_qr.png",
        help="Output filename (default: wifi_qr.png)",
    )

    args = parser.parse_args()

    create_wifi_qr(args.ssid, args.password, args.type, args.output)


if __name__ == "__main__":
    main()
