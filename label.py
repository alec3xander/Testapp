import tkinter as tk

def on_closing(root):
    root.destroy()

def change_text(label):
    label.config(text="¡Texto cambiado!")

def main():
    root = tk.Tk()
    root.title("Simple Test App")
    label = tk.Label(root, text="¡Hola, Mundo!")
    label.pack()
    
    button = tk.Button(root, text="Cambiar texto", command=lambda: change_text(label))
    button.pack()
    
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))
    root.mainloop()

if __name__ == "__main__":
    main()
