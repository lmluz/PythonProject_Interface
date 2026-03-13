import customtkinter as ctk

ctk.set_appearance_mode('dark')

root = ctk.CTk()
root.geometry('400x300')
root.title('new app')

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

def mostrar_frame(frame):
    frame.tkraise()

login = ctk.CTkFrame(root)
inicio = ctk.CTkFrame(root)
calculadora = ctk.CTkFrame(root)

for frame in (login, inicio, calculadora):
    frame.grid(row=0, column=0, sticky='nsew')

def validarLogin():
    usar = entry_usar.get()
    password = entry_pass.get()

    if usar == 'luz' and password == '123':
        mostrar_frame(inicio)
    else:
        result_login.configure(text='Login incorreto', text_color='red')

#================== frame login ==================

label_user = ctk.CTkLabel(login, text='User')
label_user.pack(pady=10)

entry_usar = ctk.CTkEntry(login, placeholder_text='Usuario', placeholder_text_color='white')
entry_usar.pack(pady=10)

label_pass = ctk.CTkLabel(login, text='Password')
label_pass.pack(pady=10)

entry_pass = ctk.CTkEntry(login, placeholder_text='Password', placeholder_text_color='white')
entry_pass.pack(pady=10)

button = ctk.CTkButton(login, text='Login', command=validarLogin)
button.pack(pady=10)

result_login = ctk.CTkLabel(login, text='')
result_login.pack(pady=10)

#================== frame inicio ==================

titulo = ctk.CTkLabel(inicio, text='-- Ola, Mundo --', font=('Arial', 25, 'bold'))
titulo.pack(pady=10)

button_cal = ctk.CTkButton(inicio, text='calculadora', command=lambda: mostrar_frame(calculadora))
button_cal.pack(pady=10)

button_vol = ctk.CTkButton(inicio, text='Voltar para pagina de Login', command=lambda: mostrar_frame(login))
button_vol.pack(pady=10)

#================== frame calculadora ==================

entry_cal = ctk.CTkEntry(calculadora, placeholder_text='Digite o valor')
entry_cal.pack(pady=10)

frame_button = ctk.CTkFrame(calculadora)
frame_button.pack(pady=10)

tecladoNum = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['1','.','=','+'],
]

for linha, valor in enumerate(tecladoNum):
    for coluna, valor2 in enumerate(valor):
        botao = ctk.CTkButton(
            frame_button,
            text=valor2,
            width=30,
            height=30,
        )
        botao.grid(row=linha, column=coluna, padx=3, pady=3)

button_voltar = ctk.CTkButton(
    calculadora,
    text='Voltar',
    command=lambda: mostrar_frame(inicio),
)
button_voltar.pack(pady=10)

mostrar_frame(inicio)
root.mainloop()
