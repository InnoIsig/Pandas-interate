#
# student_list = {"student": ["Innocent", "David", "Isaac"],
#                 "score":[74, 58, 67]}
#
# # for (key, value) in student_list.items():
# #     print(value)
#
# import  pandas
# student_data_frame = pandas.DataFrame(student_list)
# print(student_data_frame)
# for (index, row) in student_data_frame.iterrows():
#     if row.student == "Innocent":
#         print(row.score)


import turtle
import tkinter
import random

time = turtle.Turtle()
screen = turtle.Screen()
label = tkinter.Label(text="❤❤❤ I AM INNOCENT A FUTURE PROGRAMMER ❤❤❤", font=("Helvetica", 20), bg="white", )
screen.bgcolor("black")
time.speed(0)

colors = ["red", "pink", "yellow", "blue", "cyan", "light green"]

for i in range(150):
    time.pencolor(colors[i % 6])
    time.circle(190 - i / 2, 90)
    time.lt(90)
    time.circle(190 - i / 3, 90)
    time.lt(60)

label.pack()


screen.exitonclick()
