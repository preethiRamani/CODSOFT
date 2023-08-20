import tkinter
import tkinter.messagebox
import pickle
n=tkinter.Tk()
n.title("To do list")

def adding_task():
    p=task_add.get()
    if p !="":
        todo_list.insert(tkinter.END,p)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning..!!",message="To add a task, please enter the task")
def removing_task():
    try:
        index_p=todo_list.curselection()[0]
        todo_list.delete(index_p)
    except:
        tkinter.messagebox.showwarning(title="Warning!!",message="To delete a task you must select the task")
def loading_task():
    try:
        q=pickle.load(open("tasks.dat","rb"))
        list1.delete(0,tkinter.END)
        for p in tasks:
            list1.inset(tkinter.END,p)
    except:
        tkinter.messagebox.showwarning(title="Warning!!",message="Cannot find task.dat")
def save_task():
    r=list1.get(0,list1.size())
    pickle.dump(r,open("tasks.dat","wb"))

list1=tkinter.Frame(n)
list1.pack()
todo_list=tkinter.Listbox(list1,height=20,width=60)
todo_list.pack(side=tkinter.LEFT)
scrollbar=tkinter.Scrollbar(list1)
scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
todo_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=todo_list.yview)

task_add=tkinter.Entry(n,width=30)
task_add.pack()

add_button=tkinter.Button(n,text="Click To Add Task",font=("arial",30,"bold"),background="Orange",width=40,command=adding_task)
add_button.pack()

remove_button=tkinter.Button(n,text="Click To Delete Task",font=("arial",30,"bold"),background="blue",width=40,command=removing_task)
remove_button.pack()

loading_button=tkinter.Button(n,text="Click To Load Task",font=("arial",30,"bold"),background="yellow",width=40,command=loading_task)
loading_button.pack()

save_button=tkinter.Button(n,text="Click to save task",font=("arial",30,"bold"),background="green",width=40,command=save_task)
save_button.pack()

n.mainloop()
