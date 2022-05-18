
from turtle import Screen
import pygame, sys
from button import Button
from inputBox import InputBox
from helper2 import write_json, write_txt, create_new
from text_based import insert_data, read_txt, read_excel, read_data2, insert_data2, print_file
import pandas as pd
from datetime import datetime, timedelta
from dateutil import parser


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def new_client():
    client_name = InputBox(500, 130, 300, 50)
    client_address = InputBox(500, 240, 300, 50)
    client_job_price1 = InputBox(500, 340, 300, 50)
    client_job_description1 = InputBox(500, 440, 300, 50)
    client_job_price2 = InputBox(850, 340, 300, 50)
    client_job_description2 = InputBox(850, 440, 300, 50)
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(20).render("This is the new client screen.", True, "White")
        client_name_text = get_font(20).render("Enter the client's name here", True, "white")
        client_address_text = get_font(20).render("Enter the client's address here", True, 'white')
        name_text_rect = client_name_text.get_rect(center=(640, 100))
        address_text_rect = client_address_text.get_rect(center=(640, 200))
        client_price_text = get_font(20).render("Price:", True, 'white')
        client_price_rect = client_price_text.get_rect(center=(640, 310))
        client_job_desc = get_font(20).render("Job/ Job Description:", True, 'white')
        client_job_desc_rect = client_job_desc.get_rect(center=(640,410))
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(client_job_desc, client_job_desc_rect)
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        SCREEN.blit(client_name_text, name_text_rect)
        SCREEN.blit(client_address_text, address_text_rect)
        SCREEN.blit(client_price_text, client_price_rect)

        PLAY_BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        done_button = Button(image=None, pos=(640, 550), text_input="Save", font=get_font(30), base_color='white', hovering_color='green')
        done_button.changeColor(PLAY_MOUSE_POS)
        done_button.update(SCREEN)
        
 


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if done_button.checkForInput(PLAY_MOUSE_POS):
                    current_client = client_name.text
                    current_address = client_address.text
                    current_job_desc = client_job_description1.text
                    current_job_price = client_job_price1.text
                    if client_job_description2.text != "" and client_job_price2.text != "":
                        y = {current_client:{"Address":current_address, 
                                             "Jobs": [current_job_desc, client_job_description2.text],
                                             "Price": [current_job_price, client_job_price2.text]}}
                    else:
                        y = {current_client:{"Address":current_address, 
                                             "Jobs": [current_job_desc],
                                             "Price": [current_job_price]}}
                    write_json(y)
                    write_txt(current_client)
                    create_new(current_client)
                    client_name.text = ""
                    client_address.text = ""
                    client_job_description1.text = ""
                    client_job_price1.text = ""
                    client_job_description2.text = ""
                    client_job_price2.text = ""
            client_name.handle_event(event, SCREEN)
            client_address.handle_event(event, SCREEN)
            client_job_description1.handle_event(event, SCREEN)
            client_job_price1.handle_event(event, SCREEN)
            client_job_description2.handle_event(event, SCREEN)
            client_job_price2.handle_event(event, SCREEN)


        client_job_description1.update()
        client_job_description1.draw(SCREEN)
        client_job_description2.update()
        client_job_description2.draw(SCREEN)
        client_job_price1.update()
        client_job_price1.draw(SCREEN)
        client_job_price2.update()
        client_job_price2.draw(SCREEN)
        client_address.update()
        client_address.draw(SCREEN)
        client_name.update()
        client_name.draw(SCREEN)


        pygame.display.update()
    


def existing_client():
    client_name = InputBox(500, 200, 300, 50)
    is_in_text = False

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        client_name_text = get_font(20).render("Enter the client's name here", True, "white")
        name_text_rect = client_name_text.get_rect(center=(640, 160))
        SCREEN.blit(client_name_text, name_text_rect)
        OPTIONS_TEXT = get_font(15).render("This is the existing clients screen.", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 620), 
                            text_input="BACK", font=get_font(20), base_color="white", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        save_button = Button(image=None, pos=(640, 350), text_input="Save", font=get_font(20), base_color="white", hovering_color="green")
        save_button.changeColor(OPTIONS_MOUSE_POS)
        save_button.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if save_button.checkForInput(OPTIONS_MOUSE_POS):
                    current_client = client_name.text
                    is_in_text = read_txt(current_client)
                    if is_in_text:
                        change_data_screen(current_client)                   
                    
            client_name.handle_event(event, SCREEN)

        client_name.update()
        client_name.draw(SCREEN)

        pygame.display.update()

def change_data_screen(current_client):
    path = f"C:/Users/frank/Desktop/excelAutomation/clientFiles/{current_client}.xlsx"

    jobs_done, prices_for_jobs, dates = read_excel(current_client)
    dates_dict = []
    jobs_done_dict = []
    prices_for_jobs_dict = []
    
    for i in range(5):
        try:
            dates[i] = parser.parse(dates[i])
            dates_dict.append(InputBox(300, 150+i*50, 250, 50, text=dates[i].strftime("%d %b %Y ")))
            jobs_done_dict.append(InputBox(50, 150+i*50, 250, 50, text=jobs_done[i]))
            prices_for_jobs_dict.append(InputBox(550, 150+i*50, 125, 50, text=f"{prices_for_jobs[i]}"))
        except:
            dates_dict.append(InputBox(300, 150+i*50, 250, 50))
            jobs_done_dict.append(InputBox(50, 150+i*50, 250, 50))
            prices_for_jobs_dict.append(InputBox(550, 150+i*50, 125, 50))
    
    jobs_buttons = []
    jobs = read_data2(current_client)['Jobs']
    for i in range(len(jobs)):
        jobs_buttons.append(Button(image=None, pos=(800+i*150, 100), text_input=jobs[i], font=get_font(15), base_color='white', hovering_color='green'))


    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        jobs_done_text = get_font(15).render("Job done", True, 'white')
        jobs_done_text_rect = jobs_done_text.get_rect(center=(150, 125))
        jobs_date_text = get_font(15).render("Date done", True, 'white')
        jobs_date_text_rect = jobs_date_text.get_rect(center=(450, 125))
        SCREEN.blit(jobs_date_text, jobs_date_text_rect)
        SCREEN.blit(jobs_done_text, jobs_done_text_rect)
        client_name_text = get_font(20).render(current_client, True, 'white')
        client_name_rect = client_name_text.get_rect(center=(150,50))
        SCREEN.blit(client_name_text, client_name_rect)
        save_button = Button(image=None, pos=(1100, 700), text_input="Save", font=get_font(20), base_color='white', hovering_color='Green')
        save_button.changeColor(OPTIONS_MOUSE_POS)
        save_button.update(SCREEN)
        





        print_button = Button(image=None, pos=(1100, 600), text_input="Print File", font=get_font(20), base_color='white', hovering_color='green')
        print_button.changeColor(OPTIONS_MOUSE_POS)
        print_button.update(SCREEN)
        
        OPTIONS_BACK = Button(image=None, pos=(640, 620), 
                            text_input="BACK", font=get_font(20), base_color="white", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        change_all_4_wk = Button(image=None, pos=(1150, 100), text_input="4 weeks", base_color='white',
                                hovering_color='Green', font=get_font(15))
                    
        change_all_4_wk.changeColor(OPTIONS_MOUSE_POS)
        change_all_4_wk.update(SCREEN)
        weeks_button_dict = []
        jobs_button_dict = []
        for i in range(5):
            weeks_button_dict.append(Button(image=None, pos=(1150, 175+i*50), text_input=f"{i + 1}", base_color='white', hovering_color='Green', font=get_font(25)))
            jobs_button_dict.append(Button(image=None, pos=(900, 175+i*50), text_input=f"{i + 1}", base_color='white', hovering_color='Green', font=get_font(25)))
        for i in range(len(weeks_button_dict)):
            weeks_button_dict[i].changeColor(OPTIONS_MOUSE_POS)
            weeks_button_dict[i].update(SCREEN)
            jobs_button_dict[i].changeColor(OPTIONS_MOUSE_POS)
            jobs_button_dict[i].update(SCREEN)
        for i in range(len(dates_dict)):
            dates_dict[i].update()
            dates_dict[i].draw(SCREEN)
            jobs_done_dict[i].update()
            jobs_done_dict[i].draw(SCREEN)
            prices_for_jobs_dict[i].update()
            prices_for_jobs_dict[i].draw(SCREEN)

        for i in range(len(jobs_buttons)):
            jobs_buttons[i].changeColor(OPTIONS_MOUSE_POS)
            
            jobs_buttons[i].update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if print_button.checkForInput(OPTIONS_MOUSE_POS):
                    print_file(path)
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    existing_client()
                try:
                    if jobs_buttons[0].checkForInput(OPTIONS_MOUSE_POS):
                        jobs_buttons[0].base_color = 'Blue'
                        jobs_buttons[1].base_color = 'White'
                    if jobs_buttons[1].checkForInput(OPTIONS_MOUSE_POS):
                        jobs_buttons[1].base_color = 'Blue'
                        jobs_buttons[0].base_color = 'White'
                except:
                    if jobs_buttons[0].checkForInput(OPTIONS_MOUSE_POS):
                        jobs_buttons[0].base_color = 'Blue'
                
                if save_button.checkForInput(OPTIONS_MOUSE_POS):
                    for i in range(5):
                        try:
                            if prices_for_jobs_dict[i].text[0] == "$":
                                prices_for_jobs_dict[i].text = prices_for_jobs_dict[i].text[1:]
                        except:
                            break

                    insert_data2(prices_for_jobs_dict, jobs_done_dict, read_data2(current_client)["Address"], current_client, dates_dict)
                    change_data_screen(current_client)
                for i in range(len(weeks_button_dict)):
                        if weeks_button_dict[i].checkForInput(OPTIONS_MOUSE_POS):  
                            dates[i] += timedelta(weeks=4)
                            dates_dict[i] = InputBox(300, 150+i*50, 250, 50, text=dates[i].strftime("%d %b %Y"))
                for i in range(len(jobs_button_dict)):
                    if jobs_button_dict[i].checkForInput(OPTIONS_MOUSE_POS):
                        try:
                            if jobs_buttons[0].base_color == 'Blue':
                                jobs_done_dict[i] = InputBox(50, 150+i*50, 250, 50, text=jobs_done[0])
                                prices_for_jobs_dict[i] = InputBox(550, 150+i*50, 125, 50, text=read_data2(current_client)["Price"][0])
   
                            if jobs_buttons[1].base_color == 'Blue':
                                jobs_done_dict[i] = InputBox(50, 150+i*50, 250, 50, text=jobs[1])
                                prices_for_jobs_dict[i] = InputBox(550, 150+i*50, 125, 50, text=read_data2(current_client)["Price"][1])

                        except IndexError:
                            if jobs_buttons[0].base_color == 'Blue':
                                jobs_done_dict[i] = InputBox(50, 150+i*50, 250, 50, text=jobs[0])
                                prices_for_jobs_dict[i] = InputBox(550, 150+i*50, 125, 50, text=read_data2(current_client)["Price"][0])
                        

                        

            for i in range(len(dates_dict)):
                dates_dict[i].handle_event(event, SCREEN)
                jobs_done_dict[i].handle_event(event, SCREEN)
                prices_for_jobs_dict[i].handle_event(event, SCREEN)
            

            





        change_dates = get_font(15).render("Change Date", True, 'white')
        change_dates_rect = change_dates.get_rect(center=(1150, 50))
        SCREEN.blit(change_dates, change_dates_rect)
        add_job_to_file = get_font(15).render("Add Jobs", True, 'white')
        add_job_to_file_rect = add_job_to_file.get_rect(center=(900, 50))
        SCREEN.blit(add_job_to_file, add_job_to_file_rect)

            
        pygame.display.update()
    

    

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="New Client", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="Existing Clients", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    new_client()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    existing_client()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()