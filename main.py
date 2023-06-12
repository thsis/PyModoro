import time
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from playsound import playsound

IMG_SIZE = (150, 150)
SECONDS_PER_MINUTE = 60
INIT_POMODORO_SECONDS = 25 * SECONDS_PER_MINUTE
INIT_BREAK_SECONDS = 5 * SECONDS_PER_MINUTE


def display_seconds(seconds):
    m, s = divmod(seconds, SECONDS_PER_MINUTE)
    return f"{m:02d}:{s:02d}"


def cycle_pomodoro(*args):
    label["image"] = tomato_img_obj
    pomodoro_counter_var.set(INIT_POMODORO_SECONDS)
    break_counter_var.set(INIT_BREAK_SECONDS)

    display_var.set("Pomodoro!")
    countdown(pomodoro_counter_var)

    label["image"] = coffee_img_obj
    display_var.set("Break!")
    countdown(break_counter_var)


def countdown(counter_var):
    seconds = counter_var.get()
    for i in range(seconds, -1, -1):
        counter_var.set(i)
        time_var.set(display_seconds(i))
        time_display.update()
        time.sleep(1)
    playsound("CUCKOOO.WAV")


root = tk.Tk()
root.title("PyModoro")
# expand to fill extra space if window is expanded.
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

style = ttk.Style()
style.theme_use("alt")
style.configure("Colored.TFrame", background="#eba434")
style.configure("Colored.TLabel", background="#eba434", font='Chilanka 24 bold', foreground="#eb3d34")
style.configure("Colored.TButton", background="#eba434", font='Chilanka 12 bold', foreground="#eb3d34")

content = ttk.Frame(root, padding="12 3 12 12", style="Colored.TFrame")
content.grid(row=0, column=0, sticky="news")
content.columnconfigure(0, weight=1)
content.rowconfigure(0, weight=1)


tomato_img_obj = ImageTk.PhotoImage(Image.open("tomato.png").resize(IMG_SIZE))
coffee_img_obj = ImageTk.PhotoImage(Image.open("coffee.png").resize(IMG_SIZE))

# spot for image
label = tk.Label(content, width=IMG_SIZE[1], height=IMG_SIZE[0], background="#eba434")
label.grid(row=0, column=0, rowspan=2, sticky="news")
label["image"] = tomato_img_obj

# display
pomodoro_counter_var = tk.IntVar(value=INIT_POMODORO_SECONDS)
break_counter_var = tk.IntVar(value=INIT_BREAK_SECONDS)
display_var = tk.StringVar(value="Pomodoro!")
time_var = tk.StringVar(value=display_seconds(INIT_POMODORO_SECONDS))

text_display = ttk.Label(content, textvariable=display_var, style="Colored.TLabel", anchor="center")
time_display = ttk.Label(content, textvariable=time_var, style="Colored.TLabel", anchor="center")

text_display.grid(row=0, column=2, columnspan=2, sticky="news")
time_display.grid(row=1, column=2, columnspan=2, sticky="news")

# buttons
play_button = ttk.Button(content, command=cycle_pomodoro, text="Go!", style="Colored.TButton")
play_button.grid(row=2, column=2, sticky="e")

for widget in content.winfo_children():
    widget.grid_configure(padx=5, pady=5)

root.mainloop()
