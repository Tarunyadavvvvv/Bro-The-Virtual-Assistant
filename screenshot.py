import time
import pyautogui
import tkinter as tk


def screenshot():
    name = int(round(time.time()*1000))
    name = f"C:\\Users\\Lenovo\\OneDrive\\Desktop\\Bro-The-Virtual-Assistant-main\\Bro-The-Virtual-Assistant-main\\screenshots_data{name}.png"
    
    img = pyautogui.screenshot(name)
    img.show()


if __name__ == '__main__':
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame,text="Take Screenshot",command=screenshot)

    button.pack(side=tk.LEFT)
    close = tk.Button(frame,text="Quit",command=quit)
    close.pack(side=tk.LEFT)

    root.mainloop()