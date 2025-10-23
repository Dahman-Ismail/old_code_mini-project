# QR Code Generator & Decoder

A modern, user-friendly desktop application for generating and decoding QR codes with customization options.

<!-- ![Application Screenshot](screenshot.png) -->

## Features

### QR Code Generation
- 📝 Generate QR codes from any text or URL
- 🎨 Customize foreground and background colors
- 📏 Adjustable scale/size settings
- 💾 Save QR codes as PNG images
- 🖼️ Real-time preview

### QR Code Decoding
- 🔍 Decode QR codes from image files (PNG, JPG, JPEG)
- 📊 Display detailed information including:
  - Content/data
  - QR code type
  - Bounding box coordinates
  - Polygon points
  - File path

<!-- ## Screenshots

### Generate QR Tab
![Generate QR Screenshot](https://via.placeholder.com/800x600/1a1a2e/eee?text=QR+Code+Generator+Tab)
*Generate custom QR codes with color customization and preview*

### Decode QR Tab
![Decode QR Screenshot](https://via.placeholder.com/800x600/1a1a2e/eee?text=QR+Code+Decoder+Tab)
*Decode QR codes and view detailed information* -->

## Requirements

### Python Version
- Python 3.7 or higher

### Dependencies
Install all required packages using pip:

```bash
pip install pyqrcode pypng pyzbar pillow customtkinter
```

#### Package Breakdown:
- `pyqrcode` - QR code generation
- `pypng` - PNG image support for pyqrcode
- `pyzbar` - QR code decoding
- `pillow` - Image processing
- `customtkinter` - Modern UI framework

### Additional Requirements for pyzbar

**Windows Users:**
The application requires the `libzbar` library for QR code decoding. The code includes Windows-specific configuration:

<!-- ```python
os.add_dll_directory(r"C:\Users\Sanae\Desktop\tesssst\python")
cdll.LoadLibrary(r"C:\Users\Sanae\Desktop\tesssst\python\libzbar-64.dll")
``` -->

**⚠️ Important:** You need to:
1. Download `libzbar-64.dll` from the [pyzbar releases](https://github.com/NaturalHistoryMuseum/pyzbar/)
2. Update the paths in lines 4-5 of `qr_code_v2.py` to match your DLL location
3. Or place the DLL in your Python directory and update the path accordingly

**Linux/Mac Users:**
Install zbar using your package manager:
- **Linux:** `sudo apt-get install libzbar0` (Ubuntu/Debian) or `sudo yum install zbar` (Fedora/RHEL)
- **Mac:** `brew install zbar`

Then remove or comment out lines 1-5 in the code.

## Installation

1. Clone or download this repository
2. Install Python dependencies:
   ```bash
   pip install pyqrcode pypng pyzbar pillow customtkinter
   ```
3. (Windows only) Download and configure `libzbar-64.dll` as described above
4. Run the application:
   ```bash
   python qr_code_v2.py
   ```

## Usage

### Generating a QR Code

1. Navigate to the **"Generate QR"** tab
2. Enter your text or URL in the text box
3. (Optional) Customize colors:
   - Click **"Pick Foreground Color"** to change the QR code color
   - Click **"Pick Background Color"** to change the background color
4. (Optional) Adjust the scale (default: 8)
5. Click **"Generate QR Code"** to preview
6. Click **"Save QR Code"** to save the image to your desired location

### Decoding a QR Code

1. Navigate to the **"Decode QR"** tab
2. Click **"Open QR Image"**
3. Select a QR code image file (PNG, JPG, or JPEG)
4. View the decoded information in the text area

## Configuration

### Appearance Mode
The application supports three appearance modes:
- **System** (default) - Follows system theme
- **Dark** - Dark mode
- **Light** - Light mode

To change, modify line 25 in the code:
```python
ctk.set_appearance_mode("Dark")  # or "Light", "System"
```

### Color Theme
Change the accent color by modifying line 26:
```python
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"
```

## File Structure

```
project/
├── qr_code_v2.py          # Main application file
├── README.md               # This file
├── screenshot.png          # Application screenshot
└── temp_qr.png            # Temporary QR code file (generated at runtime)
```

## Troubleshooting

### "Cannot find libzbar" error
- Ensure `libzbar-64.dll` is in the correct location
- Update the path in lines 4-5 of the code
- On Linux/Mac, install zbar using your package manager

### "No QR code detected" error
- Ensure the image contains a valid QR code
- Try a higher quality image
- Check that the QR code is not damaged or obscured

### Colors not applying
- Ensure you click "Generate QR Code" after selecting colors
- Some color combinations may have low contrast

## License

This project is open source and available for personal and educational use.

## Contributing

Contributions, issues, and feature requests are welcome!

## Author

Created with ❤️ using Python and CustomTkinter

---

**Note:** Remember to update the DLL paths in the code to match your system configuration before running the application.