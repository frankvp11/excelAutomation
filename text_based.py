from openpyxl import Workbook, load_workbook
from os import listdir
from os.path import isfile, join
import time
import json
from helper2 import couldnt_find_client, get_curr_price, get_curr_job
import os
from datetime import datetime



path = "C:/Users/frank/Desktop/excelAutomation/clientFiles"
all_files = [file for file in listdir(path) if isfile(join(path, file))]

def get_curr_client():
    current_client = input("Enter the client's full name whos file you want to change: \n")
    return current_client

def could_find_client(current_client):
    print("Was able to find client")
    current_price = get_curr_price()
    current_job = get_curr_job()
    current_address = read_data2(current_client)["Address"]
    date_job_done = get_date()
    os.system("cls")
    return current_price, current_job, current_address, date_job_done


def get_date():
    date = input("What day did you do this on? \n")
    return date

def insert_data(current_price, current_job, current_address, current_client, date_done):
    path = f"C:/Users/frank/Desktop/excelAutomation/clientFiles/{current_client}.xlsx"
    workbook = load_workbook(path)
    worksheet = workbook.active
    worksheet.cell(10, 2, current_client) 
    worksheet.cell(11, 2, current_address)
    date = datetime.today().strftime('%Y-%m-%d')
    worksheet.cell(10, 10, date)
    if worksheet.cell(21, 3).value == None:
        worksheet.cell(21, 3, current_job)
        worksheet.cell(21, 10, current_price)
        worksheet.cell(21, 7, date_done)
    else:
        if worksheet.cell(22, 3).value == None:
            worksheet.cell(22, 3, current_job)
            worksheet.cell(22, 10, current_price)
            worksheet.cell(22, 7, date_done)

        else:
            if worksheet.cell(23, 3).value == None:
                worksheet.cell(23, 3, current_job)
                worksheet.cell(23, 10, current_price)
                worksheet.cell(23, 7, date_done)

            else:
                if worksheet.cell(24, 3).value == None:                
                    worksheet.cell(24, 3, current_job)
                    worksheet.cell(24, 10, current_price)
                    worksheet.cell(24, 7, date_done)
                    print("full")
                    want_to_print = input("Would you like to print? Y/N\n").lower()
                    if want_to_print == "y":
                        print(f"Your book is full, currently working to print {current_client}'s file")
                        print("Please hold")
                        os.startfile(path, 'print')
                        time.sleep(20)
                    clear_cell_input = input("Would you like to empty the previous person's file? Y/N \n").lower()
                    if clear_cell_input == "y":
                        clear_file(workbook, path)
                        return
    print("Done inserting data")
    workbook.save(path)  
                        
def clear_file(workbook, path):
    worksheet = workbook.active
    worksheet.cell(21, 3).value=None
    worksheet.cell(21, 10).value=None
    worksheet.cell(22, 3).value=None
    worksheet.cell(22, 10).value=None
    worksheet.cell(23, 3).value=None
    worksheet.cell(23, 10).value=None
    worksheet.cell(24, 3).value=None
    worksheet.cell(24, 10).value=None
    worksheet.cell(21, 7).value=None
    worksheet.cell(22, 7).value=None
    worksheet.cell(23, 7).value=None
    worksheet.cell(24, 7).value=None

    
    workbook.save(path)

                


def read_data2(current_client):
    with open("data.json", "r") as file:
        data = json.load(file)
        stack = data["Clients"]
        while stack:
            if current_client in stack[0]:
                return stack[0][current_client]
            stack.pop(0)
            

def read_txt(current_client):
    with open("clients.txt", "r") as file:
        data = file.read()
        if current_client in data:
            return True
    return False




def interrogate():
    current_client = get_curr_client()
    boolean_client_in_text = read_txt(current_client)
    if f"{current_client}.xlsx" in all_files or boolean_client_in_text:
        current_price, current_job, current_address, date_done = could_find_client(current_client)
  
        insert_data(current_price, current_job, current_address, current_client, date_done)
    else:
        couldnt_find_client(current_client)
    interrogate()

#interrogate()
