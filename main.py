from tkinter import *

#Create window - screen
window = Tk()
window.title("Disappearing Text Writing App")
window.configure(padx=10, pady=10, background='gray')
window.geometry("1200x400")

key_counter = 0
seconds = 5
fade = 1.0

def key_pressed(event):
    key = event.char
    # print(key)
    global key_counter, seconds, fade
    key_counter += len(key)
    fade = 1.2
    seconds = 6

    if key_counter == 1:
        fade_timer()
        time_destoyer()

def fade_timer():
    global clock_text
    clock_text = seconds
    canvas.itemconfig(clock, text=clock_text)
    global ws
    ws = window.after(1000, fade_out_time)
    if seconds < 6:
        canvas.itemconfig(clock, fill='red')

    if fade <= 0:
        window.destroy()

def fade_out_time():
    global fade
    window.attributes("-alpha", fade)
    fade -= 0.2
    fade_timer()
    print(f"Opacity: {fade}")

def time_destoyer():
    global clock_text
    clock_text = seconds
    canvas.itemconfig(clock, text=clock_text)
    global ws
    ws = window.after(1000, dec_time)
    if seconds < 6:
        canvas.itemconfig(clock, fill='red')

    if seconds <= 0:
        window.after_cancel(ws)

def dec_time():
    global seconds
    seconds -= 1
    time_destoyer()
    print(f"Sec: {seconds}")


time_left_label = Label(text="Fade Time left: ", background='gray')
time_left_label.pack_forget()

canvas = Canvas(window,height=17,width=20)
canvas.pack_forget()

clock = canvas.create_text(11,11,font=('', 10), fill="black")

#Text/input box for words and sentences.
type_box = Text(height=10, width=60, font=("Arial",20,),bg='light gray')
type_box.pack()
type_box.focus_set()

sample_sentence = "Please continue and do not stop typing for this application. Be productive, use your imagination or write down what are you thinking right now and don't stop!"
type_box.insert(END,sample_sentence)
















window.bind("<KeyPress>", key_pressed)

window.mainloop()