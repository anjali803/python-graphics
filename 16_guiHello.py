import tkinter as tk

class HelloWorldFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello, World!")
        
        # Create a label with the text "Hello, World!"
        label = tk.Label(self, text="Hello, World!")
        label.pack(padx=20, pady=20)

if __name__ == "__main__":
    HelloWorldFrame().mainloop()