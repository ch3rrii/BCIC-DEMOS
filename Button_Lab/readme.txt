
Lesson outline
Goal: Understand buttons as objects, attach behavior with callbacks, then animate a button and control it with clicks.

Suggested flow:
 - Create a window and a basic button.
 - Attach a click handler that changes something visible.
 - Make the button move automatically using a game-loop style pattern.
 - Stop the movement when the user clicks the button.
 - What is ‘Elegant code’ and try it out yourself.


Step 1 – A button as an object
Key idea: “A button is just an object with properties (text, position) and behaviors (what happens on click).”
Time: 45–60 minutes, assuming you have already seen functions and basic Python syntax.


Tools: Local Python 3 install or Replit + Tkinter environment.

####################################################################
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

####################################################################

Notice: root = tk.Tk() creates the window.

Questions to ponder: 
 - “Where is the button created?” (the line with tk.Button).
 - “What part of this code is ‘just data’ and what part is ‘behavior’?”
      - tk.Button(root, ...) constructs a button object with root as its parent.
      - hello_button.pack(...) tells Tkinter to actually display it.
      - root.mainloop() is the loop where Tkinter listens for events (like clicks).


Step 2 – Make the button respond to clicks
Key idea: Use the command parameter to attach a callback function that runs when the button is clicked.

####################################################################
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


####################################################################

Notice: command=on_button_click wires the button to the function.
Questions to ponder:
 - “What if we want the button to change its own text instead of a label?”
 - “Could we reuse the same handler for multiple buttons with different messages?”


Key takeaways: When the user clicks, Tkinter calls on_button_click automatically.
message_label.config(...) updates the label text on the screen, giving immediate feedback.


Step 3 – Moving button that stops when clicked
Key ideas:
 - Use place instead of pack so you can control x/y coordinates.
 - This version uses a class and __init__/self to keep all the GUI state and behavior bundled together like a tiny “game object.” That makes the code easier to grow (more buttons, more logic) without turning into a pile of globals.
 - Use root.after(delay_ms, func) to make a “soft game loop” that moves the button every few milliseconds.
 - Use a shared flag (e.g., is_moving) to start/stop movement from the click handler.

####################################################################
import tkinter as tk


class MovingButtonApp:
	def __init__(self, root: tk.Tk) -> None:
    	self.root = root
    	self.root.title("Catch the Button")
    	self.root.geometry("600x200")

    	# State for animation
    	self.button_x = 10
    	self.button_y = 80
    	self.button_speed = 5   	# pixels per frame
    	self.is_moving = True   	# start in motion

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
    	else:
        	# Optional: let students “restart” the movement
        	self.is_moving = True
        	self.info_label.config(text="Moving again – try to stop it!")


def main():
	root = tk.Tk()
	app = MovingButtonApp(root)
	root.mainloop()


if __name__ == "__main__":
	main()

####################################################################


Concepts to emphasize:
 - The button is stored as self.move_button, and the “world state” is stored as self.button_x, self.is_moving. This is a classic game-loop structure, just with Tkinter.
on_button_click controls state, not position directly, which keeps logic clean and testable.

Examples:
 - “Think of after as a reminder: ‘in 30 milliseconds, run animate again’.”
 -  “The button is like a character in a game with position and speed.” animate calls itself via self.root.after(30, self.animate) instead of using while True, which would freeze the GUI.

Why use a class, init, and self?
Class:
class MovingButtonApp: defines a new “type of thing” that knows how to:
 - store the window and button state,
 - update the animation,
 - react when the button is clicked.
It’s like making your own custom object called “app” instead of scattering variables and functions everywhere.


__init__:
def __init__(self, root: tk.Tk) -> None: is the constructor.
It runs automatically when you create the app: app = MovingButtonApp(root).
This is where you set up:
 - the window title and size,
 - the label,
 - the button,
 - the starting animation state,
 - and then start the animation loop.


self:
self means “this particular app object.”
Anything stored on self (like self.button_x, self.move_button) belongs to this instance.
That’s how animate and on_button_click share and update the same state without using global variables.

Why this design is “elegant” 
Single responsibility:
 - animate only handles movement and scheduling.
 - on_button_click only handles what happens when clicked.
Clear state:
 - All motion-related state lives in instance attributes (self.button_x, self.is_moving), not globals.
 - Progressive complexity:
	 - Start with a trivial button → reactive button → animated, stateful object.
 - Mirrors patterns they’ll see in real GUI and game code.



Make it your own: Play around. Break the code. Fix the code. Make it your own. 
 - Change speed via a slider or extra “Faster/Slower” buttons to reinforce the idea of state.
 - Change the colors, x/y coordinates. 
 - Change direction when the button hits a wall instead of wrapping, to introduce simple collision logic.
 - Add a “score” label that counts how many times they stop/restart the button, tying in variables and arithmetic.




