from tkinter import *
import time


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
ELECTRIC_GREEN = "#00ff00"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 1
CHECK_MARK = "✓"


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    timer_label_var.set("Work")
    count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count, break_time=False):
    global WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN

    # Make timer looks nice
    time_str = f"{(count // 60):02}:{(count % 60):02}"
    canvas.itemconfig(timer_text, text=time_str)

    # Check condition
    if count > 0:
        window.after(1000, count_down, count - 1, break_time)
    elif count == 0 and not break_time:
        current = check_mark_label_var.get()
        check_mark_label_var.set(current + "✓")
        if current == "✓✓✓":
            timer_label_var.set("Long Break")
            count_down(LONG_BREAK_MIN * 60, break_time=True)
            check_mark_label_var.set("")
        else:
            timer_label_var.set("Break")
            count_down(SHORT_BREAK_MIN * 60, break_time=True)
    elif count == 0 and break_time:
        timer_label_var.set("Work")
        count_down(WORK_MIN * 60, break_time=False)



# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 127, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


# Label
timer_label_var = StringVar()
timer_label_var.set("Timer")
timer_label = Label(textvariable=timer_label_var, fg=GREEN, font=(FONT_NAME, 39, "bold"), bg=YELLOW)
timer_label.grid(column=2, row=1)
# --------- StrVar ------- #
check_mark_label_var = StringVar()
check_mark_label_var.set("")
check_mark_label = Label(textvariable=check_mark_label_var, fg=ELECTRIC_GREEN, bg=YELLOW)
check_mark_label.grid(column=2, row=4)


def clicked_start():
    pass


def clicked_reset():
    pass


# Button
start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset", command=clicked_reset)
start_button.grid(column=1, row=3)
reset_button.grid(column=3, row=3)
window.mainloop()
