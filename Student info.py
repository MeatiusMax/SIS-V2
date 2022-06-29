#import libraries
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

#=========================================Database===============================
def Database():
    global conn, cursor
    conn = sqlite3.connect("student2.db")
    cursor = conn.cursor()
    #creating table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS StudentDB (STU_ID TEXT, STU_NAME TEXT, STU_GENDER TEXT, STU_YEAR TEXT, STU_COURSEID TEXT, STU_COURSENAME TEXT)")

#=======================Display========================================
def DisplayForm():
    display_screen = Tk()
    display_screen.geometry("1100x500")
    display_screen.title("Student Management System")
    global tree
    global SEARCH
    global Name,Year,Gender,CourseID,CourseName,Stu_id
    SEARCH = StringVar()
    Name = StringVar()
    Year = StringVar()
    Gender = StringVar()
    CourseID = StringVar()
    CourseName = StringVar()
    Stu_id = StringVar()
#============================================Frames===============================
    TopViewFrame = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewFrame.pack(side=TOP, fill=X)
    Lframe1 = Frame(display_screen, width="350")
    Lframe1.pack(side=LEFT, fill=Y)
    Lframe2 = Frame(display_screen, width=500,bg="gray")
    Lframe2.pack(side=LEFT, fill=Y)
    MidViewFrame = Frame(display_screen, width=600)
    #label
    MidViewFrame.pack(side=RIGHT)
    lbl_text = Label(TopViewFrame, text="Student Management System", font=('verdana', 18), width=600,bg="#1C2833",fg="white")
    lbl_text.pack(fill=X)
    Label(Lframe1, text="Student Id  ", font=("Arial", 12)).pack(side=TOP)
    Entry(Lframe1,font=("Arial",10,"bold"),textvariable=Stu_id).pack(side=TOP, padx=10, fill=X)
    Label(Lframe1, text="Full Name  ", font=("Arial", 12)).pack(side=TOP)
    Entry(Lframe1,font=("Arial",10,"bold"),textvariable=Name).pack(side=TOP, padx=10, fill=X)
    Label(Lframe1, text="Year ", font=("Arial", 12)).pack(side=TOP)
    Entry(Lframe1, font=("Arial", 10, "bold"),textvariable=Year).pack(side=TOP, padx=10, fill=X)
    Label(Lframe1, text="Gender ", font=("Arial", 12)).pack(side=TOP)
    Entry(Lframe1, font=("Arial", 10, "bold"),textvariable=Gender).pack(side=TOP, padx=10, fill=X)
    Label(Lframe1, text="CourseID ", font=("Arial", 12)).pack(side=TOP)
    Entry(Lframe1, font=("Arial", 10, "bold"),textvariable=CourseID).pack(side=TOP, padx=10, fill=X)
    Label(Lframe1, text="CourseName ", font=("Arial", 12)).pack(side=TOP)
    Entry(Lframe1, font=("Arial", 10, "bold"),textvariable=CourseName).pack(side=TOP, padx=10, fill=X)
    Button(Lframe1,text="Add",font=("Arial", 10, "bold"),command=register).pack(side=TOP, padx=10,pady=5, fill=X)

#=====================================Buttons,Entry,Scrollbar==================================
    #search label and entry 
    lbl_txtsearch = Label(Lframe2, text="Enter Student ID to Search", font=('verdana', 10),bg="gray")
    lbl_txtsearch.pack()
    #search entry
    search = Entry(Lframe2, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    #search button
    btn_search = Button(Lframe2, text="Search", command=SearchRecord)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    #view button
    btn_view = Button(Lframe2, text="View All", command=DisplayData)
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    #delete button
    btn_delete = Button(Lframe2, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating update button
    btn_Update = Button(Lframe2, text="Update", command=Update)
    btn_Update.pack(side=TOP, padx=10, pady=10, fill=X)
    #setting scrollbar
    scrollbarx = Scrollbar(MidViewFrame, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewFrame, orient=VERTICAL)
    tree = ttk.Treeview(MidViewFrame,columns=("Student Id", "Name", "Year", "Gender","CourseID","CourseName"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
#===========================Display Table=================================
    tree.heading('Student Id', text="Student ID", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Year', text="Year", anchor=W)
    tree.heading('Gender', text="Gender", anchor=W)
    tree.heading('CourseID', text="CourseID", anchor=W)
    tree.heading('CourseName', text="CourseName", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()
#============================Functions=========================
#function to Add data into database
def register():
    Database()
    Name1=Name.get()
    Year1=Year.get()
    Gender1=Gender.get()
    CourseID1=CourseID.get()
    CourseName1=CourseName.get()
    Stuid=Stu_id.get()
    #Warning id entry is empty
    if Name1=='' or Year1==''or Gender1=='' or CourseID1==''or CourseName1==''or Stuid=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        conn.execute('INSERT INTO StudentDB (STU_Name,STU_Year,STU_Gender,STU_CourseID,STU_CourseName,STU_ID) \
              VALUES (?,?,?,?,?,?)',(Name1,Year1,Gender1,CourseID1,CourseName1,Stuid));
        conn.commit()
        tkMessageBox.showinfo("Message","Stored successfully")
        DisplayData()
        conn.close()
#function to Delete data in the database
def Delete():
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM StudentDB WHERE STU_ID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
#function to Update data in database
def Update():
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to Update")
        DisplayData()
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to Update this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM StudentDB WHERE STU_ID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
        elif result == 'no':
            DisplayData()
    Name2=Name.get()
    Year2=Year.get()
    Gender2=Gender.get()
    CourseID2=CourseID.get()
    CourseName2=CourseName.get()
    Stuid2=Stu_id.get()
    if Name2=='' or Year2==''or Gender2=='' or CourseID2==''or CourseName2=='' or Stuid2=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        conn.execute('INSERT INTO StudentDB (STU_Name,STU_Year,STU_Gender,STU_CourseID,STU_CourseName,STU_ID) \
              VALUES (?,?,?,?,?,?)',(Name2,Year2,Gender2,CourseID2,CourseName2,Stuid2));
        conn.commit()
        tkMessageBox.showinfo("Message","Updated successfully") 
        DisplayData()
        conn.close()
#===================Search================
def SearchRecord():
    Database()
    #error if search is empty
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        cursor=conn.execute("SELECT * FROM StudentDB WHERE STU_ID LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
#==============================Display Data==================
def DisplayData():
    Database()
    tree.delete(*tree.get_children())
    cursor=conn.execute("SELECT * FROM StudentDB")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

#calling function
DisplayForm()
if __name__=='__main__':
#Running Application
 mainloop()