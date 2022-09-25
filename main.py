

from tkinter import *
from tkinter import messagebox, filedialog
from pytube import YouTube

import os


dir_name = os.getcwd()


FG_COLOR = "#2C4B57"
BG_COLOR = "#D4FFDF"
BTN_COLOR = "#52B36A"


def create_widget():


    link_label = Label(root, text="Youtube URL: ", bg=BG_COLOR)
    link_label.grid(row=1, column=0, pady=10, padx=1)

    root.link_text = Entry(root, width=60, textvariable=video_link)
    root.link_text.grid(row=1, column=1, pady=5, padx=5)

    destination_label = Label(root, text="Destination: ", bg=BG_COLOR)
    destination_label.grid(row=2, column=0, pady=5,  padx=5)

    root.destination_text = Entry(root, width=60, textvariable=download_path)
    root.destination_text.grid(row=2, column=1, pady=5, padx=5)    

    browse_btn = Button(root, text="Browse", command=browse, width=10, bg=BTN_COLOR)
    browse_btn.grid(row=2, column=2, pady=1, padx=1)

    audio_option = Radiobutton(root, text="Download video", variable=media_option, value=0, bg=BG_COLOR)
    audio_option.grid(row=3, column=0, pady=10, padx=10)

    video_option = Radiobutton(root, text="Download audio only", variable=media_option, value=1, bg=BG_COLOR)
    video_option.grid(row=3, column=1, sticky='w', pady=10, padx=10)



    download_btn = Button(root, text="Download", width=10, bg=BTN_COLOR, command=download_media)
    download_btn.grid(row=4, column=1, pady=4, padx=4)



    

def download_media():
    
    if media_option.get():
        download_audio()
    else:
        download_video()
        



def browse():
    download_dir = filedialog.askdirectory(initialdir=dir_name)
    download_path.set(download_dir)


def download_video():
    try:
        url = video_link.get()
        folder = download_path.get()

        video = YouTube(url)
        video.streams.get_highest_resolution().download(output_path=folder)
        messagebox.showinfo("Success!", "Download finished, your video is at "+folder)
    
    except:
        messagebox.showinfo("Error!", "Error downloading your video")  


def download_audio():
    try:
        url = video_link.get()
        folder = download_path.get()

        audio = YouTube(url)
        audio.streams.get_audio_only().download(output_path=folder)
        convert_to_mp3(audio, folder)
        messagebox.showinfo("Success!", "Download finished, your audio is at "+folder)
        
    
    except:
        messagebox.showinfo("Error!", "Error downloading your audio")  




def convert_to_mp3(audio, folder):
    """
    The conversion isn't exactly a conversion, this function is just replacing the extension '.mp4' for '.mp3'. Pytube gets has its methods to get only the audio, but the file is saved as a '.mp4' file.
    """
    name = remove_characters(audio.title)
    old_name = folder + '/' + name + '.mp4'
    new_name = folder + '/' + name + '.mp3'
    os.rename(old_name, new_name)

 


def remove_characters(name):
    """
    When saving the file, some medias with characters such as commas and periods in the title were being saved without these characters in the filename, to rename the files we have to remove these characters from the string that stores the title of the media
    """

    name = name.replace(',', '')
    name = name.replace('.', '')
    name = name.replace("'","")
    name = name.replace(':', '')
    name = name.replace('|', '')
    return name





root = Tk()

root.geometry("800x200")
root.resizable(False, False)
root.title("YouTube Downloader")
root.config(background=BG_COLOR)


video_link = StringVar()
download_path = StringVar()
media_option = IntVar()

create_widget()

root.mainloop()





