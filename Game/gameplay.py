import cv2
import numpy
from imgProcessing import contour4 as ctr
from imgProcessing import img

from Game import data

kondisi = 0
'''
    0 : inisiasi game
    1 : putaran pertama game
    2 : compare pertama game
    3 : putaran pemain vs komputer
    4 : putaran komputer vs pemain
    5 : compare pemain vs komputer
    6 : compare komputer vs pemain
    7 : cek siapa pemenangnya
'''



putaran = 1

def init(card):
    msg = ""
    global kondisi
    if len(data.card_player) <= 4:
        data.add_card_player(card)
        msg = "Masukkan Kartu Pemain"
    elif len(data.card_computer) <= 4:
        data.add_card_computer(card)
        # data.add_card_computer_1()
        msg = "Masukkan Kartu Computer"
    else:
        msg = "Input kartu sudah selesai"
        kondisi = 1

    return msg

def first_game(card, card2):
    msg = ""
    global kondisi
    if not data.input_first:
        msg = "Silahkan masukkan kartu untuk pertama kali"
        data.f_input_first(card)
    elif not data.input_player:
        msg = "Silahkan masukkan kartu pemain"
        data.f_input_player(card)
        if card2 != "":
            data.add_card_player(card2)
    elif not data.input_computer:
        msg = "silahkan masukkan kartu komputer"
        data.f_input_computer(card)
        if card2 != "":
            data.add_card_computer(card2)
    
    if data.f_input_full_first():
        kondisi = 2

    return msg

def first_compare():
    global putaran
    global kondisi

    bandar = str(data.input_first).split()
    pemain = str(data.input_player).split()
    computer = str(data.input_computer).split()

    # Pastikan panjang pemain, bandar, dan computer cukup
    if len(pemain) >= 2 and len(bandar) >= 2:
        if pemain[1] == bandar[1]:
            max = data.list_kartu.index(pemain[0])
            winner = "pemain"

    if len(computer) >= 2 and len(bandar) >= 2:
        if computer[1] == bandar[1]:
            angka = data.list_kartu.index(computer[0])

            if angka > max:
                winner = "computer"

    if winner == "pemain":
        kondisi = 3
    elif winner == "computer":
        kondisi = 4

    print(f"pemengangnya adalah {winner}")
    putaran += 1
    data.reset_input()
    data.reset_table()


def comVsPly(card, card2):
    msg = ""
    global kondisi
    if not data.input_computer:
        msg = "silahkan masukkan kartu komputer"
        data.f_input_computer(card)
        if card2 != "":
            data.add_card_computer(card2)
    elif not data.input_player:
        data.f_input_player(card)
        msg = "Silahkan masukkan kartu pemain"
        if card2 != "":
            data.add_card_player(card2)
    
    if data.f_input_full():
        kondisi = 6

    return msg

def plyVsCom(card, card2):
    msg = ""
    global kondisi
    if not data.input_player:
        data.f_input_player(card)
        msg = "Silahkan masukkan kartu pemain"
        if card2 != "":
            data.add_card_player(card2)
    elif not data.input_computer:
        msg = "silahkan masukkan kartu komputer"
        data.f_input_computer(card)
        if card2 != "":
            data.add_card_computer(card2)
    
    if data.f_input_full():
        kondisi = 5

    return msg

def compare_comVsPly():
    global kondisi
    global putaran

    pemain = str(data.input_player).split()
    computer = str(data.input_computer).split()

    winner = ""
    max = 0

    if pemain[1] != computer[1]:
        winner = "computer"
    else:
        max = data.list_kartu.index(computer[0])

    angka = data.list_kartu.index(pemain[0])
    if angka > max:
       winner = "pemain"
    else:
        winner = "computer"

    if winner == "pemain":
        kondisi = 3
    elif winner == "computer":
        kondisi = 4

    if(data.cek_winner()):
        kondisi = 7

    putaran += 1
    data.reset_input()
    data.reset_table()

def compare_plyVsCom():
    global kondisi
    global putaran

    pemain = str(data.input_player).split()
    computer = str(data.input_computer).split()

    winner = ""
    max = 0

    if pemain[1] != computer[1]:
        winner = "pemain"
    else:
        max = data.list_kartu.index(pemain[0])

    angka = data.list_kartu.index(computer[0])
    if angka > max:
       winner = "computer"
    else:
        winner = "pemain"

    if winner == "pemain":
        kondisi = 3
    elif winner == "computer":
        kondisi = 4

    if(data.cek_winner()):
        kondisi = 7

    putaran += 1
    data.reset_input()
    data.reset_table()

def mainkan(frame):
    cropped = img.crop_center(frame)
    filter = img.filter(frame)

    pesan = ""
    pemenang = ""
    #area draw kartu
    kontur,_ = ctr.find_four_sided_contours(filter, cropped,(0,480),True)
    kontur1, kartu_text1 = ctr.find_four_sided_contours(filter, cropped,(0,240))
    kontur2, kartu_text2 = ctr.find_four_sided_contours(filter,cropped,(240,480))
    if kondisi == 0:
        pesan = init(kartu_text1)
    elif kondisi == 1:
        pesan = first_game(kartu_text2, kartu_text1)
    elif kondisi == 2:
        first_compare()
    elif kondisi == 3:
        pesan = plyVsCom(kartu_text2, kartu_text1)
    elif kondisi == 4:
        pesan = comVsPly(kartu_text2, kartu_text1)
    elif kondisi == 5:
        compare_plyVsCom()
    elif kondisi == 6:
        compare_comVsPly()
    elif kondisi == 7:
        pesan = data.who_is_the_winner()

    tag_meja = data.tampilkan_data_kartu_meja(data.card_table)
    pemain_kartu =  data.tampilkan_data_kartu_player()
    komputer_kartu = data.tampilkan_data_kartu_komputer()

    print(kondisi)

    tag_player = cv2.imread('Game/PLAYER.jpg')
    tag_komputer = cv2.imread('Game/komputer1.jpg')
    tag_pesan = data.pesan_sistem(pesan)

    cv2.line(kontur, (240, 0), (240, 360), (255,0,255), thickness=2)
    # cv2.putText(kontur,pesan,(10,350), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(kontur,str(putaran),(440,40),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

    gabung = cv2.hconcat([pemain_kartu, tag_player, kontur, tag_komputer, komputer_kartu])
    gabung = cv2.vconcat([tag_pesan,gabung,tag_meja])
    cv2.imshow('kontur123', gabung)
    

    pass