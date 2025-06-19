import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from fox_video_download.service.video_service import download_video
import os
import threading

def escolher_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        pasta_var.set(pasta)
        atualizar_lista_arquivos()

def atualizar_lista_arquivos():
    lista_arquivos.delete(0, tk.END)
    pasta = pasta_var.get()
    if os.path.isdir(pasta):
        for f in os.listdir(pasta):
            lista_arquivos.insert(tk.END, f)

def progresso_callback(percent):
    def set_progress():
        progresso_bar['value'] = percent
    root.after(0, set_progress)

def baixar_video_thread():
    url = url_entry.get()
    pasta = pasta_var.get()
    try:
        output_file = download_video(url, pasta, progress_callback=progresso_callback)
        root.after(0, lambda: messagebox.showinfo("Sucesso", f"Vídeo baixado em:\n{output_file}"))
        root.after(0, atualizar_lista_arquivos)
    except Exception as e:
        root.after(0, lambda: messagebox.showerror("Erro", f"Erro ao baixar vídeo:\n{e}"))
    finally:
        root.after(0, lambda: baixar_btn.config(state=tk.NORMAL))
        root.after(0, lambda: progresso_bar.config(value=0))

def baixar_video():
    progresso_bar['value'] = 0
    baixar_btn.config(state=tk.DISABLED)
    threading.Thread(target=baixar_video_thread, daemon=True).start()

def checar_clipboard():
    try:
        clipboard = root.clipboard_get()
        if clipboard.startswith("http"):
            if messagebox.askyesno("Link detectado", f"Detectamos um link na área de transferência:\n{clipboard}\nDeseja baixar?"):
                url_entry.delete(0, tk.END)
                url_entry.insert(0, clipboard)
    except Exception:
        pass

root = tk.Tk()
root.title("Fox Video Download")
root.geometry("600x440")

# Header
header = tk.Frame(root)
header.pack(fill=tk.X, pady=5)
tk.Label(header, text="Fox Video Download", font=("Arial", 16, "bold")).pack(side=tk.LEFT, padx=10)
baixar_btn = tk.Button(header, text="Baixar", command=baixar_video)
baixar_btn.pack(side=tk.RIGHT, padx=10)

# Campo URL
url_frame = tk.Frame(root)
url_frame.pack(fill=tk.X, padx=10, pady=5)
tk.Label(url_frame, text="URL do vídeo:").pack(side=tk.LEFT)
url_entry = tk.Entry(url_frame, width=50)
url_entry.pack(side=tk.LEFT, padx=5)

# Campo pasta destino
pasta_frame = tk.Frame(root)
pasta_frame.pack(fill=tk.X, padx=10, pady=5)
tk.Label(pasta_frame, text="Pasta destino:").pack(side=tk.LEFT)
pasta_var = tk.StringVar(value=os.path.expanduser("~/Downloads"))
pasta_entry = tk.Entry(pasta_frame, textvariable=pasta_var, width=40)
pasta_entry.pack(side=tk.LEFT, padx=5)
pasta_btn = tk.Button(pasta_frame, text="Escolher...", command=escolher_pasta)
pasta_btn.pack(side=tk.LEFT)

# Barra de progresso
progresso_bar = ttk.Progressbar(root, orient="horizontal", length=580, mode="determinate", maximum=100)
progresso_bar.pack(padx=10, pady=10)

# Lista de arquivos baixados
arquivos_frame = tk.LabelFrame(root, text="Arquivos baixados")
arquivos_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
lista_arquivos = tk.Listbox(arquivos_frame)
lista_arquivos.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Inicializa lista
atualizar_lista_arquivos()

# Checa clipboard ao abrir
root.after(500, checar_clipboard)

root.mainloop()