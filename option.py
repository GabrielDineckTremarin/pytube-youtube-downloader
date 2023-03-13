import customtkinter

app = customtkinter.CTk()

optionmenu_var = customtkinter.StringVar(value="option 213")  # set initial value

def optionmenu_callback():
    print("optionmenu dropdown clicked:",optionmenu_var.get() )

combobox = customtkinter.CTkOptionMenu(master=app,
                                       values=["option 1", "option 2"],
                                       command=optionmenu_callback,
                                       variable=optionmenu_var)
combobox.pack(padx=20, pady=10)

app.mainloop()