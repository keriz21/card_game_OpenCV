import cv2
import pygame
import sys
import numpy as np
import random

card_player = []
card_computer = []
card_temp = []

card_deck = [
    "as clubs",
    "as diamonds",
    "as hearts",
    "as spades",
    "delapan clubs",
    "delapan diamonds",
    "delapan hearts",
    "delapan spades",
    "lima clubs",
    "lima diamonds",
    "lima hearts",
    "lima spades",
    "empat clubs",
    "empat diamonds",
    "empat hearts",
    "empat spades",
    "jack clubs",
    "jack diamonds",
    "jack hearts",
    "jack spades",
    "joker",
    "king clubs",
    "king diamonds",
    "king hearts",
    "king spades",
    "sembilan clubs",
    "sembilan diamonds",
    "sembilan hearts",
    "sembilan spades",
    "queen clubs",
    "queen diamonds",
    "queen hearts",
    "queen spades",
    "tujuh clubs",
    "tujuh diamonds",
    "tujuh hearts",
    "tujuh spades",
    "enam clubs",
    "enam diamonds",
    "enam hearts",
    "enam spades",
    "sepuluh clubs",
    "sepuluh diamonds",
    "sepuluh hearts",
    "sepuluh spades",
    "tiga clubs",
    "tiga diamonds",
    "tiga hearts",
    "tiga spades",
    "dua clubs",
    "dua diamonds",
    "dua hearts",
    "dua spades"
]

card_table = []

input_player = None
input_computer = None
input_first = None

list_kartu = [
    "dua",
    "tiga",
    "empat",
    "lima",
    "enam",
    "tujuh",
    "delapan",
    "sembilan",
    "sepuluh",
    "jack",
    "queen",
    "king",
    "as"
]

def f_input_player(card):
    global input_player
    global input_computer
    global input_first
    if card == "" or card == input_computer or card == input_first:
        return
    
    if input_player == None:
        if card in card_player:
            input_player = card
            card_table.append(card)
            card_player.remove(card)
            print(f"input player adalah {card}")
        else:
            print("tidak valid")
    

def f_input_computer(card):
    global input_computer
    global input_first
    global input_player
    if card == "" or card == input_first or card == input_player:
        return
    if input_computer == None:
        if card in card_computer:
            input_computer = card
            card_table.append(card)
            card_computer.remove(card) 
            print(f"input computer adalah {card}")
        else:
            print("tidak valid")
        


def f_input_first(card):
    global input_first
    global input_player
    global input_computer

    if card == "" or card == input_first or card == input_computer:
        return
    if input_first == None and card in card_deck:
        input_first = card
        card_table.append(card)
        card_deck.remove(card)
        print(f"input first adalah {card}")
    return bool(input_first)

def f_input_full_first():
    global input_player, input_computer, input_first
    
    if all([input_player, input_computer, input_first]):
        return True
    else:
        return False
    
def f_input_full():
    global input_player, input_computer

    if all([input_player, input_computer]):
        return True
    else:
        return False

def reset_input():
    global input_player, input_computer, input_first
    input_player = None
    input_computer = None
    input_first = None

def reset_table():
    global card_table
    card_table = []

def add_card_player(card):
    if card == "":
        card_temp.clear()
        return
    
    if card in card_temp:
        card_temp.append(card)
    else:
        card_temp.clear()
        card_temp.append(card)

    if len(card_temp) > 10:
        # card_player.append(card)
        if card not in card_player and card not in card_computer and card in card_deck:
            card_player.append(card)
            card_deck.remove(card)

def add_card_computer(card):
    if card == "":
        card_temp.clear()
        return
    
    if card in card_temp:
        card_temp.append(card)
    else:
        card_temp.clear()
        card_temp.append(card)

    if len(card_temp) > 10:
        # card_player.append(card)
        if card not in card_player and card not in card_computer and card in card_deck:
            card_computer.append(card)

def add_card_computer_1():
    card = random.choice(card_deck)
    card_computer.append(card)
    card_deck.remove(card)
    pass


def tampilkan_data_kartu_player(data_kartu = card_player):
    latar = cv2.imread('Game/black.jpg')
    if data_kartu is None or len(data_kartu) == 0:
        return latar
    
    x_gambar = 0
    y_gambar = 0
    max = 2
    for item in data_kartu:
        img_kartu = cv2.imread(f'Game/dataGambar/{item}.png')
        if img_kartu is not None:
            x,y,w,h = x_gambar * 48, y_gambar * 60, 48, 60
            roi = latar[y:y+h, x:x+w]
            img_kartu = cv2.resize(img_kartu, (w,h))
            latar[y:y+h, x:x+w] = img_kartu
            x_gambar += 1
        
        if x_gambar == max:
            x_gambar = 0
            y_gambar += 1

    return latar

def tampilkan_data_kartu_komputer(data_kartu = card_computer):
    latar = cv2.imread('Game/black.jpg')
    if data_kartu is None or len(data_kartu) == 0:
        return latar
    
    x_gambar = 0
    y_gambar = 0
    max = 2
    for item in data_kartu:
        img_kartu = cv2.imread(f'Game/dataGambar/{item}.png')
        if img_kartu is not None:
            x,y,w,h = x_gambar * 48, y_gambar * 60, 48, 60
            roi = latar[y:y+h, x:x+w]
            img_kartu = cv2.resize(img_kartu, (w,h))
            latar[y:y+h, x:x+w] = img_kartu
            x_gambar += 1
        
        if x_gambar == max:
            x_gambar = 0
            y_gambar += 1

    return latar

def cek_winner():
    if not card_computer or not card_player:
        return True
    else:
        return False
    
def who_is_the_winner():
    global card_computer, card_player

    if not card_player and not card_computer:
        return "DRAW"
    elif not card_player:
        return "PLAYER WIN"
    elif not card_computer:
        return "COMPUTER WIN"
    
def pesan_sistem(text):
    hasil = cv2.imread('Game/black3.jpg')
    tinggi_gambar, lebar_gambar,_ = hasil.shape

    font = cv2.FONT_HERSHEY_SIMPLEX
    skala = 1
    warna = (255,255,255)
    ketebalan = 1

    ukuran_teks,_ = cv2.getTextSize(text, font, skala, ketebalan)

    x = (lebar_gambar -  ukuran_teks[0]) // 2
    y = 40

    cv2.putText(hasil, text, (x,y), font, skala, warna, ketebalan)

    return hasil


def tampilkan_data_kartu_meja(data_kartu=card_table):
    hasil = cv2.imread('Game/meja.jpg')
    if data_kartu is None or len(data_kartu) == 0:
        return hasil
    
    lebar_meja = hasil.shape[1]  # Mengambil lebar gambar meja

    jumlah_kartu = len(data_kartu)
    lebar_kartu, tinggi_kartu = 48, 60

    x = 390
    y, w, h = 0, lebar_kartu, tinggi_kartu

    for item in data_kartu:
        img_kartu = cv2.imread(f'Game/dataGambar/{item}.png')
        if img_kartu is not None:
            roi = hasil[y:y+h, x:x+w]
            img_kartu = cv2.resize(img_kartu, (w, h))
            hasil[y:y+h, x:x+w] = img_kartu
            x += lebar_kartu
    return hasil