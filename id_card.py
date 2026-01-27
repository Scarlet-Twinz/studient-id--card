import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

photo_path = ""

def upload_photo():
    global photo_path
    photo_path = filedialog.askopenfilename()

def generate_id():
    name = name_entry.get()
    age = age_entry.get()
    student_class = class_entry.get()
    student_id = id_entry.get()

    card = Image.new("RGB", (400, 250), "white")
    draw = ImageDraw.Draw(card)
    font = ImageFont.load_default()

    draw.text((20, 20), "STUDENT ID CARD", fill="black", font=font)
    draw.text((20, 60), "Name: " + name, fill="black", font=font)
    draw.text((20, 90), "Age: " + age, fill="black", font=font)
    draw.text((20, 120), "Class: " + student_class, fill="black", font=font)
    draw.text((20, 150), "ID: " + student_id, fill="black", font=font)

    if photo_path != "":
        photo = Image.open(photo_path)
        photo = photo.resize((100, 120))
        card.paste(photo, (280, 80))

    card.save(name + "_ID.png")

root = tk.Tk()
root.title("Student ID Card Generator")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Class").pack()
class_entry = tk.Entry(root)
class_entry.pack()

tk.Label(root, text="Student ID").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Button(root, text="Upload Photo", command=upload_photo).pack()
tk.Button(root, text="Generate ID Card", command=generate_id).pack()

root.mainloop()