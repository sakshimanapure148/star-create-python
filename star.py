import tkinter as tk
import random

# ==================================================
#                  GAME SETTINGS
# ==================================================

WIDTH = 700
HEIGHT = 500
GAME_TIME = 30

score = 0
time_left = GAME_TIME
game_running = False
target = None


# ==================================================
#                  MAIN WINDOW
# ==================================================

root = tk.Tk()
root.title("Catch the Circle Game")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)


# ==================================================
#                  START SCREEN
# ==================================================

start_frame = tk.Frame(root, width=WIDTH, height=HEIGHT)
start_frame.pack(fill="both", expand=True)

title = tk.Label(
    start_frame,
    text="CATCH THE CIRCLE",
    font=("Arial", 32, "bold")
)
title.pack(pady=80)

instruction = tk.Label(
    start_frame,
    text="Click the circle as many times as you can!",
    font=("Arial", 16)
)
instruction.pack(pady=10)


# ==================================================
#                  GAME SCREEN
# ==================================================

game_frame = tk.Frame(root, width=WIDTH, height=HEIGHT)

top_frame = tk.Frame(game_frame)
top_frame.pack(fill="x", padx=20, pady=10)

score_label = tk.Label(
    top_frame,
    text="Score: 0",
    font=("Arial", 18, "bold")
)
score_label.pack(side="left")

timer_label = tk.Label(
    top_frame,
    text="Time: 30",
    font=("Arial", 18, "bold")
)
timer_label.pack(side="right")


canvas = tk.Canvas(
    game_frame,
    width=WIDTH - 40,
    height=HEIGHT - 80,
    highlightthickness=0
)
canvas.pack()


# ==================================================
#                  GAME OVER SCREEN
# ==================================================

game_over_frame = tk.Frame(root, width=WIDTH, height=HEIGHT)

game_over_title = tk.Label(
    game_over_frame,
    text="GAME OVER",
    font=("Arial", 35, "bold")
)
game_over_title.pack(pady=80)

final_score_label = tk.Label(
    game_over_frame,
    text="Your Score: 0",
    font=("Arial", 22)
)
final_score_label.pack(pady=20)


# ==================================================
#                  CREATE TARGET
# ==================================================

def create_target():
    global target

    canvas.delete("target")

    x = random.randint(40, WIDTH - 80)
    y = random.randint(40, HEIGHT - 130)

    size = 40

    target = canvas.create_oval(
        x,
        y,
        x + size,
        y + size,
        fill="red",
        outline="black",
        width=2,
        tags="target"
    )


# ==================================================
#                  TARGET CLICK
# ==================================================

def catch_target(event):
    global score

    if not game_running:
        return

    items = canvas.find_withtag("target")

    if items:
        coords = canvas.coords(items[0])

        x1, y1, x2, y2 = coords

        if x1 <= event.x <= x2 and y1 <= event.y <= y2:
            score += 1

            score_label.config(
                text=f"Score: {score}"
            )

            create_target()


# ==================================================
#                  START GAME
# ==================================================

def start_game():
    global score
    global time_left
    global game_running

    score = 0
    time_left = GAME_TIME
    game_running = True

    start_frame.pack_forget()
    game_over_frame.pack_forget()

    game_frame.pack(
        fill="both",
        expand=True
    )

    score_label.config(
        text="Score: 0"
    )

    timer_label.config(
        text=f"Time: {GAME_TIME}"
    )

    create_target()

    countdown()


# ==================================================
#                  COUNTDOWN
# ==================================================

def countdown():
    global time_left
    global game_running

    if not game_running:
        return

    if time_left > 0:

        timer_label.config(
            text=f"Time: {time_left}"
        )

        time_left -= 1

        root.after(
            1000,
            countdown
        )

    else:
        end_game()


# ==================================================
#                  END GAME
# ==================================================

def end_game():
    global game_running

    game_running = False

    canvas.delete("all")

    game_frame.pack_forget()

    game_over_frame.pack(
        fill="both",
        expand=True
    )

    final_score_label.config(
        text=f"Your Score: {score}"
    )


# ==================================================
#                  RESTART GAME
# ==================================================

def restart_game():
    game_over_frame.pack_forget()

    start_frame.pack(
        fill="both",
        expand=True
    )


# ==================================================
#                  BUTTONS
# ==================================================

start_button = tk.Button(
    start_frame,
    text="START",
    font=("Arial", 20, "bold"),
    width=12,
    command=start_game
)

start_button.pack(pady=40)


restart_button = tk.Button(
    game_over_frame,
    text="PLAY AGAIN",
    font=("Arial", 18, "bold"),
    width=12,
    command=restart_game
)

restart_button.pack(pady=30)


exit_button = tk.Button(
    game_over_frame,
    text="EXIT",
    font=("Arial", 16),
    width=10,
    command=root.destroy
)

exit_button.pack()


# ==================================================
#                  MOUSE CONTROL
# ==================================================

canvas.bind(
    "<Button-1>",
    catch_target
)


# ==================================================
#                  START PROGRAM
# ==================================================

root.mainloop()