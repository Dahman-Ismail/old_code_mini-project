import os
from ctypes import cdll
from pyzbar.pyzbar import decode
import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox, colorchooser
import pyqrcode
# from pyzbar.pyzbar import decode
from PIL import Image, ImageTk
import os

# Initialize modern theme
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")

class QRApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("QR Code Generator & Decoder")
        self.geometry("800x600")
        self.resizable(False, False)

        # State variables
        self.fg_color = "black"
        self.bg_color = "white"

        # Layout frames
        self.create_widgets()

    def create_widgets(self):
        tabview = ctk.CTkTabview(self, width=780, height=560)
        tabview.pack(padx=10, pady=10)

        gen_tab = tabview.add("Generate QR")
        dec_tab = tabview.add("Decode QR")

        # ---- GENERATOR TAB ----
        ctk.CTkLabel(gen_tab, text="Enter text or URL:").pack(pady=(20, 5))
        self.input_text = ctk.CTkTextbox(gen_tab, width=500, height=100)
        self.input_text.pack(pady=5)

        # QR Customization
        frame = ctk.CTkFrame(gen_tab)
        frame.pack(pady=10)

        ctk.CTkButton(frame, text="Pick Foreground Color", command=self.pick_fg_color).grid(row=0, column=0, padx=10)
        ctk.CTkButton(frame, text="Pick Background Color", command=self.pick_bg_color).grid(row=0, column=1, padx=10)

        ctk.CTkLabel(frame, text="Scale:").grid(row=0, column=2, padx=5)
        self.scale_entry = ctk.CTkEntry(frame, width=60)
        self.scale_entry.insert(0, "8")
        self.scale_entry.grid(row=0, column=3)

        ctk.CTkButton(gen_tab, text="Generate QR Code", command=self.generate_qr).pack(pady=15)
        ctk.CTkButton(gen_tab, text="Save QR Code", command=self.save_qr).pack()

        self.qr_display = ctk.CTkLabel(gen_tab, text="")
        self.qr_display.pack(pady=10)

        # ---- DECODER TAB ----
        ctk.CTkButton(dec_tab, text="Open QR Image", command=self.decode_qr).pack(pady=20)
        self.decode_output = ctk.CTkTextbox(dec_tab, width=700, height=300)
        self.decode_output.pack(pady=10)

    def pick_fg_color(self):
        color = colorchooser.askcolor(title="Choose QR Foreground Color")
        if color[1]:
            self.fg_color = color[1]

    def pick_bg_color(self):
        color = colorchooser.askcolor(title="Choose QR Background Color")
        if color[1]:
            self.bg_color = color[1]

    def generate_qr(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Input Missing", "Please enter some text or URL.")
            return

        scale = int(self.scale_entry.get() or 8)
        qr = pyqrcode.create(text, error='H')
        qr.png("temp_qr.png", scale=scale, module_color=self.fg_color, background=self.bg_color)

        img = Image.open("temp_qr.png").resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        self.qr_display.configure(image=img_tk, text="")
        self.qr_display.image = img_tk

    def save_qr(self):
        if not os.path.exists("temp_qr.png"):
            messagebox.showerror("No QR", "Please generate a QR code first.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            os.rename("temp_qr.png", file_path)
            messagebox.showinfo("Saved", f"QR code saved to {file_path}")

    def decode_qr(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if not file_path:
            return

        data = decode(Image.open(file_path))
        if not data:
            messagebox.showerror("Error", "No QR code detected.")
            return

        info = data[0]
        details = f"""
Decoded QR Code Information
----------------------------
Content: {info.data.decode('utf-8')}
Type: {info.type}
Bounding Box: {info.rect}
Polygon Points: {info.polygon}
----------------------------
File Path: {file_path}
"""
        self.decode_output.delete("1.0", tk.END)
        self.decode_output.insert(tk.END, details)

if __name__ == "__main__":
    app = QRApp()
    app.mainloop()
