from PIL import Image, ImageChops, ImageEnhance
import numpy as np 
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox

def show_text(text): #gui for extracted text output
    root = tk.Tk()
    root.title("Extracted Text")

    text_area= scrolledtext.ScrolledText(root, wrap=tk.WORD, width = 50, height= 20)
    text_area.insert(tk.INSERT, text)
    text_area.config(state='disabled')
    text_area.pack(padx=10, pady=10)

    close_button = tk.Button(root, text='Close', command=root.destroy)
    close_button.pack(pady=5)

    root.mainloop()

def hideFileInImage(imagePath, text, output_stream):

    #read image as array
    img = Image.open(imagePath)
    data = np.array(img)

    #read file

    #convert file text to binary
    binaryData = ''.join([format(ord(i),'08b') for i in text]) + '00000000'

    #check if file size is bigger than image
    if len(binaryData) > (data.size):
        raise ValueError("File is too large to input in image.")
    
    #flatten image array to 1D 
    flatData = data.flatten()

    #Change LSB of each pixel
    for i in range(len(binaryData)):
        #clear lsb (2^0) of pixel and then set to binary value of text
        flatData[i] = (flatData[i] & 0xFE) | int(binaryData[i])

    #reshape back to original shape
    newData = flatData.reshape(data.shape)

    newImage = Image.fromarray(newData.astype('uint8'))
    newImage.save(output_stream, format='PNG')

def extractFileFromImage(stegImage, userLength):

    img = Image.open(stegImage)
    data = np.array(img)

    #flatten data to 1D array
    flatData = data.flatten()

    #take lsb from each pixel
    binaryData = [str(flatData[i] & 1) for i in range(userLength * 8)]

    #convert binary to bytes (pixel values)
    byteData = bytearray()
    for i in range(0, len(binaryData), 8):
        byteData.append(int("".join(binaryData[i:i+8]), 2))

    return(byteData.decode(errors='ignore')) 

def enhanceDifferenceInImage(originalImage, hiddenImage, differencePath):
    #use to see the changes being made to the image

    original = Image.open(originalImage).convert('RGB')
    modified = Image.open(hiddenImage).convert('RGB')

    difference = ImageChops.difference(original, modified)

    enhanced_diff = ImageEnhance.Brightness(difference).enhance(scale_factor=10)

    enhanced_diff.save(differencePath)
    enhanced_diff.show()
    print(f"Enhanced difference image saved as: {differencePath}")


def hide_text():
    #tkinter gui
    image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not image_path:
        return
    file_path = filedialog.askopenfilename(title="Select Text File", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return
    output_image_path = filedialog.asksaveasfilename(title="Save Output Image", defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if not output_image_path:
        return
    try:
        hideFileInImage(image_path, file_path, output_image_path)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def extract_text():
    #tkinter gui
    stego_image_path = filedialog.askopenfilename(title="Select Secret Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not stego_image_path:
        return
    try:
        extractFileFromImage(stego_image_path)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    root.title("Steganography Tool")
    root.geometry("300x200")

    hide_button = tk.Button(root, text="Hide Text in Image", command=hide_text)
    hide_button.pack(pady=20)

    extract_button = tk.Button(root, text="Extract Text from Image", command=extract_text)
    extract_button.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()