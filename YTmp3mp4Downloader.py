
print('''
Github: https://github.com/msfraish or https://github.com/fraishmsa
2022 All rights reversed to the programmer's name below:
  __  __       _         _         ______         _     _     
 |  \/  |     | |       | |       |  ____|       (_)   | |    
 | \  / | __ _| |__   __| |_   _  | |__ _ __ __ _ _ ___| |__  
 | |\/| |/ _` | '_ \ / _` | | | | |  __| '__/ _` | / __| '_ \ 
 | |  | | (_| | | | | (_| | |_| | | |  | | | (_| | \__ \ | | |
 |_|  |_|\__,_|_| |_|\__,_|\__, | |_|  |_|  \__,_|_|___/_| |_|
                            __/ |                             
                           |___/                              
Script Version: v0.1 beta
Program under GNU General Public License v3.0
''')

'''
Upcoming updates:

Adding download multiple videos at once.
Adding download playlists.
Adding download all channel videos at once.
Adding more options when downloading such as video quality resulotion
Adding verification of the link entry.
'''

# Importing the modules
from time import sleep
from pytube import YouTube 
import tkinter as tk
from tkinter import filedialog
import os

# Loading GUI for directory dialog
root = tk.Tk()
root.withdraw()

# Asking user to choose directory to save files at
print('Please enter where do you want to save the file at: Please wait 2 secs.\n')

# Wait 2 secs
sleep(2)

# Show dialog for directory selection
dic_path = filedialog.askdirectory()

# Where to save 
SAVE_PATH = dic_path

# Asking user to enter url video want to be downloaded
print('Please enter the url of the YouTube video that you want to download: \n')

# Link of the channel videos to be downloaded
link = input()

try: 
    # Object creation using YouTube
    # Which was imported in the beginning 
    yt = YouTube(link) 
except: 
    print("Connection Error") # To handle exception 
  
# Asking user to choose what type of file he want
print('Please Choose File Type mp3 or mp4: \n')
filetype = input()

# To change the extention for the downloaded file from mp4 to mp3
path = SAVE_PATH
def renamefile():
    for filename in os.listdir(path):
        if filename.endswith("mp4"):
            os.rename(os.path.join(path, filename), os.path.join(path, filename.replace("mp4", "mp3")))
        else:
            continue

try: 
        # downloading the song
    if filetype == 'mp3':
        yt.streams.filter(only_audio=True).first().download(SAVE_PATH)
        renamefile()
        # downloading the video 
    elif filetype == 'mp4':
        yt.streams.filter(file_extension='mp4').first().download(SAVE_PATH)
    else:
        print('Somthing went wrong!')
except: 
    print("Some Error!") 
print('Download Completed!') 