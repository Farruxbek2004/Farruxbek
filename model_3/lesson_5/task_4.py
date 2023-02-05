from pytube import YouTube
from tkinter import Label, Entry, Button, Tk, messagebox


def download_youtube():
    try:
        link = sayt_entry.get()
        yt = YouTube(link)
        video = yt.streams.first()
        video.download(save_combo.get())

        messagebox.showinfo("Downloan\n", "\nVideo Downloand"
                                          f"\nShu Papkada --> {save_combo.get()}")

    except:
        messagebox.showerror("Erorr\n", "\nError")


window = Tk()
window.title("YuTube DownLoaD")
window.geometry("600x200")
window.configure(bg='green')

sayt_label = Label(text="Video Linkini Kiritng -->")
sayt_label.place(x=10, y=10)
sayt_label.configure(font=1, background='red')

sayt_entry = Entry()
sayt_entry.place(x=200, y=10)
sayt_entry.configure(font=5)

download_label = Label(text="DownLoaD Papka Nomini Kiriting ->:")
download_label.place(x=10, y=40)
download_label.configure(font=1, background='red')

save_combo = Entry(window, width=20)
save_combo.place(x=300, y=40)
save_combo.configure(font=1)

download_button = Button(text="DownLoaD", bg='#6058B9', command=download_youtube)
download_button.place(x=80, y=100)
download_button.configure(font=1)

window.mainloop()
