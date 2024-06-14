import tkinter as tk
from tkinter import messagebox, simpledialog
import calendar
from datetime import datetime


class WorkTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Work Tracker")

        self.year = datetime.now().year
        self.month = datetime.now().month
        self.days_off_count = 0
        self.max_days_off = 28

        self.work_days = []
        self.days_off = []
        self.holidays = []

        self.create_widgets()
        self.update_calendar()

    def create_widgets(self):
        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.pack(pady=20)

        self.nav_frame = tk.Frame(self.root)
        self.nav_frame.pack()

        self.prev_btn = tk.Button(self.nav_frame, text="<", command=self.prev_month)
        self.prev_btn.pack(side=tk.LEFT)

        self.month_label = tk.Label(self.nav_frame, text="", width=15)
        self.month_label.pack(side=tk.LEFT)

        self.next_btn = tk.Button(self.nav_frame, text=">", command=self.next_month)
        self.next_btn.pack(side=tk.LEFT)

        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(pady=20)

        self.work_btn = tk.Button(self.control_frame, text="Set Work Day", command=self.set_work_day)
        self.work_btn.pack(side=tk.LEFT, padx=5)

        self.off_btn = tk.Button(self.control_frame, text="Set Day Off", command=self.set_day_off)
        self.off_btn.pack(side=tk.LEFT, padx=5)

        self.holiday_btn = tk.Button(self.control_frame, text="Set Holiday", command=self.set_holiday)
        self.holiday_btn.pack(side=tk.LEFT, padx=5)

        self.info_frame = tk.Frame(self.root)
        self.info_frame.pack(pady=20, padx=10, side=tk.RIGHT)

        self.max_off_label = tk.Label(self.info_frame, text=f"Max Days Off: {self.max_days_off}")
        self.max_off_label.pack()

        self.days_used_label = tk.Label(self.info_frame, text=f"Days Used: 0")
        self.days_used_label.pack()

        self.days_remaining_label = tk.Label(self.info_frame, text=f"Days Remaining: {self.max_days_off}")
        self.days_remaining_label.pack()

    def update_calendar(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        self.month_label.config(text=f"{calendar.month_name[self.month]} {self.year}")

        days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        week_header = tk.Frame(self.calendar_frame)
        week_header.pack()
        for day in days_of_week:
            lbl = tk.Label(week_header, text=day, width=5, height=2, borderwidth=1, relief="solid")
            lbl.pack(side=tk.LEFT)

        cal = calendar.Calendar()
        month_days = cal.monthdayscalendar(self.year, self.month)

        for week in month_days:
            row = tk.Frame(self.calendar_frame)
            row.pack()
            for day in week:
                if day == 0:
                    lbl = tk.Label(row, text=" ", width=5, height=2)
                else:
                    lbl = tk.Label(row, text=str(day), width=5, height=2, borderwidth=1, relief="solid")
                    lbl.bind("<Button-1>", lambda e, day=day: self.select_day(day))

                    if (self.year, self.month, day) in self.work_days:
                        lbl.config(bg="green")
                    elif (self.year, self.month, day) in self.days_off:
                        lbl.config(bg="grey")
                    elif (self.year, self.month, day) in self.holidays:
                        lbl.config(bg="purple")

                lbl.pack(side=tk.LEFT)

    def select_day(self, day):
        selected_date = (self.year, self.month, day)
        if selected_date in self.work_days:
            self.work_days.remove(selected_date)
        elif selected_date in self.days_off:
            self.days_off.remove(selected_date)
            self.days_off_count -= 1
        elif selected_date in self.holidays:
            self.holidays.remove(selected_date)
        else:
            if len(self.work_days) < self.max_days_off:
                self.days_off.append(selected_date)
