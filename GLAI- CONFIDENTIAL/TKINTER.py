import os
import signal
import subprocess
import tkinter as tk
from tkinter import ttk

class CodeRunnerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GLAI")
        self.root.geometry("800x600")  # Increased size
        self.root.configure(bg="sky blue")

        # Initial interface with start button
        self.create_start_interface()

    def create_start_interface(self):
        # Create a label for the start interface
        title_label = ttk.Label(self.root, text="Gesturelink Accessibility Interface", font=("Arial", 18, "bold"))
        title_label.pack(pady=20)

        # Create a start button
        start_button = ttk.Button(self.root, text="Start", command=self.show_main_interface, style="TButton")
        start_button.pack(pady=10, ipadx=20, ipady=10)  # Adjusted size to match script buttons

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12, "bold"), padding=(10, 5), background="sky blue")

    def show_main_interface(self):
        # Destroy the widgets in the start interface
        for widget in self.root.winfo_children():
            widget.destroy()

        # Continue with the main interface
        self.root.geometry("800x600")  # Increased size
        self.script_names = {
            "HAND CONTROLL": r"C:\Users\shinchan\OneDrive\Documents\NANOTHON 2.0\LED Controller\LED Controller\main.py",
            "VOICE CONTROL": r"C:\Users\shinchan\OneDrive\Documents\NANOTHON 2.0\LED Controller (Voice)\LED Controller (Voice)\main.py",
            "HAND AND VOICE": r"C:\Users\shinchan\OneDrive\Documents\NANOTHON 2.0\Merging properties HAND AND VOICE\MAIN.py",
            "VIRTUAL MOUSE": r"C:\Users\shinchan\OneDrive\Documents\NANOTHON 2.0\Virtual mouse basic.py",
            "VIRTUAL CANVAS": r"DIGITAL_BOARD_CANVAS\Air-Canvas-with-ML-master\air_canvas_ml.py",
            "VIRTUAL KEYBOARD": r"Virtual-Keyboard-using-Python-main\virtual_keyboard.py",
        }

        # Apply themed style
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12, "bold"), padding=(10, 5), background="sky blue")

        self.create_main_interface()

        # Add text indications with specified formatting
        indications_label = ttk.Label(self.root, text="*  Click on the button to run the operation\n"
                                                     "*  Click only one time to run the code\n"
                                                     "*  Clicking the button twice or more leads to error\n"
                                                     "*  MADE WITH  ❤️ accessibility for every one", font=("Times New Roman", 10, "bold"), background="sky blue")
        indications_label.pack(pady=20)

    def create_main_interface(self):
        # Create buttons for each script with adjusted styling
        for title, script_path in self.script_names.items():
            button = ttk.Button(self.root, text=title, command=lambda path=script_path: self.toggle_script(path), style="TButton")
            button.pack(pady=10, ipadx=20, ipady=10)  # Adjusted size to match start button

    def toggle_script(self, script_path):
        # Check if a script is currently running
        if hasattr(self, 'process') and self.process.poll() is None:
            try:
                # Use process.terminate() to stop the script
                self.process.terminate()
            except Exception as e:
                # If terminate() fails, try sending a SIGTERM signal
                try:
                    os.kill(self.process.pid, signal.SIGTERM)
                except Exception as e:
                    print(f"Error stopping script: {str(e)}")
        else:
            try:
                # Use subprocess.Popen to run the script
                self.process = subprocess.Popen(["python", script_path])
            except Exception as e:
                print(f"Error running script: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeRunnerApp(root)
    root.mainloop()
