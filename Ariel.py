from pytube import YouTube
from youtube_search import YoutubeSearch
import os
from pyigdl import IGDownloader
import colorama
from colorama import Fore, Style

user = os.getlogin()
colorama.init()
LIST_MUSICS = []
local = fr'C:/Users/{user}/Downloads'
def HEAD():
    os.system('cls')
    print(f'''{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}
         _      ____    ___   _____   _     
        / \    |  _ \  |_ _| | ____| | |    
       / _ \   | |_) |  | |  |  _|   | |    
      / ___ \  |  _ <   | |  | |___  | |___ 
     /_/   \_\ |_| \_\ |___| |_____| |_____|
    {Style.NORMAL}{Fore.WHITE}''')
    inicio()


def YTdownloader():
    if LIST_MUSICS:
        for music in LIST_MUSICS:
            if 'https://' in music:
                try:
                    video = YouTube(music, use_oauth=True, allow_oauth_cache=False)
                    stream = video.streams.filter(only_audio=True).order_by('abr').desc()
                    stream.download(local, filename=f"{video.title}.mp3")  # caminho do diretorio para download
                    print(f"{video.title} {Fore.LIGHTGREEN_EX}{Style.BRIGHT}SUCESSO.{Fore.WHITE}{Style.NORMAL}")
                    inicio()
                except:
                    print(f'{video.title} {Fore.RED}{Style.BRIGHT}FALHOU.{Fore.WHITE}{Style.NORMAL}')
                    inicio()

            else:
                results = YoutubeSearch(music, max_results=1).to_dict()
                try:
                    url = 'youtube.com' + results[0]['url_suffix']
                    video = YouTube(url, use_oauth=True, allow_oauth_cache=False)
                    stream = video.streams.filter(only_audio=True).order_by('abr').desc()
                    stream.download(local, filename=f"{video.title}.mp3")  # caminho do diretorio para download
                    print(f'{video.title} {Fore.RED}{Style.BRIGHT}FALHOU.{Fore.WHITE}{Style.NORMAL}')
                    inicio()
                except:
                    print(f'{video.title} {Fore.RED}{Style.BRIGHT}FALHOU.{Fore.WHITE}{Style.NORMAL}')
                    inicio()
    else:
        print(f'{Style.BRIGHT}A lista de músicas está vazia!{Style.NORMAL}')
        music_downloader()


def music_downloader():
    print(f'''
    {Style.BRIGHT}-- Módulo de download de músicas --{Style.NORMAL}
    [1] Realizar o download
    [2] Começar a adicionar as músicas
    [3] Retornar ao menu principal
    [4] Lista de músicas adicionadas
    [5] Limpar lista de músicas INTEIRA
    ''')
    i = input('Opção Desejada: ')
    if i == '1':
        YTdownloader()
    elif i == '2':
        while True:
            nome = input(f'{Fore.LIGHTMAGENTA_EX}Nome da música{Fore.WHITE}/{Fore.YELLOW}Link do youtube{Fore.WHITE}/{Fore.CYAN}Opção Desejada{Fore.WHITE}: ')
            if nome == '1':
                YTdownloader()
                break
            elif nome == '3':
                HEAD()
                break
            elif nome == '4':
                if LIST_MUSICS:
                    for musica in LIST_MUSICS:
                        print(musica)
                else:
                    print(f'{Style.BRIGHT}A lista de músicas está vazia!{Style.NORMAL}')
            elif nome == '5':
                if LIST_MUSICS:
                    LIST_MUSICS.clear()
                    print('A lista de músicas foi esvaziada')
                    music_downloader()
                else:
                    print('A lista já está vazia')
                    music_downloader()
            else:
                LIST_MUSICS.append(nome)
    elif i == '3':
        HEAD()
    elif i == '4':
        if LIST_MUSICS:
            for musica in LIST_MUSICS:
                print(musica)
        else:
            print(f'{Style.BRIGHT}A lista de músicas está vazia{Style.NORMAL}')
            music_downloader()
    elif i == '5':
        if LIST_MUSICS:
            LIST_MUSICS.clear()
            print(f'{Style.BRIGHT}A lista de músicas foi esvaziada{Style.NORMAL}')
            music_downloader()
        else:
            print(f'{Style.BRIGHT}A lista já está vazia{Style.NORMAL}')
            music_downloader()
    else:
        print(f'Comando: {i} {Fore.RED}Invalido{Fore.WHITE}')
        music_downloader()

def reel_download():
    while True:
        print('Digite "1" para voltar ao menu principal')
        data = input(f'{Fore.YELLOW}Link do Reel{Fore.WHITE}/{Fore.CYAN}Opção Desejada{Fore.WHITE}: ')
        if data == '1':
            HEAD()
        else:
            data = IGDownloader(data)
            link = data[0]["download_link"]
            os.system(f'start {link}')


def inicio():
    print(f'''
    {Style.BRIGHT}--Selecione a opção desejada--{Style.NORMAL}
    [1] Onde será salvo os arquivos
    [2] Baixador de músicas
    [3] Baixador de Reels do Instagram\n''')
    i = input('Opção Desejada: ')
    if i == '1':
        localDownload()
    elif i == '2':
        music_downloader()
    elif i == '3':
        reel_download()
    else:
        print(f'Comando: {i} {Fore.RED}Invalido{Fore.WHITE}')
        inicio()


def localDownload():
    global local
    print('Local de Download padrão é "Downloads"')
    local = input('Indique o novo local de Download: ')
    if local:
        print(f'{Style.BRIGHT}{Fore.LIGHTBLUE_EX}Novo local de Download: {local}{Fore.WHITE}{Style.NORMAL}')
    else:
        local = fr'C:/Users/{user}/Downloads'
        print(f'{Style.BRIGHT}{Fore.LIGHTBLUE_EX}O local do download é: {local}{Fore.WHITE}{Style.NORMAL}')
    inicio()


HEAD()



