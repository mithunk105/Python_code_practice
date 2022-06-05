from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repo = 0
timer = "None"
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    timer_lable.after_cancel(timer)
    timer_lable.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    global repo
    repo = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global repo
    repo += 1
    long_break_min = LONG_BREAK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    work_min = WORK_MIN * 60
    if repo % 8 == 0:
        count_down(long_break_min)
        timer_lable.config(text="Break", fg=RED, bg=YELLOW)
    elif repo % 2 == 0:
        count_down(short_break_min)
        timer_lable.config(text="Break", fg=PINK, bg=YELLOW)
    else:
        count_down(work_min)
        timer_lable.config(text="Work", fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    minutes = int(count / 60)
    if minutes == 0:
        minutes = "00"
    elif minutes < 10:
        minutes = f"0{minutes}"
    seconds = int(count % 60)
    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(repo/2)
        for _ in range(work_session):
            marks += "✔"
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_lable = Label(text="Timer", font=(FONT_NAME, 50, "normal"), fg=GREEN, bg=YELLOW)
timer_lable.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(text="Start", font=(FONT_NAME, 10, "normal"), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "normal"), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark = Label(font=(FONT_NAME, 10, "normal"), fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmark.grid(row=3, column=1)

window.mainloop()
