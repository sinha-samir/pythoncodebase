from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk, messagebox
import pymysql


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        root.geometry('1350x700+0+0')
        self.root.config(bg="black")

        self.bg = ImageTk.PhotoImage(file="/Users/samirsinha/PycharmProjects/Jira/Backgroung.webp")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        self.left_bg = ImageTk.PhotoImage(file="/Users/samirsinha/PycharmProjects/Jira/CB-Background.jpeg")
        left_bg = Label(self.root, image=self.left_bg).place(x=0, y=0, width=250, relheight=1)

        frame1 = Frame(self.root, bg="grey91")
        frame1.place(x=300, y=100, width=700, height=900)

        # Title of Frame
        Label(frame1, text="Employee Registration Form", font=("times new roman", 20, "bold"), bg="grey91",
              fg="green").place(x=50, y=30)
        # Label Name of first column Employee Id
        Label(frame1, text="Employee ID", font=("times new roman", 15, "bold"), bg="grey91",
              fg="black").place(x=50, y=100)

        # Text Box for column Employee id
        self.txt_emp_id = Entry(frame1, font=("times new roman", 15, "bold", "italic"), bg="mint cream", fg="black", bd=1)
        self.txt_emp_id.place(x=50, y=130, width=250)

        # Label Name of Second column Comments
        Label(frame1, text="Comments", font=("times new roman", 15, "bold"), bg="grey91",
              fg="black").place(x=50, y=200)

        # Text Box for column Comments
        font_tuple = ("times new roman", 15, "italic")

        self.txt_emp_comments = Text(frame1, bg="mint cream", fg="black", wrap=WORD, width=15, height=10, bd=1)
        self.txt_emp_comments.place(x=50, y=230, width=300, height=200)
        self.txt_emp_comments.configure(font=font_tuple)

        # self.txt_emp_comments = Entry(frame1, font=("times new roman", 15, "bold", "italic"), bg="lightgrey", fg="black")
        # self.txt_emp_comments.place(x=50, y=230, width=300, height=200)

        # Button creation for submitting text
        Button(frame1, text='Submit', width=20, bd=1, cursor="hand2", bg="red", fg='green',
               command=self.register_data).place(x=100, y=480)

    def clear_data(self):

        self.txt_emp_id.delete(0, END)
        self.txt_emp_comments.delete("1.0", END)

    def register_data(self):
        # print(self.txt_emp_id.get(), self.txt_emp_comments.get("1.0", END))
        try:
            conn = pymysql.connect(host="localhost", user="root", password="sinha123", database="test")
            cur = conn.cursor()
            if self.txt_emp_id.get() == '':
                print("Please Enter Value for Employee Id")
                messagebox.showerror("Error", "Employee Id Is Needed For Submitting Comments", parent=self.root)
            else:
                if self.txt_emp_id.get().isdigit():
                    cur.execute("insert into employee_comments(employee_id, employee_comments) values(%s, %s)",
                            (
                                self.txt_emp_id.get(),
                                self.txt_emp_comments.get("1.0", END)
                            ))
                    messagebox.showinfo("Success", "Comments Submitted Successfully....", parent=self.root)
                else:
                    messagebox.showerror("Error", "Employee Id Should be Numeric", parent=self.root)

            conn.commit()
            conn.close()
            self.clear_data()

        except Exception as e:
            print("Some Error...", e)


root = Tk()
obj = Register(root)
root.mainloop()
