# Student ID Card Generator

A small Python desktop application that generates student ID card images from information entered through a Tkinter form.

## Features

- Enter a student's name, age, class, and student ID
- Select and upload a photo
- Generate a 400×250 PNG ID card
- Save the generated card using the student's name

## Technologies

- Python
- Tkinter — desktop interface and file selection
- Pillow — image creation, drawing, resizing, and saving

## How It Works

The application opens a simple form. After the student details and optional photo are provided, the **Generate ID Card** action creates an image containing the supplied information and saves it as a PNG file.

## Requirements

- Python 3
- Pillow

Install Pillow with:

```bash
pip install Pillow
```

Tkinter is included with many standard Python installations. On some systems it may need to be installed separately.

## Run Locally

```bash
python id_card.py
```

The generated ID card is saved in the current working directory using the entered student name as the filename.

## Project Structure

```text
.
└── id_card.py
```

## Author

**Anthony Emmanuella Mmasinachi**

GitHub: [@Scarlet-Twinz](https://github.com/Scarlet-Twinz)
