# created based on instructions by 100 days of python course
from tkinter import Tk, Button, Label, Entry, Canvas, PhotoImage
import time


#### Define constants

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#194d26"
YELLOW = "#ddd46e"
WHITE = "#ffffff"
FONT_NAME = "Helvetica"

#defrine time intervals in minutes

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
speed = 1000 # refresh interval. 1000 = 1 sec. a lower number runs the script faster for debug/test
reps = 0
checkmark_text = ""
timer = None
paused = False # to track when the timer is paused

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        # if reps is odd, is a working period
        countdown(work_sec)
        title.config(text="Work", fg=RED)

    elif reps % 8 == 0:
        # if reps % 8 = 0 means 4 working periods have been completed and now a long rest is awarded
        countdown(long_break_sec)
        title.config(text="Long Break", fg=PINK)
    else:
        # reps is even, means there is a short break
        countdown(break_sec)
        title.config(text="Break", fg=GREEN)

### COUNTDOWN


def countdown(count):
    global checkmark_text, speed
    # global reps
    minutes = int(count/60)  # another option is using math.floor (import math)
    seconds = count % 60
    if seconds < 10:
        timertext.config(text=f"{minutes}:0{seconds}")
    else:
        #to prevent the time label to bewcome too short when there are less than 10 sec left in the minute
        timertext.config(text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(speed, countdown, count-1)
    else:
        # Timer has reached 0, start the next timer
        start_timer()

        # Update checkmark display for completed work intervals
        if reps % 2 == 0:
            if reps < 10:
                checkmark_text += "✓"
            else: #prevent the screen becoming too wide after too many ✓'s
                checkmark_text = f"{reps//2}x ✓"
            checkmark.config(text=checkmark_text)
# ---------------------------- TIMER RESET ------------------------------- #
# def toggle_pause():
#     global paused, speed
#     # paused = not paused
#     if not paused:
#         paused = True
#         pause_button.config(text="Resume")
#         speed = 0
#     else:
#         pause_button.config(text="Pause")
#         paused = False
#         # start_timer()
#         speed = 1000 # restores counter speed

#to reset the timer
def reset_timer():
    global checkmark_text, reps
    window.after_cancel(timer)
    timertext.config(text=f"25:00")
    checkmark_text = ""
    checkmark.config(text=checkmark_text)
    title.config(text="Timer", fg=GREEN)
    reps = 0

### UI

window = Tk()
window.title("Pomodoro")
window.config(width=400, height=400, padx=100, pady=50, bg=WHITE)

canvas = Canvas(width=206, height=224, bg=WHITE, highlightthickness=0)
# Create and place the title label
title = Label(text="My Pomodoro Timer ⏰", font=(FONT_NAME, 30), fg=GREEN, bg=WHITE)
title.grid(column=1, row=0)

#create tomato image (Created by wall-e)
tomato = PhotoImage(file="Pomodoro/pomodoro.png")
#image is too big, so it needs to be resized
img_width = 200  # Set your desired width
img_height = 200  # Set your desired height
resized_image = tomato.subsample(tomato.width() // img_width, tomato.height() // img_height)

# places the timer label and tomato image
timertext = Label(text=f"{WORK_MIN}:00", fg=GREEN, bg=WHITE,
                               font=(FONT_NAME, 35, "bold"))
timertext.grid(column=1, row=1)
canvas.create_image(102, 112, image=resized_image)
canvas.grid(column=1, row=2)


#buttons to start and reset the timer
button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=3)
# pause_button = Button(text="Pause", command=toggle_pause, highlightthickness=0)
# pause_button.grid(column=1, row=3)
button_reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
button_reset.grid(column=2, row=3)

#label to display checkmarks (completed pomodoros)
checkmark = Label(text=checkmark_text, font=(
    FONT_NAME, 20), fg=GREEN, bg=WHITE)
checkmark.grid(column=1, row=4)

#runs the Tkinter event loop
window.mainloop()

# TODO when pressing start, the window width reduces
# TODO implement a pause button
