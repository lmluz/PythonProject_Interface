import customtkinter as ctk

ctk.set_appearance_mode('dark')

def validarLogin():
    usar = camp_usar.get()
    password = camp_pass.get()

    if usar == 'usar@hotmail.com' and password == '123456':
        result_login.configure(text='Login feito com sucesso', text_color='green')
    else:
        result_login.configure(text='Login incorreto', text_color='red')


root = ctk.CTk()
root.title('new app')
root.geometry('600x400')

label_user = ctk.CTkLabel(root, text='User')
label_user.pack(pady=10)

camp_usar = ctk.CTkEntry(root, placeholder_text='Email', placeholder_text_color='white')
camp_usar.pack(pady=10)

label_pass = ctk.CTkLabel(root, text='Password')
label_pass.pack(pady=10)

camp_pass = ctk.CTkEntry(root, placeholder_text='Password', placeholder_text_color='white')
camp_pass.pack(pady=10)

button = ctk.CTkButton(root, text='Login', command=validarLogin)
button.pack(pady=10)

result_login = ctk.CTkLabel(root, text='')
result_login.pack(pady=10)

root.mainloop()
root.destroy()

