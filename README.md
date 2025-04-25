# Quick QR

A 5-star, user-friendly QR Code Generator GUI application for Windows.

## Features
- Enter any text or URL
- Instant QR code preview
- Save QR code directly to Downloads folder
- No Python installation required
- Branded icon `icon.ico`

## Installation
1. Download `qr_gui.exe` from the [Releases](https://github.com/C0DER-B0T/qr-generator/releases/latest).
2. Place `qr_gui.exe` anywhere on your system.
3. Double-click to run.

## Usage
1. Launch the app.
2. Enter your text or URL in the input field.
3. Click **Generate QR** to preview.
4. Click **Save QR** to save the image in your Downloads folder.

## Files
- `qr_gui.py`: Source code for the GUI app.
- `icon.ico`: Application icon.
- `qr_gui.exe`: Standalone Windows executable.

## Building from Source
```bash
pip install qrcode[pil] pillow pyinstaller
pyinstaller --onefile --windowed --icon=icon.ico qr_gui.py
