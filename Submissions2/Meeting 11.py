from tkinter import Tk, Canvas
from datetime import datetime

def update_clock():
   now = datetime.now()
   current_time = now.strftime('%H:%M:%S')
   current_date = now.strftime('%d/%m/%Y')
   c.itemconfig(clock_text, text=f"Date: {current_date}\nTime: {current_time}")
   root.after(1000, update_clock)  #1000ms = 1second

def get_events():
   list_events = []  #List kosong untuk menyimpan semua event
   with open('birthdays.txt') as file:
       for line in file:   #Membaca file baris demi baris
           line = line.rstrip('\n')
           current_event = line.split(',')
           event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
           current_event[1] = event_date
           list_events.append(current_event)
   print(list_events)
   return list_events

def days_between_dates(date1, date2):
   time_between = str(date1 - date2)
   number_of_days = time_between.split(' ')
   return number_of_days[0]

root = Tk()
c = Canvas(root, width=800, height=500, bg='lightblue')
c.pack()
c.create_text(100, 50, anchor='w', fill='darkblue', font='Arial 28 bold underline',
text='My Countdown Calendar')

events = get_events()
today = datetime.now().date()
vertical_space = 100
events.sort(key=lambda x: x[1])
# print(today)

for event in events:
   event_name = event[0]
   days_until = days_between_dates(event[1], today)
   display = f"It is {days_until} days until {event_name}"
   if int(days_until) <= 7:
       text_col = 'red'
   else:
       text_col = 'lightblue'
   c.create_text(100, vertical_space, anchor='w', fill=text_col, font='ComicSansMS 28 bold', text=display)
   vertical_space += 30

root.mainloop()