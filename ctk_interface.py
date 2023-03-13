import tkinter as tk
import customtkinter as ctk


download_options = ['Download an audio', 'Download a video', 'Download a video playlist', 'Download an audio playlist']

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # self.geometry(f"{750}x{300}")
        self.center_window(750,300)
        self.title("Youtube Downloader")
        self.resizable(False,False)


        # setting up 5x4 grid system
        self.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.grid_columnconfigure((0,1,2,3), weight=1)





        # creating the widgets
        self.title_label = ctk.CTkLabel(master=self,
                                        text="Youtube Downloader",
                                        font= ctk.CTkFont(size=30, weight="normal")
                                        )
        


        self.url_label = ctk.CTkLabel(master=self,
                                        text="Url: ",
                                        font= ctk.CTkFont(size=15, weight="normal")
                                        )


    
        self.url_entry = ctk.CTkEntry(master=self,
                                width=400,
                               height=30,
                               placeholder_text='url goes here',
                               border_width=2,
                               corner_radius=10)
        

        self.clear_btn = ctk.CTkButton(master=self,
                                        height=30,
                                       text="Clear")
        




        self.path_label = ctk.CTkLabel(master=self,
                                text="Destination: ",
                                font= ctk.CTkFont(size=15, weight="normal")
                                )




        
        self.path_entry = ctk.CTkEntry(master=self,
                                width=400,
                               height=30,
                               placeholder_text='url goes here',
                               border_width=2,
                               corner_radius=10)
        
        self.browse_btn = ctk.CTkButton(master=self,
                                height=30,
                                text="Browse")


        self.select_options = ctk.CTkOptionMenu(master=self,
                                        width=195,
                                       values=download_options,
                                       )
        self.select_options.set('Select an option')
        
        self.download_btn = ctk.CTkButton(master=self,
                                         height=30,
                                        text="Download",
                                        width=195)



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

        


        
        



if __name__ == "__main__":
    app = App()
    app.mainloop()
