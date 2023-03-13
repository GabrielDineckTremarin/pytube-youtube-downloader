import tkinter as tk
from datetime import date
import customtkinter as ctk
import os
from pytube import YouTube, Playlist



ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.download_options = ['Download an audio', 'Download a video', 'Download an audio playlist', 'Download a video playlist']
        self.initial_dir = self.get_initial_dir()
        self.download_url = ctk.StringVar(master=self)
        self.download_path = ctk.StringVar(master=self)
        self.download_path.set(self.initial_dir)
        self.choosen_download_option = ''
        self.labels_font_cfg = ctk.CTkFont(size=15, weight="normal")


        # self.geometry(f"{750}x{300}")
        self.center_window(750,300)
        self.title("Youtube Downloader")
        self.resizable(False,False)


        # setting up 6x4 grid system
        self.grid_config()



        # creating the widgets
        self.title_label = ctk.CTkLabel(master=self,
                                        text="Youtube Downloader",
                                        font= ctk.CTkFont(size=30, weight="normal")
                                        )
        


        self.url_label = ctk.CTkLabel(master=self,
                                        text="Url: ",
                                        font= self.labels_font_cfg
                                        )


    
        self.url_entry = ctk.CTkEntry(master=self,
                                width=400,
                               height=30,
                               border_width=2,
                               corner_radius=10,
                                textvariable=self.download_url
                               )
        

        self.clear_btn = ctk.CTkButton(master=self,
                                        height=30,
                                       text="Clear",
                                       command=self.clear_url_entry)
        




        self.path_label = ctk.CTkLabel(master=self,
                                text="Destination: ",
                                font= self.labels_font_cfg)

        

        
        self.path_entry = ctk.CTkEntry(master=self,
                                width=400,
                               height=30,
                               placeholder_text='url goes here',
                               border_width=2,
                               corner_radius=10,
                               textvariable=self.download_path)
        

        self.browse_btn = ctk.CTkButton(master=self,
                                height=30,
                                text="Browse",
                                command=self.browse)


        self.select_options = ctk.CTkOptionMenu(master=self,
                                        width=195,
                                       values=self.download_options,
                                       command=self.set_download_option
                                       )
        self.select_options.set('Select an option')


        
        self.download_btn = ctk.CTkButton(master=self,
                                         height=30,
                                        text="Download",
                                        width=195,
                                        command=self.download)



        #putting the widgets in the frame
        self.title_label.grid(row=0, column=0,columnspan=4)
        self.url_label.grid(row=2, column=0, sticky='e')
        self.url_entry.grid(row=2, column=1, columnspan=2)
        self.clear_btn.grid(row=2, column=3, sticky='w')
        self.path_label.grid(row=3,column=0, sticky='e')
        self.path_entry.grid(row=3,column=1, columnspan=2)
        self.browse_btn.grid(row=3, column=3, sticky='w')
        self.select_options.grid(row=4,column=1, sticky='e', padx=5)
        self.download_btn.grid(row=4, column=2, sticky='w', padx=5)


    def center_window(self, width, height):
        width_screen = self.winfo_screenwidth()
        height_screen = self.winfo_screenheight()
        x = (width_screen/2) - (width/2)
        y = (height_screen/2) - (height/2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))


    def grid_config(self):
        self.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.grid_rowconfigure(5, weight=3)
        self.grid_columnconfigure((0,1,2,3), weight=1)



    def clear_url_entry(self):
        self.download_url.set('')



    def browse(self):
        download_dir = ctk.filedialog.askdirectory(initialdir=self.initial_dir)
        self.download_path.set(download_dir)




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
        


    def set_download_option(self, choice):
        self.choosen_download_option = choice



    def playlists_download_dir(self, playlist_title):
        folder_name = str(playlist_title).replace(" ", "_")
        today = str(date.today())
        new_path = f'{self.download_path.get()}/{folder_name}_{today}/'
        os.system(f'mkdir {new_path}')
        return new_path
    





    def download(self):
        if self.choosen_download_option == self.download_options[0]:
            self.download_audio()

        elif self.choosen_download_option == self.download_options[1]:
            self.download_video()

        elif self.choosen_download_option == self.download_options[2]:
            self.download_audio_playlist()

        elif self.choosen_download_option == self.download_options[3]:
            self.download_video_playlist()

        else:
            self.show_info("Error!", "Select an option")


    def download_video(self):
        pass
        try:
            url = self.download_url.get()
            folder = self.download_path.get()

            video = YouTube(url)
            video.streams.get_highest_resolution().download(output_path=folder)
            self.show_info("Success!", "Download finished, your video is at "+folder)
        
        except:
            self.show_info("Error!", "Error downloading your video")  


    def download_audio(self):
        pass
        try:
            url = self.download_url.get()
            folder = self.download_path.get()

            audio = YouTube(url)
            file = audio.streams.get_audio_only().download(output_path=folder)
            self.change_extension_to_mp3(file)
            self.show_info("Success!", "Download finished, your audio is at "+folder)
            
        
        except:
            self.show_info("Error!", "Error downloading your audio")  
            

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

            self.show_info("Success!", "Download finished, your playlist is at "+folder)


        except:
            self.show_info("Error!", "Error downloading your playlist")



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

            self.show_info("Success!", "Download finished, your playlist is at "+folder)
            


        except:
            self.show_info("Error!", "Error downloading your playlist")
            # ctk.messagebox.showinfo("Error!", "Error downloading your playlist")



    def show_info(self, msg1, msg2):
        tk.messagebox.showinfo(msg1, msg2)
        


        
        



if __name__ == "__main__":
    app = App()
    app.mainloop()
