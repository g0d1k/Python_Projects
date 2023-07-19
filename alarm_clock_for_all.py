import tkinter as tk
import datetime
import sys
import os
from tkinter import messagebox

if sys.platform.startswith('linux'):
    import pygame
    pygame.init()

class AlarmClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Alarm Clock")
        self.root.geometry("400x200")
        
        self.alarm_time = datetime.datetime.now()
        self.alarm_set = False
        
        self.create_widgets()
        self.update_clock()

    def create_widgets(self):
        self.clock_label = tk.Label(self.root, font=("Arial", 24))
        self.clock_label.pack(pady=20)

        self.alarm_label = tk.Label(self.root, text="Set alarm:", font=("Arial", 14))
        self.alarm_label.pack()

        self.hour_entry = tk.Entry(self.root, width=2, font=("Arial", 14))
        self.hour_entry.pack(side=tk.LEFT)
        self.minute_entry = tk.Entry(self.root, width=2, font=("Arial", 14))
        self.minute_entry.pack(side=tk.LEFT)

        self.set_button = tk.Button(self.root, text="Set Alarm", font=("Arial", 14), command=self.set_alarm)
        self.set_button.pack(pady=10)

        self.on_button = tk.Button(self.root, text="Turn On", font=("Arial", 14), command=self.turn_on)
        self.on_button.pack(pady=5)

        self.off_button = tk.Button(self.root, text="Turn Off", font=("Arial", 14), command=self.turn_off)
        self.off_button.pack(pady=5)

        self.snooze_button = tk.Button(self.root, text="Snooze", font=("Arial", 14), command=self.snooze)
        self.snooze_button.pack(pady=5)

    def update_clock(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

    def set_alarm(self):
        hour_input = self.hour_entry.get()
        minute_input = self.minute_entry.get()

        if hour_input.isdigit() and minute_input.isdigit():
            hour = int(hour_input)
            minute = int(minute_input)

            if 0 <= hour < 24 and 0 <= minute < 60:
                self.alarm_time = datetime.datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
                self.alarm_set = True
            else:
                messagebox.showerror("Invalid Time", "Please enter a valid time (0-23 for hours, 0-59 for minutes).")
        else:
            messagebox.showerror("Invalid Input", "Please enter numeric values for hours and minutes.")

    def turn_on(self):
        if self.alarm_set:
            current_time = datetime.datetime.now()
            if current_time >= self.alarm_time:
                self.play_alarm()
            else:
                self.root.after(int((self.alarm_time - current_time).total_seconds() * 1000), self.play_alarm)

    def play_alarm(self):
        if sys.platform.startswith('linux'):
            pygame.mixer.music.load('path_to_alarm_sound.wav')
            pygame.mixer.music.play()
        elif sys.platform.startswith('win'):
            os.startfile('path_to_alarm_sound.wav')

    def turn_off(self):
        if sys.platform.startswith('linux'):
            pygame.mixer.music.stop()
        elif sys.platform.startswith('win'):
            os.system("TASKKILL /F /IM wmplayer.exe")

    def snooze(self):
        if self.alarm_set:
            self.alarm_time += datetime.timedelta(minutes=5)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    alarm_clock = AlarmClock()
    alarm_clock.run()
