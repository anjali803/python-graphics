

import tkinter as tk

class LabelFieldApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Label and Field")

        # Create a label
        label = tk.Label(self, text="Enter your name:")
        label.pack(pady=10)

        # Create a text entry field
        self.entry = tk.Entry(self)
        self.entry.pack()

        # Create a button
        button = tk.Button(self, text="Submit", command=self.submit)
        button.pack(pady=10)

    def submit(self):
        name = self.entry.get()
        print("Name:", name)
        self.entry.delete(0, tk.END)  # Clear the entry field

if __name__ == "__main__":
    app = LabelFieldApp()
    app.mainloop()
