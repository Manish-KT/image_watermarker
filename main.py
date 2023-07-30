from tkinter import ttk, messagebox, Canvas, Label, Button, filedialog
import tkinter as tk
import time
from PIL import Image, ImageDraw, ImageFont

BACKGROUND_COLOR = "#B1DDC6"


# _______________________________FUNCTIONS_________________________________ #
def choose_file():
    return filedialog.askopenfilename(initialdir="/", title="Select a Image File",
                                      filetypes=(("jpg files", "*.jpg"), ("png files", "*.png")))


def get_text():
    return entry.get()


def watermarker(path, watermark="© KT"):
    bg = Image.open(path)
    width, height = bg.size
    draw = ImageDraw.Draw(bg)
    font = ImageFont.truetype("arial.ttf", 100)

    watermark_image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    watermark_draw = ImageDraw.Draw(watermark_image)

    textbox = draw.textbbox((2, 2), watermark, font=font)
    textwidth = textbox[2] - textbox[0]
    textheight = textbox[3] - textbox[1]

    margin = 50
    x = width - textwidth - margin
    y = height - textheight - margin

    watermark_draw.text((x, y), watermark, font=font, fill=(255, 255, 255, 128))
    blended_image = Image.alpha_composite(bg.convert("RGBA"), watermark_image)
    blended_image.save(f"C:\\Users\\Lenovo\\Desktop\\{path.split('/')[-1]}_watermarked.png")
    messagebox.showinfo(title="Watermark added", message="Watermark added to desktop successfully!")


# __________________SCREEN 1_______________________#


# _________UI SETUP________ #
window = tk.Tk()
window.geometry("400x600")
window.title("KT's Water-Marker App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=400, height=600, highlightthickness=0, bg=BACKGROUND_COLOR)

# Create a ttk Style and configure the button style
style = ttk.Style()
style.configure("TButton", font=("Arial", 15, "bold"), foreground="#FFFFFF", background="#4CAF50", padding=10)

# label
label1 = Label(text="loading KT's \nwatermarker...", font=("Ariel", 20, "bold"), bg=BACKGROUND_COLOR)
label1.pack(pady=150)

# Progress Bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(window, variable=progress_var, maximum=100)
progress_bar.pack(pady=50)

# Simulate loading and updating progress bar
for i in range(101):
    progress_var.set(i)
    window.update()
    time.sleep(0.03)

# __________________SCREEN 2_______________________#

label1.destroy()
progress_bar.destroy()

# Place label2 using grid and center it
footer = Label(text="made by: KT", font=("Ariel", 10, "italic"), bg=BACKGROUND_COLOR)

label2 = Label(text="Select image", font=("Ariel", 20, "bold"), bg=BACKGROUND_COLOR)
label2.grid(row=0, column=0, columnspan=3, pady=20)

# Create the Entry widget and position it to the right
entry = tk.Entry(window, width=10, font=("Arial", 12))
entry.grid(row=2, column=0, padx=20, sticky="e")

# Add watermark button and position it at the center
done = tk.Button(window, text="Add Watermark", command=lambda: watermarker(choose_file(), get_text()))
done.grid(row=3, column=0, columnspan=3, pady=20)

# Start the main event loop
window.mainloop()
