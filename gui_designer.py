# gui designer by @Fnerz.-
# Guthub: https://github.com/Fnerz

# Yout open to use the code but would be nice to keep the first line and add your name if you want

import tkinter as tk
from tkinter import filedialog
import colorama

colorama.init(autoreset=True)

"""
 up comming features
  -Draging 

"""

print(" strg + x         :   place Label")
print(" strg + e         :   place Entry(Textbox)")
print(" strg + b         :   place Button")
print(" strg + p         :   place Progressbar")
print(" strg + l         :   place listbox")
print(" strg + s         :   Show code")


window_x = input("Width: ")
window_y = input("Height: ")
window_title = input("Title: ")

code = ["\nimport tkinter as tk\n", "window = tk.Tk()\n\n", f"window.geometry(f'{window_x}x{window_y}')\n", f"window.title('{window_title}')\n\n"]


buttons = 0
labels = 0
entrys = 0
listboxs = 0

def safe(e):
    # # asking for path
    # path = filedialog.asksaveasfile()
    
    # if path:
    #     with open(path, "w") as f:
    final_code = ""

    for i in range(len(code)):
        final_code += code[i]
    
    final_code += "\nwindow.mainloop()"

    print(colorama.Fore.GREEN + final_code)

            # f.write(str(final_code))
            

# all the functions wich places the widget
def place_button(e):
    buttons + 1

    mybutton = tk.Button(window , text="Button")
    mybutton.place(x = e.x, y = e.y)
    ThisCode = f'mybutton{buttons} = tk.Button(window , text="Button")\nmybutton{buttons}.place(x = {e.x}, y = {e.y})\n\n'
    code.append(ThisCode)


def place_label(e):
    labels + 1

    myLabel = tk.Label(window, text="Label")
    myLabel.place(x = e.x, y = e.y)
    ThisCode = myLabel = f"myLabel{labels} =  tk.Label(window, text='Label')\nmyLabel{labels}.place(x = {e.x}, y = {e.y})\n\n"
    code.append(ThisCode)
    

def place_entry(e):
    entrys + 1

    myEntry = tk.Entry(window)
    myEntry.place(x = e.x, y = e.y)
    ThisCode = myEntry = f"myEntry{entrys} = tk.Entry(window)\nmyEntry{entrys}.place(x = {e.x}, y = {e.y})\n\n"
    code.append(ThisCode)


def place_progress(e):
    pass

def place_listbox(e):
    listboxs + 1

    myBox = tk.Listbox()
    myBox.place(x = e.x, y = e.y)
    ThisCode = f"myBox = tk.Listbox{listboxs}()\nmyBox{listboxs}.place(x = {e.x}, y = {e.y})\n\n"
    code.append(ThisCode)

# innitializing window
window = tk.Tk()
window.geometry(f'{window_x}x{window_y}')
window.title(window_title)


# binding the functions
window.bind("<Control-x>", place_label)
window.bind("<Control-e>", place_entry)
window.bind("<Control-b>", place_button)
window.bind("<Control-p>", place_progress)
window.bind("<Control-l>", place_listbox)
window.bind("<Control-s>", safe)

window.mainloop()