# Importations:
import ctypes, keyboard, threading, time, tkinter.messagebox


# Main code:
class Main:
    def __init__(self):
        # Variables:
        self.clicking = 0
        self.click_velocity = 0.005 # 0.005 milliseconds delay to go over 90/110 CPS (deppends the machine).

        self.color1, self.color2 = "#000000", "#ffffff" # Black and white.

        self.version = 1.0 # GG Autoclicker version.
        self.name, self.icon, self.screen_size = f"GG Autoclicker (version: {self.version})", tkinter.PhotoImage(file="icon.png"), "314x90"

        # Tkinter's screen creation:
        self.window = tkinter.Tk()
        self.window.title(self.name)
        self.window.geometry(self.screen_size)
        self.window.config(
            bg=self.color2,
            pady=3
        )
        # self.window.iconbitmap(self.icon)
        self.window.iconphoto(True, self.icon)
        self.window.resizable(
            width=0,
            height=0
        )

        # Text:
        self.explanation_label = tkinter.Label(
            self.window,
            text="Type a key to start or stop the autoclicker:",
            bg=self.color2,
            fg=self.color1,
            bd=0,
            relief=tkinter.SUNKEN
        )
        self.explanation_label.pack(pady=3)

        # Input to define the key:
        self.entry = tkinter.Entry (
            self.window,
            width=40,
            bg=self.color2,
            fg=self.color1,
            bd=2,
            relief=tkinter.SUNKEN
        )
        self.entry.pack(pady=5)

        # Button to confirm the entered key:
        self.set_button = tkinter.Button (
            self.window,
            text="Define key",
            command=self.set_hotkey,
            bg=self.color2,
            fg=self.color1,
            bd=2,
            relief=tkinter.RAISED
        )
        self.set_button.pack(pady=3)

        # Label to show the choosed key:
        self.label_hotkey = tkinter.Label(
            self.window,
            text="",
            bg=self.color2,
            fg=self.color1,
            bd=0,
            relief=tkinter.SUNKEN
        )
        self.label_hotkey.pack()

        # Tkinter main loop
        self.window.mainloop()

    # Click function:
    def start_clicking(self):
        self.clicking = 1

        while self.clicking:
            ctypes.windll.user32.mouse_event(0x2, 0, 0, 0, 0) # Left button down.
            ctypes.windll.user32.mouse_event(0x4, 0, 0, 0, 0) # Left button up.
            time.sleep(self.click_velocity) # Sleep time.

    # Toggle clicking function:
    def toggle_clicking(self):
        if self.clicking:
            self.clicking = 0
            self.set_button.config(state=tkinter.NORMAL) # Reactivate the button.

        else:
            self.set_button.config(state=tkinter.DISABLED) # Desactivate the button while is executing.
            thread = threading.Thread(target=self.start_clicking)
            thread.start()

    # Set hotkey function:
    def set_hotkey(self):
        hotkey = self.entry.get()  # Hotkey input.
        if hotkey:
            try:
                # Add hotkey:
                keyboard.add_hotkey (
                    hotkey,
                    self.toggle_clicking
                )
                self.window.geometry("314x109")
                self.label_hotkey.config(text=f"Defined key: {hotkey}")
            
            except ValueError:
                tkinter.messagebox.showerror (
                    title="Error",
                    message="Invalid key! Choose a valid key."
                )

if __name__ == "__main__":
    Main()
