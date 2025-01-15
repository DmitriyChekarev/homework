import tkinter

window = tkinter.Tk()
window.title('Проводник')
window.geometry('350x350+800+200')
window.configure(bg='#01579B')
window.resizable(False,False)
window.attributes('-alpha', 0.9)
text = tkinter.Label(window, text='Файл:', height=5, width=20, background='#B3E5FC')
text.grid(column=1, row=1)
button_select=tkinter.Button(window, width=20, height=3, text='Выбрать файл', background='#B3E5FC')
button_select.grid(column=1, row=2)
window.mainloop()