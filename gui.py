# Program to make a simple
# login screen


import tkinter as tk
import internetSearch

root=tk.Tk()

# setting the windows size
root.geometry("1200x800")

# variable to hold the question
question=tk.StringVar()


# submit the question
def submit():

    questionText=question.get()

    print("The question is : " + questionText)
    internetSearch.search(questionText)
    question.set("")


# update the window
def update():
    # creating a label for
    # name using widget Label
    name_label = tk.Label(root, text = 'Question', font=('calibre',10, 'bold'))

    # creating a entry for input
    # name using widget Entry
    questionEntry = tk.Entry(root,textvariable = question, font=('calibre',10,'normal'))

    # creating a button using the widget
    # Button that will call the submit function
    sub_btn=tk.Button(root,text = 'Submit', command = submit)

    # placing the label and entry in
    # the required position using grid
    # method
    name_label.grid(row=0,column=0)
    questionEntry.grid(row=0,column=1)
    sub_btn.grid(row=2,column=1)

    # performing an infinite loop
    # for the window to display
    root.mainloop()
