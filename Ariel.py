import PySimpleGUI as sg
import pyautogui as pa
from pytube import YouTube
from youtube_search import YoutubeSearch
import os

sg.theme('Dark Blue')
layout = [
    [sg.Text("ARIEL", size=(0, 2), font=('arial', 33), pad=(195, 0))],
    [sg.Input(pad=(23, 0), size=(30, 1), font=('arial', 20))],
    [sg.Button('Add', size=(7, 1), pad=(80, 2), font=('hervitica', 20), button_color='#6bd15b'),
     sg.Button('Remove', pad=(30, 0), size=(7, 1), font=('hervitica', 20), button_color='#E93D3D')],
    [sg.Button('Show list', size=(10, 1), pad=(170, 5), font=('hervitica', 20), button_color='#3D96E9')],
    [sg.Button('Download', size=(10, 1), pad=(170, 5), font=('hervitica', 20), button_color='white')],
]

window = sg.Window('Ariel', layout, icon='ARIEL.ico')
LIST_MUSICS = []

while True:
    event, values = window.read()
    print(event, values)

    if event == 'Download':
        results = YoutubeSearch(LIST_MUSICS[0], max_results=1).to_dict()
        titulo = results[0]['title']
        author = results[0]['channel']
        duration = results[0]['duration']
        url = 'youtube.com' + results[0]['url_suffix']

    #CONFIRMATION=======================
        l = [
            [sg.Text(text='Do you wanna Continue?', size=(20,2), font=('arial', 30))],
            [sg.Button('Yes', size=(6,1), pad=(90, 2), font=('hervitica', 15), button_color='#6bd15b'),
             sg.Button('No', size=(6,1), pad=(35, 0),font=('hervitica', 15), button_color='#E93D3D')],
        ]
        win = sg.Window('Confirmation', l, icon='ARIEL.ico')
        while True:
            event, values = win.read()
            if event == 'No':
                quit()

            elif event == 'Yes':
                for music in LIST_MUSICS:
                    results = YoutubeSearch(music, max_results=1).to_dict()
                    url = 'youtube.com' + results[0]['url_suffix']
                    video = YouTube(url)
                    stream = video.streams.filter(only_audio=True).first()
                    stream.download(fr'C:\Users\{os.getlogin()}\Downloads',filename=f"{video.title}.mp3")
                    #my_video.download('~/Downloads')
                    pa.alert(text=f"A musica {video.title} foi baixado")
                    quit()

    elif event == 'Add':
        nome = values[0]
        LIST_MUSICS.append(nome)
        print(LIST_MUSICS)

    elif event == 'Remove':
        nome = values[0]
        LIST_MUSICS.remove(nome)
        print(LIST_MUSICS)

    elif event == 'Show list':
        pa.alert(text=LIST_MUSICS, title='Ariel')
        print(LIST_MUSICS)


    elif event == None:
        break

