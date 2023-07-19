import tkinter as tk
import datetime
import sys
import os

if sys.platform.startswith('linux'):
    import pygame
    pygame.init()

class AlarmClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Alarm Clock")
        self.root.geometry("400x375")

        self.alarm_time = datetime.datetime.now()
        self.alarm_set = False
        self.alarm_playing = False

        self.create_widgets()
        self.update_clock()

    def create_widgets(self):
        self.clock_label = tk.Label(self.root, font=("Arial", 24))
        self.clock_label.pack(pady=20)

        self.alarm_status_label = tk.Label(self.root, font=("Arial", 16))
        self.alarm_status_label.pack()

        self.alarm_time_label = tk.Label(self.root, font=("Arial", 16))
        self.alarm_time_label.pack()

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
                self.alarm_status_label.config(text="Alarm is set")
                self.alarm_time_label.config(text=f"Alarm time: {self.alarm_time.strftime('%H:%M')}")
            else:
                self.alarm_status_label.config(text="Invalid Time")
                self.alarm_time_label.config(text="")
        else:
            self.alarm_status_label.config(text="Invalid Input")
            self.alarm_time_label.config(text="")

    def turn_on(self):
        if self.alarm_set and not self.alarm_playing:
            current_time = datetime.datetime.now()
            if current_time >= self.alarm_time:
                self.play_alarm()
            else:
                self.root.after(int((self.alarm_time - current_time).total_seconds() * 1000), self.play_alarm)

    def play_alarm(self):
        if sys.platform.startswith('linux'):
            pygame.mixer.music.load('C:\\Users\\FrankieV\\Desktop\\Cut_The_Crap.mp3')
            pygame.mixer.music.play(-1)  # Set -1 to repeat indefinitely
        elif sys.platform.startswith('win'):
            os.startfile('C:\\Users\\FrankieV\\Desktop\\Cut_The_Crap.mp3')

        self.alarm_playing = True

    def turn_off(self):
        if sys.platform.startswith('linux'):
            pygame.mixer.music.stop()
        elif sys.platform.startswith('win'):
            os.system("TASKKILL /F /IM wmplayer.exe")

        self.alarm_status_label.config(text="")
        self.alarm_time_label.config(text="")
        self.alarm_set = False
        self.alarm_playing = False

    def snooze(self):
        if self.alarm_set:
            self.alarm_time += datetime.timedelta(minutes=5)
            self.turn_off()
            self.turn_on()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    alarm_clock = AlarmClock()
    alarm_clock.run()
