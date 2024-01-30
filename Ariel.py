from pytube import YouTube
from youtube_search import YoutubeSearch
import os
from pyigdl import IGDownloader


LIST_MUSICS = []
local = fr'C:\Users\{os.getlogin()}\Downloads'
def HEAD():
    os.system('cls')
    print('''
         _      ____    ___   _____   _     
        / \    |  _ \  |_ _| | ____| | |    
       / _ \   | |_) |  | |  |  _|   | |    
      / ___ \  |  _ <   | |  | |___  | |___ 
     /_/   \_\ |_| \_\ |___| |_____| |_____|
    ''')
    inicio()




def music_downloader():
    print('''
    -- Módulo de download de músicas --
    Selecione a opção desejada:
    [1] Para realizar o download
    [2] Para começar a adicionar as músicas
    [3] Para voltar ao menu principal
    [4] Para Mostrar músicas que seram baixadas
    [5] Para limpar a lista de músicas INTEIRA
    ''')

    i = int(input('Opção Desejada: '))

    if i == 1:
        if LIST_MUSICS:
            for music in LIST_MUSICS:
                if 'https://' in music:
                    try:
                        video = YouTube(music,use_oauth=True, allow_oauth_cache=False)
                        stream = video.streams.filter(only_audio=True, abr='320kbps').first()
                        stream.download(local,
                                        filename=f"{video.title}.mp3")  # caminho do diretorio para download
                        print(f"A musica {video.title} foi baixado")
                        inicio()
                    except:
                        print(f'A musica {video.title} não foi baixada.')
                        inicio()

            else:
                results = YoutubeSearch(music, max_results=1).to_dict()
                try:
                    url = 'youtube.com' + results[0]['url_suffix']
                    video = YouTube(url,use_oauth=True, allow_oauth_cache=False)
                    stream = video.streams.filter(only_audio=True, abr='320kbps').first()
                    stream.download(local,
                                    filename=f"{video.title}.mp3")  # caminho do diretorio para download
                    print(f"A musica {video.title} foi baixado")
                    inicio()

                except:
                    print(f'A musica {video.title} não foi baixada.')
                    inicio()
        else:
            print('A lista de músicas está vazia!')
            music_downloader()

    elif i == 2:
        while True:
            nome = input('Nome da música/Link do youtube/Opção Desejada: ')

            if nome == '1':
                for music in LIST_MUSICS:
                    if 'https://' in music:
                        try:
                            video = YouTube(music)
                            stream = video.streams.filter(only_audio=True).first()
                            stream.download(fr'C:\Users\{os.getlogin()}\Downloads', filename=f"{video.title}.mp3")  # caminho do diretorio para download
                            print(f"A musica {video.title} foi baixado")
                            inicio()
                        except Exception as e:
                            print(e)
                            print(f'A musica {music} não foi baixada.')
                            inicio()

                    else:
                        results = YoutubeSearch(music, max_results=1).to_dict()
                        try:
                            url = 'youtube.com' + results[0]['url_suffix']
                            video = YouTube(url)
                            stream = video.streams.filter(only_audio=True).first()
                            stream.download(fr'C:\Users\{os.getlogin()}\Downloads', filename=f"{video.title}.mp3")  # caminho do diretorio para download
                            print(f"A musica {video.title} foi baixado")
                            inicio()

                        except Exception as e:
                            print(e)
                            print(f'A musica {music} não foi baixada.')
                            inicio()
                break

            elif nome == '3':
                HEAD()

            elif nome == '4':
                if LIST_MUSICS:
                    for musica in LIST_MUSICS:
                        print(musica)
                else:
                    print('A lista de músicas está vazia')


            elif nome == '5':
                if LIST_MUSICS:
                    LIST_MUSICS.clear()
                    print('A lista de músicas está vazia')
                    music_downloader()
                else:
                    print('A lista já está vazia')
                    music_downloader()

            else:
                LIST_MUSICS.append(nome)
    elif i == 3:
        HEAD()

    elif i == 4:
        if LIST_MUSICS:
            for musica in LIST_MUSICS:
                print(musica)
        else:
            print('A lista de músicas está vazia')
            music_downloader()

    elif i == 5:
        if LIST_MUSICS:
            LIST_MUSICS.clear()
            print('A lista de músicas está vazia')
            music_downloader()
        else:
            print('A lista já está vazia')
            music_downloader()

def reel_download():
    while True:
        print('Digite "1" para voltar ao menu principal')
        data = input('Link do Reel/Opção Desejada: ')
        print('\n')
        if data == '1':
            HEAD()
        else:
            data = IGDownloader(data)
            link = data[0]["download_link"]
            os.system(f'start {link}')


def inicio():
    print('''
    Selecione a opção desejada:
    [1] Onde será salvo os arquivos
    [2] Baixador de músicas
    [3] Baixador de Reels do Instagram
    \n''')
    i = int(input('Opção Desejada: '))
    if i == 1:
        print('Local de Download padrão é "Downloads"')
        local = input('Indique o novo local de Download: ')
        print(f'Novo local de Download: {local}')
        inicio()

    elif i == 2:
        music_downloader()

    elif i == 3:
        reel_download()

HEAD()



