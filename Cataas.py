from tkinter import *
#from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def set_image():
    #global url
    img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img

def exit():
    window.destroy()

window = Tk()
window.title("Cats!")
window.geometry("600x520")

main_menu = Menu(window)
window.config(menu=main_menu)
file_menu = Menu(main_menu, tearoff = 0)

main_menu.add_cascade(label="Update", menu =file_menu)
file_menu.add_command(label="Загрузить фото", command = set_image)
file_menu.add_separator()
file_menu.add_command(label="Выход", command = exit)


# update_button = Button(text="Обновить", command = set_image)
# update_button.pack()
label = Label()
label.pack()

url = "https://cataas.com/cat"

set_image()


window.mainloop()