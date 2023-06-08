import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def convert_tiff_to_png(input_folder, output_folder):
    # Get the list of TIFF files in the input folder
    tiff_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.tiff', '.tif'))]

    for tiff_file in tiff_files:
        try:
            # Open the TIFF image
            input_path = os.path.join(input_folder, tiff_file)
            image = Image.open(input_path)

            # Convert the image to RGBA mode
            image = image.convert("RGBA")

            # Convert the image to PNG format
            output_filename = os.path.splitext(tiff_file)[0] + ".png"
            output_path = os.path.join(output_folder, output_filename)
            image.save(output_path, "PNG")

            print(f"Conversion successful: {tiff_file} --> {output_filename}")
        except Exception as e:
            print(f"Conversion failed: {tiff_file} - {str(e)}")


def select_input_folder():
    # Ask the user to select the input folder
    input_folder = filedialog.askdirectory()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_folder)


def select_output_folder():
    # Ask the user to select the output folder
    output_folder = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_folder)


def convert_button_clicked():
    input_folder = input_entry.get()
    output_folder = output_entry.get()

    if not input_folder or not output_folder:
        result_label.config(text="Please select input and output folders.")
        return

    convert_tiff_to_png(input_folder, output_folder)
    result_label.config(text="Conversion complete.")


# Create the main window
window = tk.Tk()
window.title("TIFF to PNG Converter")

# Create a label for input folder
input_label = tk.Label(window, text="Input Folder:")
input_label.pack()

# Create a label for output folder
output_label = tk.Label(window, text="Output Folder:")
output_label.pack()

# Create a text entry for input folder
input_entry = tk.Entry(window)
input_entry.pack()

# Create a text entry for output folder
output_entry = tk.Entry(window)
output_entry.pack()

# Create a button to select the input folder
select_input_button = tk.Button(window, text="Select Input Folder", command=select_input_folder)
select_input_button.pack()

# Create a button to select the output folder
select_output_button = tk.Button(window, text="Select Output Folder", command=select_output_folder)
select_output_button.pack()

# Create the Convert button
convert_button = tk.Button(window, text="Convert", command=convert_button_clicked)
convert_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()
