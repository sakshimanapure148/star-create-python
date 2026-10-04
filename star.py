import tkinter as tk

def start_game():
    start_button.destroy()
    label.config(text="Game Started!")

window = tk.Tk()
window.title("My Python Game")
window.geometry("500x400")

label = tk.Label(
    window,
    text="WELCOME",
    font=("Arial", 30, "bold")
)
label.pack(pady=80)

start_button = tk.Button(
    window,
    text="START",
    font=("Arial", 20, "bold"),
    command=start_game
)
start_button.pack()

window.mainloop()