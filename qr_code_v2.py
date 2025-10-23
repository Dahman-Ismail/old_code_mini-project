import sys
import os
<<<<<<< HEAD
from pathlib import Path

# Try to load libzbar for Windows
if sys.platform == "win32":
    try:
        from ctypes import cdll
        # Try common locations for libzbar DLL
        possible_paths = [
            Path(__file__).parent / "libzbar-64.dll",
            Path.cwd() / "libzbar-64.dll",
            Path(os.environ.get('PROGRAMFILES', 'C:\\Program Files')) / "zbar" / "bin" / "libzbar-64.dll",
        ]
        
        dll_loaded = False
        for dll_path in possible_paths:
            if dll_path.exists():
                try:
                    os.add_dll_directory(str(dll_path.parent))
                    cdll.LoadLibrary(str(dll_path))
                    dll_loaded = True
                    break
                except:
                    continue
        
        if not dll_loaded:
            print("Warning: libzbar-64.dll not found. QR decoding may not work.")
            print("Please download libzbar-64.dll and place it in the same folder as this script.")
    except Exception as e:
        print(f"Warning: Could not load libzbar: {e}")

# Requirements:
# pip install pyqrcode pypng pyzbar pillow customtkinter
=======
from ctypes import cdll
from pyzbar.pyzbar import decode
>>>>>>> e0f898d0c2aace5a48fbe07aa0e8238b1290dd64
import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox, colorchooser
import pyqrcode
from PIL import Image, ImageTk

# Initialize modern theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class QRApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("QR Code Generator & Decoder")
        self.geometry("800x650")
        self.resizable(False, False)

        # State variables
        self.fg_color = "black"
        self.bg_color = "white"
        self.current_qr_path = None

        # Layout frames
        self.create_widgets()

    def create_widgets(self):
        tabview = ctk.CTkTabview(self, width=780, height=610)
        tabview.pack(padx=10, pady=10)

        gen_tab = tabview.add("Generate QR")
        dec_tab = tabview.add("Decode QR")

        # ---- GENERATOR TAB ----
        ctk.CTkLabel(gen_tab, text="Enter text or URL:", font=("Arial", 14, "bold")).pack(pady=(20, 5))
        self.input_text = ctk.CTkTextbox(gen_tab, width=700, height=120)
        self.input_text.pack(pady=5)

        # QR Customization
        frame = ctk.CTkFrame(gen_tab)
        frame.pack(pady=15)

        ctk.CTkButton(frame, text="Pick Foreground Color", command=self.pick_fg_color, width=180).grid(row=0, column=0, padx=10, pady=5)
        ctk.CTkButton(frame, text="Pick Background Color", command=self.pick_bg_color, width=180).grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(frame, text="Scale:").grid(row=1, column=0, padx=5, sticky="e")
        self.scale_entry = ctk.CTkEntry(frame, width=100)
        self.scale_entry.insert(0, "8")
        self.scale_entry.grid(row=1, column=1, padx=5, sticky="w")

        # Buttons
        button_frame = ctk.CTkFrame(gen_tab)
        button_frame.pack(pady=10)
        
        ctk.CTkButton(button_frame, text="Generate QR Code", command=self.generate_qr, width=200).grid(row=0, column=0, padx=5)
        ctk.CTkButton(button_frame, text="Save QR Code", command=self.save_qr, width=200).grid(row=0, column=1, padx=5)

        # QR Display
        self.qr_display = ctk.CTkLabel(gen_tab, text="QR Code will appear here", font=("Arial", 12))
        self.qr_display.pack(pady=20)

        # ---- DECODER TAB ----
        ctk.CTkLabel(dec_tab, text="Upload QR Code Image to Decode", font=("Arial", 14, "bold")).pack(pady=(20, 10))
        ctk.CTkButton(dec_tab, text="Open QR Image", command=self.decode_qr, width=200).pack(pady=10)
        
        ctk.CTkLabel(dec_tab, text="Decoded Information:", font=("Arial", 12, "bold")).pack(pady=(10, 5))
        self.decode_output = ctk.CTkTextbox(dec_tab, width=700, height=400)
        self.decode_output.pack(pady=10)

    def pick_fg_color(self):
        color = colorchooser.askcolor(title="Choose QR Foreground Color", initialcolor=self.fg_color)
        if color[1]:
            self.fg_color = color[1]
            messagebox.showinfo("Color Selected", f"Foreground color set to: {self.fg_color}")

    def pick_bg_color(self):
        color = colorchooser.askcolor(title="Choose QR Background Color", initialcolor=self.bg_color)
        if color[1]:
            self.bg_color = color[1]
            messagebox.showinfo("Color Selected", f"Background color set to: {self.bg_color}")

    def generate_qr(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Input Missing", "Please enter some text or URL to generate QR code.")
            return

        try:
            scale = int(self.scale_entry.get())
            if scale < 1 or scale > 50:
                messagebox.showwarning("Invalid Scale", "Scale must be between 1 and 50.")
                return
        except ValueError:
            messagebox.showwarning("Invalid Scale", "Please enter a valid number for scale.")
            return

        try:
            # Generate QR code
            qr = pyqrcode.create(text, error='H')
            self.current_qr_path = "temp_qr.png"
            qr.png(self.current_qr_path, scale=scale, module_color=self.fg_color, background=self.bg_color)

            # Display QR code
            img = Image.open(self.current_qr_path)
            # Resize for display (max 300x300)
            img.thumbnail((300, 300), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            self.qr_display.configure(image=img_tk, text="")
            self.qr_display.image = img_tk
            
            messagebox.showinfo("Success", "QR Code generated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate QR code:\n{str(e)}")

    def save_qr(self):
        if not self.current_qr_path or not os.path.exists(self.current_qr_path):
            messagebox.showerror("No QR Code", "Please generate a QR code first before saving.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            initialfile="qr_code.png"
        )
        
        if file_path:
            try:
                # Copy instead of rename to avoid issues
                img = Image.open(self.current_qr_path)
                img.save(file_path)
                messagebox.showinfo("Saved", f"QR code saved successfully to:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save QR code:\n{str(e)}")

    def decode_qr(self):
        file_path = filedialog.askopenfilename(
            title="Select QR Code Image",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif"), ("All files", "*.*")]
        )
        
        if not file_path:
            return

        try:
            from pyzbar.pyzbar import decode
            
            img = Image.open(file_path)
            data = decode(img)
            
            if not data:
                messagebox.showerror("No QR Code Found", "No QR code detected in the selected image.")
                self.decode_output.delete("1.0", tk.END)
                self.decode_output.insert(tk.END, "No QR code found in the image.")
                return

            # Display decoded information
            info = data[0]
            details = f"""╔══════════════════════════════════════════════════════════════╗
                          ║          DECODED QR CODE INFORMATION                         ║
                          ╚══════════════════════════════════════════════════════════════╝

📄 Content:
{info.data.decode('utf-8', errors='replace')}

📋 Type: {info.type}

📍 Bounding Box:
   X: {info.rect.left}
   Y: {info.rect.top}
   Width: {info.rect.width}
   Height: {info.rect.height}

📐 Polygon Points: {info.polygon}

📁 File Path: {file_path}

{'─' * 60}
✓ QR Code decoded successfully!
"""
            self.decode_output.delete("1.0", tk.END)
            self.decode_output.insert(tk.END, details)
            
            messagebox.showinfo("Success", "QR Code decoded successfully!")
            
        except ImportError:
            messagebox.showerror("Error", "pyzbar is not properly installed or libzbar is missing.\n\n"
                               "Please install:\n"
                               "1. pip install pyzbar\n"
                               "2. Download libzbar-64.dll (Windows) or install zbar (Linux/Mac)")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decode QR code:\n{str(e)}")

    def destroy(self):
        # Cleanup temporary file
        if self.current_qr_path and os.path.exists(self.current_qr_path):
            try:
                os.remove(self.current_qr_path)
            except:
                pass
        super().destroy()

if __name__ == "__main__":
    app = QRApp()
    app.mainloop()