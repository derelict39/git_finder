from tkinter import *
from PIL import Image, ImageTk
import requests
import webbrowser

root = Tk()

img = Image.open("img/githubLogo.png")
icon = ImageTk.PhotoImage(img)
root.tk.call('wm', 'iconphoto', root._w, icon)


def open_url(url):
    webbrowser.open(url)


def get_repo():
    username = gitField.get()
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repositories = response.json()
        text_field.delete('1.0', END)
        for repo in repositories:
            repo_name = repo["name"]
            repo_url = repo["html_url"]
            text_field.insert(END, f"{repo_name}: ")
            text_field.insert(END, f"{repo_url}\n", ('link', repo_url))
    else:
        text_field.delete('1.0', END)
        text_field.insert(END, f"Ошибка при выполнении запроса: {response.status_code}\n")


root.configure(background='lightgrey')
root.title('Open user repositories on GitHub')
root.geometry('500x500')
root.resizable(width=False, height=False)

logo = PhotoImage(file="img/githubLogo.png")
logo_label = Label(root, image=logo, bg="lightgrey")
logo_label.place(relx=0.5, rely=0.05, anchor='n')

frame_top = Frame(root, bg='white', bd=5)
frame_top.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.3, anchor='n')

frame_bottom = Frame(root, bg='white', bd=5)
frame_bottom.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.45, anchor='n')

gitField = Entry(frame_top, bg='white', font=("Times New Roman", 20))
gitField.pack(expand=True, fill=BOTH)

button = Button(frame_top, text='find out...', command=get_repo, font=("Helvetica", 15), bg='lightblue')
button.pack(expand=True, fill=BOTH)

text_field = Text(frame_bottom, bg='white', font=("Helvetica", 13))
text_field.tag_config('link', foreground='blue', underline=True)
text_field.tag_bind('link', '<Button-1>', lambda e: open_url(e.widget.tag_names(CURRENT)[1]))
text_field.pack(expand=True, fill=BOTH)

watermark = Label(root, text="made by derelict39", bg='lightgrey', font=("Helvetica", 13))
watermark.place(relx=0.5, rely=0.95, anchor='s')

root.mainloop()
