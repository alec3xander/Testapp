import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Tkinter Test")
    label = tk.Label(root, text="¡Tkinter está funcionando!")
    label.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
