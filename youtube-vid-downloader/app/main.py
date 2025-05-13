#!/usr/bin/env python3

from pytubefix import YouTube #for dowloading the videos
import tkinter as tk 
from tkinter import filedialog
from tqdm import tqdm #for the progress bar

progress = None


def main():
    url = input("Please enter the YouTube url: ")
    if not url.strip():
        print("No url entered. Exiting the program ...")
        return

    download_destination = open_file_dialog()
    
    if download_destination:
        print("\nThe download has started!")
        video_download(url,download_destination)
    else:
        print("Invalid save location")


def video_download(url: str, download_destination:str):
    global progress
    try:
        yt = YouTube(url, on_progress_callback=progress_bar,on_complete_callback=complete_bar)
        print(yt.title)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()

        #initializing the progress bar 
        filesize = highest_res_stream.filesize
        progress = tqdm(total=filesize,unit='B', unit_scale=True,desc="Downloading")
        
        highest_res_stream.download(output_path=download_destination)

    except Exception as e:
        print(f"Error occured: {e}")


def complete_bar(stream, file_path):
    global progress
    progress.close()
    print("Download is completed.")


def progress_bar(stream,chunk,bytes_remaining):
    global progress
    bytes_downloaded = stream.filesize - bytes_remaining

    if progress:
        progress.n = bytes_downloaded
        progress.refresh()
    


def open_file_dialog() -> str :
   dir = filedialog.askdirectory()
   if dir:
      print(f"Selected folder: {dir}")

   return dir


if __name__ == "__main__":

    root_window = tk.Tk()
    root_window.withdraw()
    main()

