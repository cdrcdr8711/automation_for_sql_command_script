# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 09:56:24 2022

@author: Daniel chuang 
"""
import sqlite3
from sqlite3 import OperationalError
import os 
import glob 


def executeScriptsFromFile(database,filename):
    # connect to database 
    conn = sqlite3.connect(database)  # db
    c = conn.cursor()
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        try:
            c.execute(command)
            print(c.fetchall())
        except OperationalError:
            print("Command skipped: ")
        
        #     print("Command skipped: ", msg)
    c.close()
    conn.close()

def fileinfolder(path):
    current_path = os.path.dirname(__file__)
    find_file_list = glob.glob(current_path + "\*.sql")
    return find_file_list


if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    # print(current_path)
    # print(fileinfolder(current_path))
    database = 'inspurer.db' # 指定 database
    for i in fileinfolder(current_path): ### 使用方法: 將sql file 放置此資料夾底下
        executeScriptsFromFile(database,i) 
        print("\n")
    
    
    