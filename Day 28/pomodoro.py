from tkinter import *


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
def reset_timer():
    global cancel_id
    if cancel_id is not None:
        window.after_cancel(cancel_id)
        cancel_id = None
        buttons[0].config(state="active")
        canvas.itemconfig(timer_text, text="00:00")
        check_mark_label_var.set("")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    if True:
        buttons[0].config(state="disabled")
        print("bru")
    timer_label_var.set("Work")
    count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count, break_time=False):
    global WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN
    global cancel_id

    # Make timer looks nice
    time_str = f"{(count // 60):02}:{(count % 60):02}"
    canvas.itemconfig(timer_text, text=time_str)

    # Check condition
    if count > 0:
        cancel_id = window.after(1000, count_down, count - 1, break_time)
    # End of working session, break_time start soon
    elif count == 0 and not break_time:
        current = check_mark_label_var.get()
        check_mark_label_var.set(current + "✓")
        if current == "✓✓✓":  # 4th time but since current haven't updated itself.
            timer_label_var.set("Long Break")
            count_down(LONG_BREAK_MIN * 60, break_time=True)
        else:  # not 4th time
            timer_label_var.set("Break")
            count_down(SHORT_BREAK_MIN * 60, break_time=True)
    # End of break_time, going to start working session
    elif count == 0 and break_time:
        current = check_mark_label_var.get()
        if current == "✓✓✓✓":  # 4th time, going to reset check mark label
            check_mark_label_var.set("")
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


# Button
cancel_id = None
start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset", command=reset_timer)

# Create button widgets collections and save the two button
buttons = [start_button, reset_button]

start_button.grid(column=1, row=3)
reset_button.grid(column=3, row=3)
window.mainloop()
