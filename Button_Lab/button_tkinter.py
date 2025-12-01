import tkinter as tk


def main():
    # 1. Create the main window (the app "frame")
    root = tk.Tk()
    root.title("My First Button")
    root.geometry("400x200")  # width x height

    # 2. Create a Button OBJECT
    hello_button = tk.Button(
        root,
        text="Hello, world!",   # text shown on the button
    )

    # 3. Put the button on the window
    hello_button.pack(pady=20)

    # 4. Start the event loop (Tkinter watches for clicks, etc.)
    root.mainloop()


if __name__ == "__main__":
    main()

