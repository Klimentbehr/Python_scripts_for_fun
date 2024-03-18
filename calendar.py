import tkinter as tk
from tkinter import ttk
import calendar

def show_calendar():
    year = int(year_entry.get())
  
    full_calendar = calendar.calendar(year)
    
    calendar_text.delete(1.0, tk.END)
   
    calendar_text.insert('1.0', full_calendar)

root = tk.Tk()
root.title("Calendar App")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

year_label = ttk.Label(frame, text="Enter Year:")
year_label.pack(padx=5, pady=5)

year_entry = ttk.Entry(frame)
year_entry.pack(padx=5, pady=5)
year_entry.focus()

show_button = ttk.Button(frame, text="Show Calendar", command=show_calendar)
show_button.pack(padx=5, pady=5)

calendar_text = tk.Text(root, wrap=tk.WORD, width=50, height=10)
calendar_text.pack(padx=10, pady=10)

root.mainloop()
