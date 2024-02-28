import tkinter as tk
import tkinter.font as tkFont
from tkinter import Entry, Label, Button, StringVar, ttk, messagebox
from Malware import MalwareScanner

class App:
    def __init__(self, root):
        root.title("Anti Virus")
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_381 = tk.Label(root)
        GLabel_381["anchor"] = "ne"
        GLabel_381["bg"] = "#ffffff"
        GLabel_381["cursor"] = "target"
        ft = tkFont.Font(family='Times', size=38)
        GLabel_381["font"] = ft
        GLabel_381["fg"] = "#000000"
        GLabel_381["justify"] = "center"
        GLabel_381["text"] = "Anti Virus Software"
        GLabel_381["relief"] = "flat"
        GLabel_381.place(x=100, y=70, width=433, height=62)

        GButton_291 = tk.Button(root)
        GButton_291["bg"] = "#ff0000"
        ft = tkFont.Font(family='Times', size=23)
        GButton_291["font"] = ft
        GButton_291["fg"] = "#ffffff"
        GButton_291["justify"] = "center"
        GButton_291["text"] = "EXIT"
        GButton_291.place(x=140, y=330, width=340, height=54)
        GButton_291["command"] = self.GButton_291_command

        GButton_538 = tk.Button(root)
        GButton_538["bg"] = "#0e8536"
        ft = tkFont.Font(family='Times', size=23)
        GButton_538["font"] = ft
        GButton_538["fg"] = "#ffffff"
        GButton_538["justify"] = "center"
        GButton_538["text"] = "SCAN NOW"
        GButton_538.place(x=140, y=170, width=340, height=54)
        GButton_538["command"] = self.GButton_538_command

        GButton_814 = tk.Button(root)
        GButton_814["bg"] = "#0d5fa4"
        ft = tkFont.Font(family='Times', size=23)
        GButton_814["font"] = ft
        GButton_814["fg"] = "#ffffff"
        GButton_814["justify"] = "center"
        GButton_814["text"] = "SCHEDULE SCAN"
        GButton_814.place(x=140, y=250, width=340, height=54)
        GButton_814["command"] = self.GButton_814_command

        self.scheduled_scan_id = None

    def GButton_291_command(self):
        print("command")
        root.destroy()

    def GButton_538_command(self):
        print("scan the file")
        malware_scanner = MalwareScanner()
        malware_scanner.scan()

    def GButton_814_command(self):
        self.schedule_scan_window()

    def schedule_scan_window(self):
        schedule_window = tk.Toplevel(root)
        schedule_window.title("Schedule Scan")
        schedule_window.geometry("400x200")

        label = tk.Label(schedule_window, text="Set time to schedule scan:")
        label.pack(pady=10)

        entry_var = StringVar()
        entry = Entry(schedule_window, textvariable=entry_var)
        entry.pack(pady=10)

        unit_var = StringVar()
        unit_var.set("seconds")
        unit_options = ["seconds", "minutes", "hours"]
        unit_combobox = ttk.Combobox(schedule_window, textvariable=unit_var, values=unit_options, state="readonly")
        unit_combobox.pack(pady=10)

        # Button to schedule scan
        schedule_button = Button(schedule_window, text="Schedule Scan", command=lambda: self.schedule_scan(entry_var.get(), unit_var.get(), schedule_window))
        schedule_button.pack(pady=10)

    def schedule_scan(self, time, unit, schedule_window):
        try:
            time = int(time)
            if unit == "seconds":
                time_in_seconds = time
            elif unit == "minutes":
                time_in_seconds = time * 60
            elif unit == "hours":
                time_in_seconds = time * 60 * 60

            if self.scheduled_scan_id:
                root.after_cancel(self.scheduled_scan_id)

            self.scheduled_scan_id = root.after(time_in_seconds * 1000, self.ask_to_scan, schedule_window)

            print(f"Scheduled scan in {time} {unit}")
            schedule_window.destroy()

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def ask_to_scan(self, schedule_window):
        answer = messagebox.askquestion("Scan Confirmation", "Do you want to start the scan now?")
        if answer == "yes":
            print("Scan confirmed. Initiating scan.")
            self.run_scheduled_scan(schedule_window)
        else:
            print("Scan canceled by user.")
            schedule_window.destroy()

    def run_scheduled_scan(self, schedule_window):
        print("Executing scheduled scan now.")
        malware_scanner = MalwareScanner()
        malware_scanner.scan()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
