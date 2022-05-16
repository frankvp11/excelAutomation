from gc import get_referents
from turtle import Screen
import pygame, sys
from button import Button
from inputBox import InputBox
from helper2 import write_json, write_txt, create_new
from text_based import read_txt, read_excel

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def new_client():
    client_name = InputBox(500, 200, 300, 50)
    client_address = InputBox(500, 340, 300, 50)
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(20).render("This is the new client screen.", True, "White")
        client_name_text = get_font(20).render("Enter the client's name here", True, "white")
        client_address_text = get_font(20).render("Enter the client's address here", True, 'white')
        name_text_rect = client_name_text.get_rect(center=(640, 160))
        address_text_rect = client_address_text.get_rect(center=(640, 300))
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        SCREEN.blit(client_name_text, name_text_rect)
        SCREEN.blit(client_address_text, address_text_rect)

        PLAY_BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        done_button = Button(image=None, pos=(640, 500), text_input="Save", font=get_font(30), base_color='white', hovering_color='green')
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
                    y = {current_client:{"Address":current_address}}
                    write_json(y)
                    write_txt(current_client)
                    create_new(current_client)
                    client_name.text = ""
                    client_address.text = ""
            client_name.handle_event(event, SCREEN)
            client_address.handle_event(event, SCREEN)
        
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
    jobs_done, prices_for_jobs, dates = read_excel(current_client)
    while True:
        SCREEN.fill("black")
        client_name_text = get_font(15).render(current_client, True, 'white')
        client_name_rect = client_name_text.get_rect(center=(150,50))
        SCREEN.blit(client_name_text, client_name_rect)
        for i in range(len(jobs_done)):
            jobs_currently_done = get_font(15).render(jobs_done[i], True, 'white')
            jobs_done_rect = jobs_currently_done.get_rect(center=(150, i+1*100))
            SCREEN.blit(jobs_currently_done, jobs_done_rect)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



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