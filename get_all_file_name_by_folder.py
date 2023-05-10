#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tools 
@File    ：get_all_file_name_by_folder.py
@Author  ：sadnesspineapple
@Date    ：2023/5/10 11:08 
'''
# built-in package
import os
# project package

# third package



# 读取一个文件夹下的所有文件，并打印出来



dir = "/Users/sadnesspineapple/Desktop/mmd/ray-mmd"


class Dir:
    def __init__(self, path: str):
        self.path = path
        self.name = path.split("/")[-1]
        self.children_dir = []
        self.children_file = []
        self.ignore_dir = [".git"]

    def file_list(self, index, s):
        for f in os.listdir(self.path):
            if f in self.ignore_dir:
                continue
            path = self.path + "/" + f
            if os.path.isdir(path):
                self.children_dir.append(Dir(path))
            else:
                self.children_file.append(File(f))

        # 打印文件名
        # for cf in self.children_file:
        #     s += "-" * (index + 1) + cf.name + "\n"

        # 打印文件夹名，递归查询所有的文件夹
        for cd in self.children_dir:
            s += "-" * (index + 1) + cd.name + "\n"
            s = cd.file_list(index + 1, s)
        return s


class File:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    dir = Dir(dir)
    s = f"{dir.name}\n"
    s = dir.file_list(1, s)
    print(s)
