import tkinter as tk
import time

class CountdownTimerApp:
    def __init__(self, root, seconds):
        self.root = root
        self.seconds = seconds
        self.label = tk.Label(root, font=('Arial', 48))
        self.label.pack(padx=20, pady=20)
        self.update_timer()

    def update_timer(self):
        mins, secs = divmod(self.seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        self.label.config(text=timer)
        if self.seconds > 0:
            self.seconds -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.label.config(text="Countdown Complete!")

def main():
    seconds = 120  # Set the countdown time here
    root = tk.Tk()
    root.geometry("500x100")
    root.title("Countdown Timer")
    app = CountdownTimerApp(root, seconds)
    root.mainloop()

if __name__ == "__main__":
    main()
