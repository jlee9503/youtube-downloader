import tkinter as tk
import customtkinter as ctk
from pytube import YouTube
from PIL import Image


def startDownload() -> None:
    try:
        youtubeLink = link.get()

        if youtubeLink == "":
            completeMsg.configure(text="Please enter a YouTube link", text_color="red")
            return

        videoObject = YouTube(youtubeLink, on_progress_callback=onProgress)
        video = videoObject.streams.get_highest_resolution()
        video.download()
        completeMsg.configure(
            text=videoObject.title + " is successfully downloaded!", text_color="green"
        )
    except:
        completeMsg.configure(text="Invalid link", text_color="red")


def onProgress(stream, chunk, bytes_remaining) -> None:
    video_size = stream.filesize
    bytes_downloaded = video_size - bytes_remaining
    percent_completed = bytes_downloaded / video_size * 100

    percent_str = str(int(percent_completed))
    percent.configure(text=percent_str + "%")
    percent.update()

    progressBar.set(float(percent_completed) / 100)

## Setting ##
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

## App window ##
app = ctk.CTk()
app.geometry("800x500")
app.title("YouTube downloader")

## Adding UI ##
logoImg = ctk.CTkImage(
    Image.open(
        r"/Users/junglee/Desktop/jung/projects/python/youtube-downloader/images/youtube-logo.png"
    ),
    size=(25, 25),
)

title = ctk.CTkLabel(app, text="YouTube Link", image=logoImg, compound="left")
title.pack(padx=10, pady=10)

url = tk.StringVar()
link = ctk.CTkEntry(app, width=500, height=40, textvariable=url)
link.pack()

## Download Complete ##
completeMsg = ctk.CTkLabel(app, text="")
completeMsg.pack()

## Progress Bar ##
percent = ctk.CTkLabel(app, text="0%")
percent.pack()
progressBar = ctk.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

## Download Button ##
downloadBtn = ctk.CTkButton(app, text="Download", command=startDownload)
downloadBtn.pack(padx=20, pady=30)

## Run App ##
app.mainloop()
