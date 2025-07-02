import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from fox_video_download.service.video_service import download_video
import os
import threading

def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_var.set(folder)
        update_file_list()

def update_file_list():
    file_listbox.delete(0, tk.END)
    folder = folder_var.get()
    if os.path.isdir(folder):
        for f in os.listdir(folder):
            file_listbox.insert(tk.END, f)

def progress_callback(percent):
    def set_progress():
        progress_bar['value'] = percent
    root.after(0, set_progress)

def download_video_thread():
    url = url_entry.get()
    folder = folder_var.get()
    try:
        output_file = download_video(url, folder, progress_callback=progress_callback)
        root.after(0, lambda: messagebox.showinfo("Success", f"Video downloaded to:\n{output_file}"))
        root.after(0, update_file_list)
    except Exception as e:
        root.after(0, lambda: messagebox.showerror("Error", f"Error downloading video:\n{e}"))
    finally:
        root.after(0, lambda: download_btn.config(state=tk.NORMAL))
        root.after(0, lambda: progress_bar.config(value=0))

def download_video_action():
    progress_bar['value'] = 0
    download_btn.config(state=tk.DISABLED)
    threading.Thread(target=download_video_thread, daemon=True).start()

def check_clipboard():
    try:
        clipboard = root.clipboard_get()
        if clipboard.startswith("http"):
            if messagebox.askyesno("Link detected", f"Detected a link in the clipboard:\n{clipboard}\nDo you want to download?"):
                url_entry.delete(0, tk.END)
                url_entry.insert(0, clipboard)
    except Exception:
        pass

root = tk.Tk()
root.title("Fox Video Download")
root.geometry("600x440")

header = tk.Frame(root)
header.pack(fill=tk.X, pady=5)
tk.Label(header, text="Fox Video Download", font=("Arial", 16, "bold")).pack(side=tk.LEFT, padx=10)
download_btn = tk.Button(header, text="Download", command=download_video_action)
download_btn.pack(side=tk.RIGHT, padx=10)

url_frame = tk.Frame(root)
url_frame.pack(fill=tk.X, padx=10, pady=5)
tk.Label(url_frame, text="Video URL:").pack(side=tk.LEFT)
url_entry = tk.Entry(url_frame, width=50)
url_entry.pack(side=tk.LEFT, padx=5)

folder_frame = tk.Frame(root)
folder_frame.pack(fill=tk.X, padx=10, pady=5)
tk.Label(folder_frame, text="Destination folder:").pack(side=tk.LEFT)
folder_var = tk.StringVar(value=os.path.expanduser("~/Downloads"))
folder_entry = tk.Entry(folder_frame, textvariable=folder_var, width=40)
folder_entry.pack(side=tk.LEFT, padx=5)
folder_btn = tk.Button(folder_frame, text="Choose...", command=choose_folder)
folder_btn.pack(side=tk.LEFT)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=580, mode="determinate", maximum=100)
progress_bar.pack(padx=10, pady=10)

files_frame = tk.LabelFrame(root, text="Downloaded files")
files_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
file_listbox = tk.Listbox(files_frame)
file_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

update_file_list()

root.after(500, check_clipboard)

root.mainloop()