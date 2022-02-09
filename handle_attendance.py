import os
from datetime import datetime

def mark_attendance(name: str) -> None:
    filename = 'Attendance.csv'
    if not os.path.exists(filename):
        f = open(filename, "x")
        f.close()
    with open('Attendance.csv', 'r+') as f:
        my_datalist = f.readlines()
        name_list = []
        for line in my_datalist:
            entry = line.split(',')
            name_list.append(entry[0])
        if name not in name_list:
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            f.writelines(f'=> {name}, {time}, {date}\n')
