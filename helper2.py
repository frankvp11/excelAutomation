import shutil
import json
import os

def couldnt_find_client(current_client):
    print("Was unable to find client")
    create_new(current_client)
    print(f"Created file for {current_client}")
    current_address = get_curr_address()
    y = {current_client:{"Address":current_address}}   
    write_json(y)
    write_txt(current_client)
    os.system("cls")


def get_curr_address():
    current_address = input("Enter the client's address: \n")
    return current_address

def get_curr_price():
    current_price = int(input("Enter the client's price: \n"))
    return current_price



def get_curr_job():
    current_job = input("What will you be doing at this client? (Mowing, trimming, etc): \n")
    return current_job

def create_new(current_client):
    original = "C:/Users/frank/Desktop/excelAutomation/assets/template.xlsx"
    new = f"C:/Users/frank/Desktop/excelAutomation/clientFiles/{current_client}.xlsx"
    shutil.copyfile(original, new)


def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["Clients"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
 
def write_txt(new_data, filename="clients.txt"):
    with open(filename, 'a') as file:
        file.write(new_data + "\n")

