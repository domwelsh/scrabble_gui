import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Scrabble Practice")

title = tk.Label(root, text="Welcome to Scrabble Practice!", font=('Arial', 18))
title.pack(padx=20, pady=20)

button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

btn1 = tk.Button(button_frame, text="Mode 1", font=('Arial', 14))
btn1.grid(row=0, column=1, sticky='we')

btn2 = tk.Button(button_frame, text="Mode 2", font=('Arial', 14))
btn2.grid(row=1, column=1, sticky='we')

btn3 = tk.Button(button_frame, text="Mode 3", font=('Arial', 14))
btn3.grid(row=2, column=1, sticky='we')

btn_q = tk.Button(button_frame, text="Quit", font=('Arial', 14))
btn_q.grid(row=3, column=1, sticky='we')

button_frame.pack(fill='x', pady=50)

root.mainloop()
