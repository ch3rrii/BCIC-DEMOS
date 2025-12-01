import tkinter as tk

# Project Name: Button Demo 
# Author: Stefany Alicea
# Objective: Using python GUI and Tkinter library, create a button that moves and when it is clicked the button changes color, text, and speed


class MovingButtonApp:
    def __init__(self, root: tk.Tk) -> None:
        #app setup
        self.root = root
        self.root.title("Catch the Button")
        self.root.geometry("600x200")

        # State for animation
        self.button_x = 80
        self.button_y = 80
        self.button_speed = 1       # pixels per frame
        self.is_moving = True       # start in motion

        # Info label
        self.info_label = tk.Label(self.root, text="Click the button to stop it!")
        self.info_label.pack(pady=10)

        # The moving button
        self.move_button = tk.Button(
            self.root,
            text="Catch me",
            command=self.on_button_click,  # stops the motion
        )

        # Use place() so we can control coordinates
        self.move_button.place(x=self.button_x, y=self.button_y)

        # Start the animation loop
        self.animate()

    def animate(self) -> None:
        """Move the button across the window while is_moving is True."""
        if self.is_moving:
            # Update x position
            self.button_x += self.button_speed

            # Wrap around when reaching the right edge
            window_width = self.root.winfo_width()
            button_width = self.move_button.winfo_width() or 80  # fallback before layout

            if self.button_x > window_width - button_width:
                self.button_x = 0

            # Apply the new position
            self.move_button.place(x=self.button_x, y=self.button_y)

        # Schedule the next frame
        self.root.after(30, self.animate)  # ~33 frames per second

    def on_button_click(self) -> None:
        """Stop the button when clicked."""

        if self.is_moving:
            self.is_moving = False
            self.info_label.config(text="Nice! You stopped the button.")
            #visual feedback 
            self.move_button.config(
                text ="Clicked!!!",
                bg = "pink", #background color
                fg = "red", #text color
            )
            self.root.config(bg="light pink")
            self.button_speed +=3
            print("This is the speed now: " + str(self.button_speed))
        else:
            # Optional: let students “restart” the movement
            self.is_moving = True
            self.info_label.config(text="Moving again – try to stop it!")
            # Visual feedback when starting again
            self.move_button.config(
                text="Catch me",
                bg="SystemButtonFace",  # default look on Windows; adjust as needed
                fg="black",
            )
            self.root.config(bg="SystemButtonFace")

def main():
    root = tk.Tk()
    app = MovingButtonApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
