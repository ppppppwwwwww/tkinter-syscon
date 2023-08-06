import tkinter as tk
import tkinter.messagebox
from tkinter import Button
from tkinter import Label
from tkinter import filedialog

root = tk.Tk()


def choose_dictory():
    folder_name = filedialog.askdirectory()  # 获取文件夹
    if '/' in folder_name:
        # 用\替换/，注意'\\'的用法，
        # 如果直接使用'\'，会被系统识别成转义字符
        folder_name.replace('/', '\\')
        print('找到1')

    if len(folder_name) == 0:
        print('未找到文件夹！')
    else:
        lb.config(text='您选择的文件夹是' + folder_name)
        print('文件夹是:', folder_name)
    return folder_name


def confirm():
    answer = tkinter.messagebox.askokcancel('请选择', '请选择确定或取消')
    if answer:
        lb.config(text='已确认')
    else:
        lb.config(text='已取消')


lb1 = Label(root, text='')
lb2 = Label(root, text='')
lb = Label(root, text='')
global old_directory_object
old_directory_object = Button(root, text="选择基线syscon的yml所在文件夹", command=choose_dictory).pack()
print(old_directory_object)
lb1 = lb
lb1.pack()
new_directory_object = Button(root, text="选择新的syscon的yml所在文件夹", command=choose_dictory).pack()
lb2 = lb
lb2.pack()

btn = Button(root, text='弹出对话框', command=confirm)
btn.pack()

root.geometry('780x560+300+300')  # 窗口的宽度x高度（x是小写的x,不是*）
root.title('syscon对比')
root.config(bg='#ffffff')

root.mainloop()
