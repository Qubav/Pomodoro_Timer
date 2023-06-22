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

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    """Function resets timer, resets check marks for each study/work time done and changes label to \"Timer\"."""

    window.after_cancel(timer)
    global reps
    reps = 0
    # setting timer label text to "00:00", deleting all check marks and changing main label text to "Timer"
    canvas.itemconfig(timer_text, text = "00:00")
    check_marks_label.config(text = "")
    highlight_text_label.config(text = "Timer", fg = GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """Function starts timer and based on reps count sets central label text to \"Break\" or \"Work\" with assigned color."""

    global reps
    reps += 1

    # calculating each activity time in seconds
    work_sec = WORK_MIN * 60
    short_brake_sec = SHORT_BREAK_MIN * 60
    long_brake_sec = LONG_BREAK_MIN * 60

    # based on reps count starting counting down for assigned activity time and setting up main label text and its color
    if reps % 8 == 0:
        count_down(long_brake_sec)
        highlight_text_label.config(text = "Brake", fg = RED)
    
    elif reps % 2 == 0:
        count_down(short_brake_sec)
        highlight_text_label.config(text = "Brake", fg = PINK)

    else:
        count_down(work_sec)
        highlight_text_label.config(text = "Work", fg = GREEN)
        work_done_count = math.floor(reps / 2)
        check_marks_text = ""
        
        # updating label with check marks
        for _ in range(work_done_count):
            check_marks_text += "✔"

        check_marks_label.config(text = check_marks_text)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """Function starts """

    # calculating amount of minutes and seconds left
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    # based on amount of seconds left changing count_seconds variable type and value
    if count_seconds < 10:
        # changing count_seconds type to str in order to display number as for example 09, not just 9
        count_seconds = f"0{count_seconds}"

    # setting timer label text
    time_text = f"{count_minutes}:{count_seconds}"
    canvas.itemconfig(timer_text, text = time_text)

    # based on count value either recursive calling itself by function or calling start_timer function
    if count > 0:   
        global timer
        timer  = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
# setting up window
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

# setting up PhotoImage object that is used as background
tomato_img = PhotoImage(file = "tomato.png")

# setting up canvas
canvas = Canvas(width = 220, height = 224, bg = YELLOW, highlightthickness = 0)
canvas.create_image(110, 112, image = tomato_img)
timer_text = canvas.create_text(110, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)

# setting up labels and buttons
check_marks_label = Label(fg = GREEN, bg = YELLOW, font = (FONT_NAME, 20, "bold"), highlightthickness = 0)
check_marks_label.grid(row = 4, column  = 1)

highlight_text_label = Label(text = "Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 35, "normal"), highlightthickness = 0)
highlight_text_label.grid(row = 0, column = 1)

start_button_label = Button(text = "Start", command = start_timer, highlightthickness = 0)
start_button_label.grid(row = 3, column = 0)

reset_button_label = Button(text = "Reset", command = reset_timer, highlightthickness = 0)
reset_button_label.grid(row = 3, column = 2)

window.mainloop()


