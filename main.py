
from datetime import date
from tkinter import *
from tkinter import messagebox, filedialog
from pytube import YouTube, Playlist
import os



FG_COLOR = "#2068F7"
ACTIVE_BG_RADIOS = "#ffc16c"
BG_COLOR = '#ffce89'
BTN_COLOR = "#2068F7"
ACTIVE_BG_BTN = '#2045F7'




class App(Tk):
    def __init__(self):
        super().__init__()

        self.initial_dir = self.get_initial_dir()


        self.resizable(False, False)
        self.center_window(750,300)

        self.title("YouTube Downloader")
        self.config(background=BG_COLOR)

        self.download_url = StringVar(master=self)
        self.download_path = StringVar(master=self)
        self.download_path.set(self.initial_dir)

        self.media_option = IntVar(master=self)

   

        self.link_label = Label(self,
                                text="URL: ",
                                bg=BG_COLOR)
        
        self.link_label.grid(row=1,column=0,pady=10,padx=1)



        self.url_entry = Entry(self,
                               highlightthickness=0,
                               width=60,
                               textvariable=self.download_url)
        
        self.url_entry.grid(row=1,column=1,pady=5,padx=5)


        
        self.clear_btn = Button(self,
                                activebackground=ACTIVE_BG_BTN,
                                highlightthickness=0,
                                text="Clear",
                                command=self.clear_url_entry,
                                width=10,
                                bg=BTN_COLOR)

        self.clear_btn.grid(row=1,column=2,pady=1,padx=1)

    

        self.destination_label = Label(self,
                                       text="Destination: ",
                                       bg=BG_COLOR)
        
        self.destination_label.grid(row=2,column=0,pady=5,padx=5)



        self.destination_text = Entry(self,
                                      highlightthickness=0,
                                      width=60,
                                      textvariable=self.download_path)
        
        self.destination_text.grid(row=2,column=1,pady=5,padx=5)    

        self.browse_btn = Button(self,
                                 activebackground=ACTIVE_BG_BTN,
                                 highlightthickness=0,
                                 text="Browse",
                                 command=self.browse,
                                 width=10,
                                 bg=BTN_COLOR)
        
        self.browse_btn.grid(row=2,column=2,pady=1,padx=1)



        self.audio_option = Radiobutton(self,
                                        activebackground=ACTIVE_BG_RADIOS,
                                        highlightthickness=0,
                                        text="Download audio",
                                        variable=self.media_option,
                                        value=0,
                                        bg=BG_COLOR)
        
        self.audio_option.grid(row=3,column=1,sticky='w',pady=10,padx=10)



        self.video_option = Radiobutton(self,
                                        activebackground=ACTIVE_BG_RADIOS,
                                        highlightthickness=0,
                                        text="Download video",
                                        variable=self.media_option,
                                        value=1, bg=BG_COLOR)
        
        self.video_option.grid(row=4,column=1,sticky='w',pady=10,padx=10)



        self.playlist_audio_option = Radiobutton(self,
                                                 activebackground=ACTIVE_BG_RADIOS,
                                                 highlightthickness=0,
                                                 text="Download an audio playlist",
                                                 variable=self.media_option,
                                                 value=2,
                                                 bg=BG_COLOR)
        
        self.playlist_audio_option.grid(row=5,column=1,sticky='w',pady=10,padx=10)



        self.playlist_video_option = Radiobutton(self,
                                                 activebackground=ACTIVE_BG_RADIOS,
                                                 highlightthickness=0,
                                                 text="Download a video playlist",
                                                 variable=self.media_option,
                                                 value=3,
                                                 bg=BG_COLOR)
        
        self.playlist_video_option.grid(row=6,column=1,sticky='w',pady=10,padx=10)



        self.download_btn = Button(self,
                                   activebackground=ACTIVE_BG_BTN,
                                   highlightthickness=0, text="Download",
                                   width=10, bg=BTN_COLOR,
                                   command=self.download)
        
        self.download_btn.grid(row=7,column=1,pady=4,padx=4)

    


    def center_window(self, width, height):
        width_screen = self.winfo_screenwidth()
        height_screen = self.winfo_screenheight()
        x = (width_screen/2) - (width/2)
        y = (height_screen/2) - (height/2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))


    def clear_url_entry(self):
        self.download_url.set('')




    def browse(self):
        download_dir = filedialog.askdirectory(initialdir=self.initial_dir)
        self.download_path.set(download_dir)


    def download(self):
        pass
        
        if self.media_option.get() == 0:
            self.download_audio()

        elif self.media_option.get() == 1:
            self.download_video()

        elif self.media_option.get() == 2:
            self.download_audio_playlist()

        elif self.media_option.get() == 3:
            self.download_video_playlist()

        else:
            print("Erro")


    def download_video(self):
        pass
        try:
            url = self.download_url.get()
            folder = self.download_path.get()

            video = YouTube(url)
            video.streams.get_highest_resolution().download(output_path=folder)
            messagebox.showinfo("Success!", "Download finished, your video is at "+folder)
        
        except:
            messagebox.showinfo("Error!", "Error downloading your video")  


    def download_audio(self):
        pass
        try:
            url = self.download_url.get()
            folder = self.download_path.get()

            audio = YouTube(url)
            file = audio.streams.get_audio_only().download(output_path=folder)
            self.change_extension_to_mp3(file)
            messagebox.showinfo("Success!", "Download finished, your audio is at "+folder)
            
        
        except:
            messagebox.showinfo("Error!", "Error downloading your audio")  
            

    def download_video_playlist(self):
        try:
            url_playlist = self.download_url.get()
            p = Playlist(url_playlist)
            folder = self.playlists_download_dir(p.title)
            
            for url in p.video_urls:

                try:
                    yt = YouTube(url)
                    yt.streams.get_highest_resolution().download(output_path=folder)
                except:
                    pass

            messagebox.showinfo("Success!", "Download finished, your playlist is at "+folder)


        except:
            messagebox.showinfo("Error!", "Error downloading your playlist")



    def download_audio_playlist(self):
        try:

            url_playlist = self.download_url.get()

            p = Playlist(url_playlist)
            folder = self.playlists_download_dir(p.title)
            
            for url in p.video_urls:

                try:

                    yt = YouTube(url)
                    file = yt.streams.get_audio_only().download(output_path=folder)
                    self.change_extension_to_mp3(file)
                except:
                    pass

            messagebox.showinfo("Success!", "Download finished, your playlist is at "+folder)


        except:
            messagebox.showinfo("Error!", "Error downloading your playlist")




    def change_extension_to_mp3(self, file):
        base, ext = os.path.splitext(file)
        new_file = base + '.mp3'
        os.rename(file, new_file)


    def get_initial_dir(self):
        if os.name == 'nt':
            import winreg
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                location = winreg.QueryValueEx(key, downloads_guid)[0]
            return location
        else:
            return os.path.join(os.path.expanduser('~'), 'Downloads')



    def playlists_download_dir(self, playlist_title):
        folder_name = str(playlist_title).replace(" ", "_")
        today = str(date.today())
        new_path = f'{self.download_path.get()}/{folder_name}_{today}/'
        os.system(f'mkdir {new_path}')
        return new_path
    








if __name__ == "__main__":
    app = App()
    app.mainloop()

