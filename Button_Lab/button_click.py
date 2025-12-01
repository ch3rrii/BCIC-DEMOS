import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Clickable Button")
    root.geometry("400x200")

    # Label to show feedback
    message_label = tk.Label(root, text="Click the button!")
    message_label.pack(pady=10)

    # This is the behavior: what should happen on click?
    def on_button_click():
        message_label.config(text="Button was clicked!")

    # Button OBJECT + behavior
    click_me_button = tk.Button(
        root,
        text="Click me",
        command=on_button_click,  # no () here – we pass the function itself
    )
    click_me_button.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
