import tkinter as tk
from tkinter import *
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='harshit_bansal',
    port=3306,
    password='harshit_bansal_17',
    database='feedback_system'
)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        Name VARCHAR(100),
        Order_Number INTEGER PRIMARY KEY,
        Customer_Satisfaction INTEGER,
        Problems_Faced VARCHAR(255),
        Problem_Explained_in_Detail VARCHAR(1000)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        Order_Number INTEGER PRIMARY KEY,
        Order_Status VARCHAR(255)
    )
''')

cursor.execute('''
    INSERT INTO orders
    VALUES
    (101, 'Delivered'),
    (102, 'Delivered'),
    (103, 'Not Delivered'),
    (104, 'Delivered'),
    (105, 'Not Delivered'),
    (106, 'Delivered')
''')


def customer_feedback():
    order_no = e2.get()
    query = '''SELECT * FROM orders WHERE Order_Number = %s'''
    cursor.execute(query, (order_no,))
    result = cursor.fetchone()

    complaint_window = tk.Toplevel(master)
    complaint_window.title("Complaint Status")

    if result:
        complaint_label = tk.Label(complaint_window, text="Complaint Registered Successfully!")
    else:
        complaint_label = tk.Label(complaint_window, text="Invalid Order Number. Please try again.")

    complaint_label.pack(padx=10, pady=10)
    close_button = tk.Button(complaint_window, text="Close", command=complaint_window.destroy)
    close_button.pack(pady=10)


master = tk.Tk()
master.title('Customer Feedback')

tk.Label(master, text='Name:').grid(row=0, column=0, sticky='e', padx=10, pady=5)
tk.Label(master, text='Order Number:').grid(row=1, column=0, sticky='e', padx=10, pady=5)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(master, text='Overall Experience:').grid(row=2, column=0, columnspan=2, pady=5)
for i in range(1, 6):
    Checkbutton(master, text=str(i), variable=IntVar()).grid(row=3, column=i - 1, sticky=W, padx=5)

tk.Label(master, text='Problem Faced Area:').grid(row=4, column=0, columnspan=2, pady=5)
problem_areas = ['Delivery', 'Product Damaged/Not as Shown', 'Payment Issues', 'Request Regarding Order',
                 'Sharing Experience']
for i, area in enumerate(problem_areas):
    Checkbutton(master, text=area, variable=IntVar()).grid(row=5, column=i, sticky=W, padx=5)

button = tk.Button(master, text='Submit Feedback', width=20, command=customer_feedback)
button.grid(row=6, column=0, columnspan=2, pady=10)

master.mainloop()