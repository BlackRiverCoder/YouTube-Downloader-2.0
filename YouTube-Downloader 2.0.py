import youtube_dl
import time
import os
import sys
import colorama
from colorama import Fore, Back, Style

#Options:
formats = ("1. mp3\n2. mp4")
format_default = '.mp4'
folders = ("1. Desktop\n2. Downloads\n3. Music\n4. Documents\n5. Videos")
folder_default = '~/Desktop/%(title)s.%(ext)s'

#Functions:
def loading():
    print("Loading")
    time.sleep(0.2)
    os.system('cls||clear')
    print("Loading.")
    time.sleep(0.2)
    os.system('cls||clear')
    print("Loading..")
    time.sleep(0.2)
    os.system('cls||clear')
    print("Loading...")
    time.sleep(0.2)
    os.system('cls||clear')
    print("Loading....")
    time.sleep(0.2)
    os.system('cls||clear')
    print("Loading.....")
    time.sleep(0.2)
    print(Fore.LIGHTGREEN_EX + 'Loaded successfully!')
    time.sleep(1)
    os.system('cls||clear')

loading()


#Fromat selection:
print(Fore.WHITE + "Please select format to download YouTube files:")
time.sleep(0.5)

print(formats)

format_choose = input(Fore.LIGHTRED_EX + "Your option:")
if format_choose == "1":
    format_ = '.mp3'
    os.system('cls||clear')

elif format_choose == "2":
    format_ = '.mp4'
    os.system('cls||clear')

else:
    format_ = format_default
    os.system('cls||clear')


#Direction selection:
print(Fore.WHITE + "Please select the folder where the file should be downloaded")
time.sleep(0.5)

print(folders)

folder_choose = input(Fore.LIGHTRED_EX + "Your option:")
if folder_choose == "1":
    folder_ = '~/Desktop/%(title)s.%(ext)s'
    os.system('cls||clear')

elif folder_choose == "2":
    folder_ = '~/Downloads/%(title)s.%(ext)s'
    os.system('cls||clear')

elif folder_choose == "3":
    folder_ = '~/Music/%(title)s.%(ext)s'
    os.system('cls||clear')

elif folder_choose == "4":
    folder_ = '~/Documents/%(title)s.%(ext)s'
    os.system('cls||clear')

elif folder_choose == "5":
    folder_ = '~/Videos/%(title)s.%(ext)s'
    os.system('cls||clear')

else:
    folder_ = folder_default
    os.system('cls||clear')


#Main code:
while(True):
    question = input(Fore.WHITE + "If you want to start press ENTER, if you want to exit please type 'END' or 'EXIT'\n")
    if question == "":
        if format_ == '.mp3':
            video_url = input(Fore.LIGHTBLUE_EX + "Please enter youtube video url:")
            video_info = youtube_dl.YoutubeDL().extract_info(
                url = video_url, download=False
            )
            filename = f"{video_info['title']}" + format_
            options={
                'format':'bestaudio/best',
                'keepvideo':'False',
                'outtmpl':folder_,
            }

            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([video_info['webpage_url']])

            os.system('cls||clear')
            print(Fore.LIGHTGREEN_EX + "Download complete... {}".format(filename))

        elif format_ == '.mp4':
            video_url = input(Fore.LIGHTBLUE_EX + "Please enter youtube video url:")
            video_info = youtube_dl.YoutubeDL().extract_info(
                url = video_url, download=False
            )
            filename = f"{video_info['title']}" + format_
            options={
                'format':'bestvideo/best',
                'keepvideo':'True',
                'outtmpl':folder_,
            }

            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([video_info['webpage_url']])

            os.system('cls||clear')
            print(Fore.LIGHTGREEN_EX + "Download complete... {}".format(filename))

    else:
        print(Fore.LIGHTYELLOW_EX + "Thanks for using YouTube Downloader 2.0")
        time.sleep(3)
        os.system('cls||clear')
        sys.exit()




