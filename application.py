#! python3

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import yaml
import os


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_wiidget()
        self.directory = ""
        self.old_directory = ""
        self.new_directory = ""
        self.lst = [['山楂树下', '大瓶', '箱', '90'], ['寿司', '草莓', '盒', '36'],
                    ['山楂树下', '小瓶', '瓶', '12'], ['纸巾', '木浆', '包', '4.5'],
                    ['珍珠奶茶', '中杯', '杯', '25'], ['益寿醋', '十里河', '瓶', '6.2'],
                    ['益寿醋', '十里河', '瓶', '6.2'], ['益寿醋', '十里河', '瓶', '6.2']]

    def create_wiidget(self):
        self.btn01 = Button(self)
        self.btn01["text"] = "选择基线syscon的yml所在文件夹"
        self.btn01.pack()
        self.btn01["command"] = lambda: self.choose_dictory("old")

        self.btn02 = Button(self)
        self.btn02["text"] = "选择新的syscon的yml所在文件夹"
        self.btn02.pack()
        self.btn02["command"] = lambda: self.choose_dictory("new")

        self.btn03 = Button(self)
        self.btn03["text"] = "开始对比"
        self.btn03.pack()
        self.btn03["command"] = self.compare_syscon

    def choose_dictory(self, directory):
        folder_name = filedialog.askdirectory()  # 获取文件夹
        if '/' in folder_name:
            # 用\替换/，注意'\\'的用法，
            # 如果直接使用'\'，会被系统识别成转义字符
            folder_name.replace('/', '\\')
            messagebox.showinfo('您选择的文件夹是:', folder_name)
        if directory == "old":
            self.old_directory = folder_name
        if self.directory == "new":
            self.new_directory = folder_name

    def compare_syscon(self):
        old_ymls = os.listdir(self.old_directory)
        for yml in old_ymls:
            if yml.find("yml") > -1:
                file_url = self.old_directory + "\\" + yml
                yml_info = self.read(file_url)
                print(yml_info)
        self.show_signal(self.lst)

    def read(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            data = f.read()
            result = yaml.load(data, Loader=yaml.FullLoader)
        return result

    def show_signal(self, lst):
        # Create columns
        cols = []
        for i in range(1, 5):
            cols.append(i)

        # Create a tree display structure
        tree = ttk.Treeview(root, columns=cols, show='headings')

        # Define column width and position
        for m in range(1, 5):
            tree.column(f'{m}', width=100, anchor='center');

        # Define column names
        tree.heading('1', text='新增信号量');
        tree.heading('2', text='只读信号量');
        tree.heading('3', text='不可修改信号量');
        tree.heading('4', text='所属腔室');

        # Display the list datas in the window
        for m in range(0, len(lst)):
            tree.insert('', 'end', values=lst[m])

        # Define the tree structure layout
        tree.pack()


root = tk.Tk()
root.geometry('780x560+300+300')  # 窗口的宽度x高度（x是小写的x,不是*）
root.title('syscon对比')
root.config(bg='#ffffff')
app = Application(master=root)
root.mainloop()
