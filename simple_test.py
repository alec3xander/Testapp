import tkinter as tk

def on_closing(root):
    root.destroy()

def main():
    root = tk.Tk()
    root.title("Simple Test App")
    label = tk.Label(root, text="¡Hola, Mundo!")
    label.pack()
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))
    root.mainloop()

if __name__ == "__main__":
    main()
