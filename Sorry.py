# for i in range(1,100001):
#     print(i,"Tejas")

# a = [1,2,3]
# b = a.copy()
# print(b == a, a is b)

# a = 7
# b = 5 
# c = a + b if a>b else b - a
# print(c)

# def my_fun(x,y):
#     if y == 0:
#         return 1
#     else:
#         return x* my_fun(x, y-1) 
# print(my_fun(2,8))

# k = pow(2,8)
# # print(k)
# import datetime
# import tkinter as tk
# from PIL import Image, ImageTk

# class Person:
#     def __init__(self, name, birthdate):
#         self.name = name
#         self.birthdate = birthdate
    
#     def age(self):
#         today = datetime.date.today()
#         age_days = (today - self.birthdate).days
#         age_years = age_days // 365
#         age_months = (age_days % 365) // 30
#         age_days = age_days % 30
#         return age_years, age_months, age_days

# def calculate_age():
#     name = name_entry.get()
#     year = int(year_entry.get())
#     month = int(month_entry.get())
#     day = int(date_entry.get())
#     birthdate = datetime.date(year, month, day)
#     person = Person(name, birthdate)
#     age_years, age_months, age_days = person.age()
#     answer = f"Hey {name}!!! You are {age_years} years, {age_months} months, and {age_days} days old!!!"
#     text_area.delete("1.0", tk.END)
#     text_area.insert(tk.END, answer)

# window = tk.Tk()
# window.title("Age Calculator App")
# window.geometry("620x780")

# name_label = tk.Label(text="Name")
# name_label.grid(column=0, row=1)

# year_label = tk.Label(text="Year")
# year_label.grid(column=0, row=2)

# month_label = tk.Label(text="Month")
# month_label.grid(column=0, row=3)

# date_label = tk.Label(text="Day")
# date_label.grid(column=0, row=4)

# name_entry = tk.Entry()
# name_entry.grid(column=1, row=1)

# year_entry = tk.Entry()
# year_entry.grid(column=1, row=2)

# month_entry = tk.Entry()
# month_entry.grid(column=1, row=3)

# date_entry = tk.Entry()
# date_entry.grid(column=1, row=4)

# button = tk.Button(text="Calculate Age", command=calculate_age, bg="pink")
# button.grid(column=1, row=5)

# text_area = tk.Text(master=window, height=10, width=25)
# text_area.grid(column=1, row=6)

# image = Image.open("54e3c837cd3ac3970fb460902cf3fc9e.jpg")
# image.thumbnail((300, 300), Image.ANTIALIAS)
# photo = ImageTk.PhotoImage(image)

# image_label = tk.Label(image=photo)
# image_label.grid(column=1, row=0)

# window.mainloop()

