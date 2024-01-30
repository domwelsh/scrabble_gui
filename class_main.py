import tkinter as tk
from tkinter import ttk
import functions


class Windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Scrabble Practice")

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=500, width=500)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (MainPage, Mode1, Mode2, Mode3):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        for i in range(3):
            self.columnconfigure(i, weight=1)
        title = tk.Label(self, text="Welcome to Scrabble Practice!", font=('Arial', 18))
        title.grid(row=0, column=1, padx=10, pady=10)

        explanation_text = tk.Label(
            self,
            text="Pick one of three modes to practice!\n"
                 "Mode 1 - Show all longest words from 7 random letters\n"
                 "Mode 2 - Enter your guess for the longest word from 7 random letters\n"
                 "Mode 3 - Enter your guess for the highest scoring word",
            bg='grey'
        )
        explanation_text.grid(row=1, column=1, pady=20)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        mode_1_button = tk.Button(
            self,
            text="Mode 1",
            command=lambda: controller.show_frame(Mode1)
        )
        mode_1_button.grid(row=2, column=1)

        mode_2_button = tk.Button(
            self,
            text="Mode 2",
            command=lambda: controller.show_frame(Mode2)
        )
        mode_2_button.grid(row=3, column=1)

        mode_3_button = tk.Button(
            self,
            text="Mode 3",
            command=lambda: controller.show_frame(Mode3)
        )
        mode_3_button.grid(row=4, column=1)


class Mode1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        for i in range(3):
            self.columnconfigure(i, weight=1)
        label = tk.Label(self, text="Mode 1", font=('Arial', 18))
        label.grid(row=0, column=1, padx=10, pady=10)

        letters_box = tk.Text(self, height=1, width=14, font=('Arial', 18))
        letters_box.grid(row=1, column=1, pady=10)

        results_box = tk.Text(self, height=8, width=14, font=('Arial', 18))
        results_box.grid(row=2, column=1, sticky='news')

        scrollbar = tk.Scrollbar(
            self,
            orient='vertical',
            command=results_box.yview
        )
        scrollbar.grid(row=2, column=1, sticky='nes')
        results_box.configure(yscrollcommand=scrollbar.set)

        generate_letters_button = tk.Button(
            self,
            text="Generate letters",
            command=lambda: functions.display_letters_random(letters_box, results_box)
        )
        generate_letters_button.grid(row=3, column=1)

        generate_results_button = tk.Button(
            self,
            text="Show results",
            command=lambda: functions.display_longest_words(letters_box.get('1.0', tk.END), results_box)
        )
        generate_results_button.grid(row=4, column=1)

        switch_window_button = tk.Button(
            self,
            text="Return to Main Menu",
            command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.grid(row=6, column=1)


class Mode2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the Side Page")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Return to Main Menu",
            command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class Mode3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the Side Page")
        label.pack(padx=10, pady=10)

        switch_window_button = ttk.Button(
            self,
            text="Return to Main Menu",
            command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


if __name__ == "__main__":
    testObj = Windows()
    testObj.geometry("500x500")
    testObj.mainloop()
