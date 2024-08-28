import pygame

def chkwinner():
    global gameover, rects, winner_combo
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)          
    ]
    for combo in win_combos:
        if texts[combo[0]] == texts[combo[1]] == texts[combo[2]] and texts[combo[0]] != "":
            gameover = True
            winner_combo = combo
            winner = texts[combo[0]]
            return winner
    if "" not in texts:
        gameover = True
        return "Draw"

pygame.init()

pygame.display.set_caption("Tic Tac Toe")

w = 400
h = 500
sc = pygame.display.set_mode((w, h))

gray = '#343434'
lgray = '#646464'
blue = '#4584b6'
yellow = '#ffde57'

font = pygame.font.SysFont("Arial Black", 80)
font2 = pygame.font.SysFont("Arial Black", 20)
font3 = pygame.font.SysFont("Arial Black", 50)

rects = [
    pygame.Rect(25, 75, 108, 108),
    pygame.Rect(143, 75, 113, 108),
    pygame.Rect(266, 75, 108, 108),
    pygame.Rect(25, 193, 108, 113),
    pygame.Rect(143, 193, 113, 113),
    pygame.Rect(266, 193, 108, 113),
    pygame.Rect(25, 316, 108, 108),
    pygame.Rect(143, 316, 113, 108),
    pygame.Rect(266, 316, 108, 108)
]

texts = [""] * 9

run = True
main_screen = True
game_started = True
gameover = False
curr_turn = "O"
winner = None
restart = False
winner_combo = ""

while run:
    if main_screen:
        sc.fill(gray)
        
        title_rect = pygame.Rect(20, 30, 360, 100)
        pygame.draw.rect(sc, lgray, title_rect)
        title = font.render("Tic Tac", True, yellow)
        title_text_rect = title.get_rect(center=title_rect.center)
        sc.blit(title, title_text_rect)
        
        title2_rect = pygame.Rect(20, 130, 360, 100)
        pygame.draw.rect(sc, lgray, title2_rect)
        title2 = font.render("Toe", True, yellow)
        title2_text_rect = title2.get_rect(center=title2_rect.center)
        sc.blit(title2, title2_text_rect)
        
        start_rect = pygame.Rect(100, 260, 200, 60)
        pygame.draw.rect(sc, blue, start_rect)
        start = font3.render("START", True, yellow)
        start_text_rect = start.get_rect(center=start_rect.center)
        sc.blit(start, start_text_rect)
        
        exit_rect = pygame.Rect(100, 360, 200, 60)
        pygame.draw.rect(sc, blue, exit_rect)
        exit = font3.render("EXIT", True, yellow)
        exit_text_rect = exit.get_rect(center=exit_rect.center)
        sc.blit(exit, exit_text_rect)
        
        pygame.display.update()
        
    elif game_started:
        sc.fill(gray)
        
        turn_rect = pygame.Rect(0, 0, 400, 50)
        pygame.draw.rect(sc, lgray, turn_rect)
        
        restart_rect = pygame.Rect(0, 450, 180, 50)
        pygame.draw.rect(sc, lgray, restart_rect)
        
        main_menu_rect = pygame.Rect(220, 450, 180, 50)
        pygame.draw.rect(sc, lgray, main_menu_rect)
        
        h1_rect = pygame.Rect(25, 183, 350, 10)
        pygame.draw.rect(sc, yellow, h1_rect)
        h2_rect = pygame.Rect(25, 306, 350, 10)
        pygame.draw.rect(sc, yellow, h2_rect)
        
        v1_rect = pygame.Rect(133, 75, 10, 350)
        pygame.draw.rect(sc, yellow, v1_rect)
        v2_rect = pygame.Rect(256, 75, 10, 350)
        pygame.draw.rect(sc, yellow, v2_rect)
        
        if gameover:
            turn_text = font2.render(f"{winner} Wins!", True, 'white')
        else:
            turn_text = font2.render(f"{curr_turn}'s Turn", True, 'white')
            
        turn_text_rect = turn_text.get_rect(center=turn_rect.center)
        sc.blit(turn_text, turn_text_rect)
        
        restart_text = font2.render("RESTART", True, 'white')
        restart_text_rect = restart_text.get_rect(center=restart_rect.center)
        sc.blit(restart_text, restart_text_rect)
        
        main_menu_text = font2.render("MAIN MENU", True, 'white')
        main_menu_text_rect = main_menu_text.get_rect(center=main_menu_rect.center)
        sc.blit(main_menu_text, main_menu_text_rect)
        
        for i, rect in enumerate(rects):
            pygame.draw.rect(sc, gray, rect)
            text = font.render(texts[i], True, blue)
            text_rect = text.get_rect(center=rect.center)
            sc.blit(text, text_rect)
        
        winner = chkwinner()
        
        if gameover and winner != "Draw" and winner_combo != "":
            for i in winner_combo:
                pygame.draw.rect(sc, lgray, rects[i])
                text = font.render(texts[i], True, 'limegreen')
                text_rect = text.get_rect(center=rects[i].center)
                sc.blit(text, text_rect)
            if winner_combo:
                start_pos = rects[winner_combo[0]].center
                end_pos = rects[winner_combo[2]].center
                pygame.draw.line(sc, 'red', start_pos, end_pos, 5)
                
        pygame.display.update()
    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and main_screen:
            if start_rect.collidepoint(event.pos):
                game_started = True
                main_screen = False
            elif exit_rect.collidepoint(event.pos):
                run = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN and not restart:
            if restart_rect.collidepoint(event.pos):
                restart = True
            elif main_menu_rect.collidepoint(event.pos):
                main_screen = True
                restart = True
                
            else:
                for i, rect in enumerate(rects):
                    if rect.collidepoint(event.pos) and texts[i] == "":
                        texts[i] = curr_turn
                        curr_turn = "O" if curr_turn == "X" else "X"
                        
                        pygame.display.update()
                    
    if gameover:
        win_rect = pygame.Rect(0, 0, 400, 50)
        pygame.draw.rect(sc, blue, win_rect)
        if winner == "Draw":
            win_text = font2.render(f"Draw!!", True, 'white')
        else:
            win_text = font2.render(f"{winner} Wins!!", True, yellow)
        win_text_rect = win_text.get_rect(center=win_rect.center)
        sc.blit(win_text, win_text_rect)
        
        pygame.display.update()
        game_started = False
        
    if restart:
        texts = [""] * 9
        curr_turn = "O"
        gameover = False
        game_started = True
        winner = None
        restart = False

pygame.quit()
