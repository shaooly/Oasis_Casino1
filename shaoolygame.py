import pygame
from pygame import mixer
import random
from cards import cards
import time
import os
pygame.font.init()
pygame.init()
# Quit
Running = False
play_hand = True
# Constants
lobby_counter = 0
cash = "2500"
chips = "0"
money = 0
cards_list = []
placed_bet = "0"
black_jack_count = 0
no_instant_win = False
total_value = 0
stay = False
dealer_value = 0
total_hits = 0
total_dealer_hits = 0
ans = 0
placed_da_bet = False
bust = False
# Clock
clock = pygame.time.Clock()
REFRESH_RATE = 60

# Colors
RED = (255, 0, 0)
Dark_RED = (200, 0, 0)
GREEN = (0, 255, 0)
Dark_Green = (0, 200, 0)
black = (0, 0, 0)
WHITE = (255, 255, 255)
Dark_white = (215, 215, 215)

# Screen settings and setup
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("Oasis Casino")

# Text constants
verysmallText = pygame.font.SysFont("informalroman", 30)
smallText = pygame.font.SysFont("informalroman", 70)
largeText = pygame.font.SysFont("informalroman", 100)

# Background music and sound effects
background = mixer.music.load('Memoir of Summer.mp3')
mixer.music.play(-1)
wrong = pygame.mixer.Sound('buzzer.wav')
chips_sound = pygame.mixer.Sound('casino_chips.wav')
jackpot = pygame.mixer.Sound('jackpot.wav')
lose_chant = pygame.mixer.Sound('lose_chant.wav')
win_chant = pygame.mixer.Sound('win_chant.wav')
# Images
entrance_pos = 'entrance.jpg'
table = 'ntable.png'
lose = 'you_lose.png'
black_jack_win = 'black_jack.png'
hot = pygame.image.load("chipshop.png")
inside = pygame.image.load("inside.png")
entrance = pygame.image.load(entrance_pos)
black_jack_table = pygame.image.load(table)
black_jack_victory = pygame.image.load(black_jack_win)

# The cards
cards_list.append(cards(11, 1, 'Ace of clubs'))
cards_list.append(cards(2, 2, 'Two of clubs'))
cards_list.append(cards(3, 3, 'Three of clubs'))
cards_list.append(cards(4, 4, 'Four of clubs'))
cards_list.append(cards(5, 5, 'Five of clubs'))
cards_list.append(cards(6, 6, 'Six of clubs'))
cards_list.append(cards(7, 7, 'Seven of clubs'))
cards_list.append(cards(8, 8, 'Eight of clubs'))
cards_list.append(cards(9, 9, 'Nine of clubs'))
cards_list.append(cards(10, 10, 'Ten of clubs'))
cards_list.append(cards(10, 11, 'Jack of clubs'))
cards_list.append(cards(10, 12, 'Queen of clubs'))
cards_list.append(cards(10, 13, 'King of clubs'))
cards_list.append(cards(11, 14, 'Ace of diamond'))
cards_list.append(cards(2, 15, 'Two of diamond'))
cards_list.append(cards(3, 16, 'Three of diamond'))
cards_list.append(cards(4, 17, 'Four of diamond'))
cards_list.append(cards(5, 18, 'Five of diamond'))
cards_list.append(cards(6, 19, 'Six of diamond'))
cards_list.append(cards(7, 20, 'Seven of diamond'))
cards_list.append(cards(8, 21, 'Eight of diamond'))
cards_list.append(cards(9, 22, 'Nine of diamond'))
cards_list.append(cards(10, 23, 'Ten of diamond'))
cards_list.append(cards(10, 24, 'Jack of diamond'))
cards_list.append(cards(10, 25, 'Queen of diamond'))
cards_list.append(cards(10, 26, 'King of diamond'))
cards_list.append(cards(11, 27, 'Ace of hearts'))
cards_list.append(cards(2, 28, 'Two of hearts'))
cards_list.append(cards(3, 29, 'Three of hearts'))
cards_list.append(cards(4, 30, 'Four of hearts'))
cards_list.append(cards(5, 31, 'Five of hearts'))
cards_list.append(cards(6, 32, 'Six of hearts'))
cards_list.append(cards(7, 33, 'Seven of hearts'))
cards_list.append(cards(8, 34, 'Eight of hearts'))
cards_list.append(cards(9, 35, 'Nine of hearts'))
cards_list.append(cards(10, 36, 'Ten of hearts'))
cards_list.append(cards(10, 37, 'Jack of hearts'))
cards_list.append(cards(10, 38, 'Queen of hearts'))
cards_list.append(cards(10, 39, 'King of hearts'))
cards_list.append(cards(11, 40, 'Ace of spades'))
cards_list.append(cards(2, 41, 'Two of spades'))
cards_list.append(cards(3, 42, 'Three of spades'))
cards_list.append(cards(4, 43, 'Four of spades'))
cards_list.append(cards(5, 44, 'Five of spades'))
cards_list.append(cards(6, 45, 'Six of spades'))
cards_list.append(cards(7, 46, 'Seven of spades'))
cards_list.append(cards(8, 47, 'Eight of spades'))
cards_list.append(cards(9, 48, 'Nine of spades'))
cards_list.append(cards(10, 49, 'Ten of spades'))
cards_list.append(cards(10, 50, 'Jack of spades'))
cards_list.append(cards(10, 51, 'Queen of spades'))
cards_list.append(cards(10, 52, 'King of spades'))


# Text for buttons
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# Button
def button(msg, x, y, w, h, ic, ac, action=None):
    global lobby_counter
    global money
    global ans
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = (x + int(w / 2), y + int(h / 2))
        screen.blit(textSurf, textRect)
        if click[0] == 1 and action is not go_back and action is not cash_for_chips and action is not chips_for_cash \
                and action is not black_jack and action is not bet and action is not start_game and action is not \
                hit_me and action is not sit and action is not double and action is not instructions and action is not \
                back_to_start:
            time.sleep(0.2)
            action()
            lobby_counter += 1
        elif click[0] == 1 and action is go_back:
            time.sleep(0.2)
            action()
        elif click[0] == 1 and action is cash_for_chips:
            time.sleep(0.2)
            money = int(msg)
            action()
        elif click[0] == 1 and action is chips_for_cash:
            time.sleep(0.2)
            money = int(msg)
            action()
        elif click[0] == 1 and action is black_jack:
            time.sleep(0.2)
            lobby_counter += 2
            action()
        elif click[0] == 1 and action is bet:
            money = int(msg)
            time.sleep(0.2)
            action()
        elif click[0] == 1 and action is start_game:
            time.sleep(0.2)
            action()
        elif click[0] == 1 and action is hit_me:
            time.sleep(0.2)
            action()
        elif click[0] == 1 and action is sit:
            time.sleep(0.2)
            action()
        elif click[0] == 1 and action is double:
            time.sleep(0.2)
            action()
        elif click[0] == 1 and action is instructions:
            time.sleep(0.2)
            lobby_counter = 4
            action()
        elif click[0] == 1 and action is back_to_start:
            time.sleep(0.2)
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = (x + int(w / 2), y + int(h / 2))
        screen.blit(textSurf, textRect)


# Getting the chips
def cash_for_chips():
    global cash
    global chips
    cash = int(cash)
    chips = int(chips)
    cash - money
    if cash - money < 0:
        textSurfa, textRecta = text_objects("Insufficient fund!!!", smallText)
        textRecta.center = (700 + int(500 / 2), 300 + int(300 / 2))
        screen.blit(textSurfa, textRecta)
        pygame.mixer.Sound.play(wrong)
    else:
        pygame.mixer.Sound.play(chips_sound)
        cash = cash - money
        chips = chips + money
    cash = str(cash)
    chips = str(chips)


# Function that takes you back to the lobby
def back_to_lobby():
    global lobby_counter
    global black_jack_count
    global no_instant_win
    global placed_da_bet
    lobby_counter -= 2
    black_jack_count = 0
    no_instant_win = False
    placed_da_bet = False


# Starts a new blackjack game
def start_new():
    black_jack()
    values_to_zero()


# Chips for cash
def chips_for_cash():
    global cash
    global chips
    cash = int(cash)
    chips = int(chips)
    if chips - money < 0:
        textSurfa, textRecta = text_objects("Insufficient fund!!!", smallText)
        textRecta.center = (700 + int(500 / 2), 300 + int(300 / 2))
        screen.blit(textSurfa, textRecta)
        pygame.mixer.Sound.play(wrong)
    else:
        pygame.mixer.Sound.play(chips_sound)
        cash = cash + money
        chips = chips - money
    cash = str(cash)
    chips = str(chips)


# Go back
def go_back():
    global lobby_counter
    lobby_counter -= 1


# Quit game
def quit_game():
    pygame.quit()
    quit()


# Lobby
def lobby():
    screen.blit(inside, (0, 0))
# Welcome screen setup


def welcome_screen():
    screen.blit(entrance, (0, 0))
# Chip shop


def chip_shop():
    screen.blit(hot, (0, 0))


def load_image(image_loc, x, y, value, action, is_button=False):
    global money
    global lobby_counter
    image_loading = str(image_loc)
    load_the_image = pygame.image.load(image_loading)
    width, height = load_the_image.get_size()
    screen.blit(load_the_image, (x, y))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if is_button:
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            if click[0] == 1 and action is not None:
                if action == cash_for_chips:
                    time.sleep(0.2)
                    money = int(value)
                    cash_for_chips()
                elif click[0] == 1 and action == chips_for_cash:
                    time.sleep(0.2)
                    money = int(value)
                    chips_for_cash()
                elif click[0] == 1 and action is black_jack:
                    lobby_counter += 2
                    time.sleep(0.2)
                    action()
                elif click[0] == 1 and action is chip_shop:
                    time.sleep(0.2)
                    action()
                    lobby_counter +=1


# Text writing
def text_writing(text, x, y, w, h, font, fill, box=False, wait=False):
    if box:
        pygame.draw.rect(screen, fill, (x, y, w, h))
    if wait:
        textSurf, textRect = text_objects(text, font)
        textRect.center = (x + int(w / 2), y + int(h / 2))
        screen.blit(textSurf, textRect)
        pygame.display.flip()
        time.sleep(3)
    else:
        textSurf, textRect = text_objects(text, font)
        textRect.center = (x + int(w / 2), y + int(h / 2))
        screen.blit(textSurf, textRect)


# Black jack code
def black_jack():
    screen.fill(WHITE)
    screen.blit(black_jack_table, (0, 0))
    pygame.display.flip()


# Placing bets
def bet():
    global placed_bet
    global chips
    global money
    chips = int(chips)
    placed_bet = int(placed_bet)
    if chips - money < 0:
        textSurfa, textRecta = text_objects("Insufficient fund!!!", smallText)
        textRecta.center = (700 + int(500 / 2), 300 + int(300 / 2))
        screen.blit(textSurfa, textRecta)
        pygame.mixer.Sound.play(wrong)
    else:
        pygame.mixer.Sound.play(chips_sound)
        placed_bet += money
        chips -= money
    chips = str(chips)
    placed_bet = str(placed_bet)


# Start game
def start_game():
    global placed_bet
    global chips
    global no_instant_win
    global total_value
    global dealer_value
    global placed_da_bet
    global play_card_1
    global play_card_2
    global dealer_card_2
    chips = int(chips)
    play_card_1 = random.randint(0, 51)
    play_card_2 = random.randint(0, 51)
    dealer_card_1 = random.randint(0, 51)
    dealer_card_2 = random.randint(0, 51)
    load_image('card' + str(play_card_1 + 1) + '.png', 770, 700, 0, None, False)
    load_image('card' + str(play_card_2 + 1) + '.png', 900, 700, 0, None, False)
    load_image('card' + str(dealer_card_1 + 1) + '.png', 770, 239, 0, None, False)
    load_image('back_card.png', 900, 239, 0, None, False)
    total_value = cards_list[play_card_1].card_value() + cards_list[play_card_2].card_value()
    dealer_value = cards_list[dealer_card_1].card_value() + cards_list[dealer_card_2].card_value()
    if (cards_list[play_card_1].card_value() == 11 or cards_list[play_card_2].card_value() == 11) and total_value == 21:
        screen.blit(black_jack_victory, (723, 391))
        pygame.display.flip()
        pygame.mixer.Sound.play(jackpot)
        time.sleep(3)
        chips = chips + int(placed_bet) * 2
        values_to_zero()
        black_jack()
    else:
        no_instant_win = True
        placed_da_bet = True
    chips = str(chips)


def hit_me():
    hits = 0
    global total_hits
    global total_value
    global play_card_1
    global play_card_2
    global bust
    while hits == 0:
        new_play_card = random.randint(0, 51)
        total_value = total_value + cards_list[new_play_card].card_value()
        hits += 1
        total_hits += 1
    load_image('card' + str(new_play_card + 1) + '.png', (900 + total_hits * 130), 700, 0, None, False)
    if total_value > 21:
        if cards_list[play_card_1].card_value() == 11 or cards_list[play_card_2].card_value() == 11 or cards_list[new_play_card].card_value() == 11:
            total_value = total_value - 10
        else:
            pygame.mixer.Sound.play(lose_chant)
            pygame.display.flip()
            time.sleep(1)
            text_writing("Bust!!!!", 548, 0, 600, 200, largeText, WHITE, False)
            pygame.display.flip()
            time.sleep(2)
            bust = True
            values_to_zero()
            black_jack()


def hit_the_dealer():
    dealer_hits = 0
    global total_dealer_hits
    global dealer_value
    global total_value
    global placed_bet
    while dealer_hits == 0:
        new_dealer_card = random.randint(0, 51)
        dealer_value = dealer_value + cards_list[new_dealer_card].card_value()
        dealer_hits += 1
        total_dealer_hits += 1
    load_image('card' + str(new_dealer_card + 1) + '.png', (900 + total_dealer_hits * 130), 239, None, False)


def values_to_zero():
    global placed_bet
    global dealer_value
    global total_value
    global total_hits
    global no_instant_win
    global total_dealer_hits
    global black_jack_count
    global placed_da_bet
    global chips
    global cash
    total_dealer_hits = 0
    placed_bet = 0
    dealer_value = 0
    total_value = 0
    total_hits = 0
    no_instant_win = False
    black_jack_count = 0
    placed_da_bet = False
    chips = str(chips)
    cash = str(cash)


def sit():
    global dealer_value
    global chips
    global placed_bet
    global total_value
    global dealer_card_2
    load_image('card' + str(dealer_card_2 + 1) + '.png', 900, 239, 0, None, False)
    chips = int(chips)
    placed_bet = int(placed_bet)
    while dealer_value < 17:
        hit_the_dealer()
    if dealer_value >= 17:
        if dealer_value > 21:
            pygame.mixer.Sound.play(win_chant)
            pygame.display.flip()
            time.sleep(1)
            # (548, 0)
            text_writing("YOU WIN!!! CONGRATULATIONS!", 548, 0, 600, 200, largeText, WHITE, False)
            pygame.display.flip()
            time.sleep(3)
            chips = chips + placed_bet * 2
            values_to_zero()
        elif dealer_value == total_value:
            pygame.mixer.Sound.play(lose_chant)
            pygame.display.flip()
            time.sleep(1)
            text_writing("It's a tie, play again!", 548, 0, 600, 200, largeText, WHITE, False)
            pygame.display.flip()
            time.sleep(2)
            chips = chips + placed_bet
            values_to_zero()
        else:
            if dealer_value > total_value:
                pygame.mixer.Sound.play(lose_chant)
                pygame.display.flip()
                time.sleep(1)
                text_writing("Sorry, you lost", 548, 0, 600, 200, largeText, WHITE, False)
                pygame.display.flip()
                time.sleep(3)
                values_to_zero()
            else:
                pygame.mixer.Sound.play(win_chant)
                pygame.display.flip()
                time.sleep(1)
                text_writing("YOU WIN!!! CONGRATULATIONS!", 548, 0, 600, 200, largeText, WHITE, False)
                pygame.display.flip()
                time.sleep(3)
                chips = chips + placed_bet * 2
                values_to_zero()
    chips = str(chips)
    black_jack()


def double():
    global placed_bet
    global chips
    global bust
    if int(chips) - int(placed_bet) >= 0:
        chips = int(chips) - int(placed_bet)
        placed_bet = int(placed_bet)*2
    else:
        text_writing("Insufficent fund!!!!", 700, 300, 500, 300, smallText, WHITE, False, False)
    # (700 + int(500 / 2), 300 + int(300 / 2))
    text_writing("bet: " + str(placed_bet), 1570, 780, 350, 100, smallText, WHITE, True)
    text_writing("Chips: " + str(chips), 1570, 980, 350, 100, smallText, WHITE, True)
    hit_me()
    if not bust:
        sit()
    bust = False
    values_to_zero()


def instructions():
    load_image("instructions.jpg", 0, 0, 0, None)


def back_to_start():
    global lobby_counter
    lobby_counter = 0


# Events
while not Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = True
    # Buttons
    if lobby_counter == 0:
        welcome_screen()
        button("Go in", 800, 700, 300, 200, Dark_Green, GREEN, lobby)
        button("Close", 0, 900, 300, 200, Dark_RED, RED, quit_game)
        button("Instructions", 0, 600, 300, 200, Dark_white, WHITE, instructions)
    elif lobby_counter == 1:
        lobby()
        load_image("sign.png", 100, 650, 0, chip_shop, True)
        # button("Chip shop", 100, 700, 300, 200, Dark_white, WHITE, chip_shop)
        button("Go back", 0, 0, 300, 200, Dark_RED, RED, go_back)
        load_image("woman_table.png", 600,700, 0, black_jack, True)
        # button("Black Jack", 1388, 655, 300, 200, Dark_white, WHITE, black_jack)
    elif lobby_counter == 2:
        chip_shop()
        button("Go back", 0, 0, 300, 200, Dark_RED, RED, go_back)
        text_writing("$ for chips", 0, 900, 400, 200, smallText, WHITE, True)
        load_image("1chip.png", 400, 900, 10, cash_for_chips, True)
        load_image("2chip.png", 600, 900, 50, cash_for_chips, True)
        load_image("3chip.png", 800, 900, 100, cash_for_chips, True)
        load_image("4chip.png", 1000, 900, 1000, cash_for_chips, True)
        load_image("1money.png", 400, 700, 10, chips_for_cash, True)
        load_image("2money.png", 800, 700, 50, chips_for_cash, True)
        load_image("3money.png", 1200, 700, 100, chips_for_cash, True)
        load_image("4money.png", 1600, 700, 1000, chips_for_cash, True)
        text_writing("Chips for $", 0, 700, 400, 200, smallText, WHITE, True)
    elif lobby_counter == 3:
        button("Stand up", 0, 900, 300, 200, Dark_RED, RED, back_to_lobby)
        while black_jack_count < 1:
            black_jack()
            black_jack_count += 1
        text_writing("bet: " + str(placed_bet), 1570, 780, 350, 100, smallText, WHITE, True)
        if not placed_da_bet:
            button("1", 0, 650, 150, 100, Dark_white, WHITE, bet)
            button("10", 175, 650, 150, 100, Dark_white, WHITE, bet)
            button("100", 0, 800, 150, 100, Dark_white, WHITE, bet)
            button("1000", 175, 800, 150, 100, Dark_white, WHITE, bet)
        if int(placed_bet) > 0 and placed_da_bet is False:
            button("Place bet", 1570, 680, 350, 100, Dark_white, WHITE, start_game)
        if no_instant_win:
            button("Hit me!", 400, 980, 300, 100, Dark_white, WHITE, hit_me)
            button("Sit", 1100, 980, 300, 100, Dark_white, WHITE, sit)
            button("Double", 750, 980, 300, 100, Dark_white, WHITE, double)
    elif lobby_counter == 4:
        button("Go to lobby", 0, 900, 300, 200, Dark_RED, RED, back_to_start)
    text_writing("Cash: " + cash + "$", 1570, 880, 350, 100, smallText, WHITE, True)
    text_writing("Chips: " + chips, 1570, 980, 350, 100, smallText, WHITE, True)
    pygame.display.flip()
    clock.tick(REFRESH_RATE)