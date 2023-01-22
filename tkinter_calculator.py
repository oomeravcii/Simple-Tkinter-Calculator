import tkinter as tk

window = tk.Tk()

window.title("Calculator")

window.state("zoomed")
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.minsize(500,400)

text_title = tk.Label(window,text="Calculator+",font="Roboto 40 bold")
text_title.pack(anchor="n")

text_motto = tk.Label(window,text="An advanced way to calculate.",font="Roboto 20 italic")
text_motto.pack(anchor="n")

text_description = tk.Label(window,text="Write your question.",font="Roboto 16")
text_description.place(x=680,y=250)

text_firstvalue = tk.Label(window,text="Enter First Value:",font="Roboto 10 italic")
text_firstvalue.place(x=486,y=370)

text_secondvalue = tk.Label(window,text="Enter Second Value:",font="Roboto 10 italic")
text_secondvalue.place(x=775,y=370)

text_answer = tk.Label(window,text="",font="Roboto 20 bold")
text_answer.place(x=490,y=730)

entry_box1 = tk.Entry(background="black",foreground="white",font="Roboto 17")
entry_box1.place(x=486,y=390,width=275)

entry_box2 = tk.Entry(background="black",foreground="white",font="Roboto 17")
entry_box2.place(x=775,y=390,width=275)

def clear():
    entry_box1.delete(0,"end")
    entry_box2.delete(0,"end")
    text_answer.config(text="")

button_clear = tk.Button(text="Clear",background="black",foreground="white",font="Roboto 10 bold",command=clear)
button_clear.place(x=486,y=770,width=565)

def addition():
    try:
        x = int(entry_box1.get())
        y = int(entry_box2.get())
    except Exception as e:
        text_answer.config(text="Error")
        error_window = tk.Tk()
        error_window.title("Error")
        error_window.state("normal")
        error_window.geometry("500x100+500+200")
        error_window.minsize(500,100)
        text_error = tk.Label(error_window,text="Error: {}".format(e),font="Roboto 10")
        text_error.pack()
        button_exit = tk.Button(error_window,text="Close",fg="white",bg="black",activebackground="red",command=error_window.destroy)
        button_exit.pack(side=tk.BOTTOM,fill=tk.X)
        error_window.mainloop()
    finally:
        text_answer.config(text=x+y)

button_addition = tk.Button(text="+",background="black",foreground="white",font="Roboto 10 bold",command=addition)
button_addition.place(x=486,y=430,width=135)

def subtraction():
    try:
        x = int(entry_box1.get())
        y = int(entry_box2.get())
    except Exception as e:
        text_answer.config(text="Error")
        error_window = tk.Tk()
        error_window.title("Error")
        error_window.state("normal")
        error_window.geometry("500x100+500+200")
        error_window.minsize(500,100)
        text_error = tk.Label(error_window,text="Error: {}".format(e),font="Roboto 10")
        text_error.pack()
        button_exit = tk.Button(error_window,text="Close",fg="white",bg="black",activebackground="red",command=error_window.destroy)
        button_exit.pack(side=tk.BOTTOM,fill=tk.X)
        error_window.mainloop()
    finally:
        text_answer.config(text=x-y)

button_subtraction = tk.Button(text="-",background="black",foreground="white",font="Roboto 10 bold",command=subtraction)
button_subtraction.place(x=625,y=430,width=135)

def multiplication():
    try:
        x = int(entry_box1.get())
        y = int(entry_box2.get())
    except Exception as e:
        text_answer.config(text="Error")
        error_window = tk.Tk()
        error_window.title("Error")
        error_window.state("normal")
        error_window.geometry("500x100+500+200")
        error_window.minsize(500,100)
        text_error = tk.Label(error_window,text="Error: {}".format(e),font="Roboto 10")
        text_error.pack()
        button_exit = tk.Button(error_window,text="Close",fg="white",bg="black",activebackground="red",command=error_window.destroy)
        button_exit.pack(side=tk.BOTTOM,fill=tk.X)
        error_window.mainloop()
    finally:
        text_answer.config(text=x*y)

button_multiplication = tk.Button(text="x",foreground="white",background="black",font="Roboto 10 bold",command=multiplication)
button_multiplication.place(x=775,y=430,width=135)

def division():
    try:
        x = int(entry_box1.get())
        y = int(entry_box2.get())
    except Exception as e:
        text_answer.config(text="Error")
        error_window = tk.Tk()
        error_window.title("Error")
        error_window.state("normal")
        error_window.geometry("500x100+500+200")
        error_window.minsize(500,100)
        text_error = tk.Label(error_window,text="Error: {}".format(e),font="Roboto 10")
        text_error.pack()
        button_exit = tk.Button(error_window,text="Close",fg="white",bg="black",activebackground="red",command=error_window.destroy)
        button_exit.pack(side=tk.BOTTOM,fill=tk.X)
        error_window.mainloop()
    finally:
        text_answer.config(text=x/y)

button_division = tk.Button(text="/",background="black",foreground="white",font="Roboto 10 bold",command=division)
button_division.place(x=915,y=430,width=135)



window.mainloop()