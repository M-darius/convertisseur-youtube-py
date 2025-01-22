import os
import json
import yt_dlp
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox

def choisir_fichier_url():
    fichier = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
    if fichier:
        entree_fichier_url.delete(0, 'end')
        entree_fichier_url.insert(0, fichier)

def choisir_dossier_sortie():
    dossier = filedialog.askdirectory()
    if dossier:
        entree_dossier_sortie.delete(0, 'end')
        entree_dossier_sortie.insert(0, dossier)

def choisir_fichier_json():
    fichier = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Fichiers JSON", "*.json")])
    if fichier:
        entree_fichier_json.delete(0, 'end')
        entree_fichier_json.insert(0, fichier)

def telecharger_videos():
    url_file = entree_fichier_url.get()
    output_path = entree_dossier_sortie.get()
    music_info_file = entree_fichier_json.get()

    if not url_file or not os.path.exists(url_file):
        messagebox.showerror("Erreur", "Veuillez sélectionner un fichier d'URL valide.")
        return
    if not output_path or not os.path.isdir(output_path):
        messagebox.showerror("Erreur", "Veuillez sélectionner un dossier de sortie valide.")
        return
    if not music_info_file:
        messagebox.showerror("Erreur", "Veuillez spécifier un fichier JSON pour enregistrer les métadonnées.")
        return

    try:
        download_multiple_videos_as_mp3_from_file(url_file, output_path, music_info_file)
        messagebox.showinfo("Succès", "Téléchargement terminé.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

def download_youtube_video_as_mp3(url, output_path, music_info_file):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', None)
            new_file = os.path.join(output_path, f"{title}.mp3")
        
        relative_path = os.path.join(output_path, f"{title}.mp3").replace("\\", "/")

        music_info = {
            "name": title,
            "theme": "unknown",
            "path": relative_path
        }

        if os.path.exists(music_info_file):
            with open(music_info_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = []

        data.append(music_info)

        with open(music_info_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"Erreur : {str(e)}")

def update_url_file(url_file, downloaded_url):
    try:
        with open(url_file, 'r', encoding='utf-8') as f:
            urls = f.readlines()
        
        urls = [url.strip() for url in urls if url.strip() and url.strip() != downloaded_url]

        with open(url_file, 'w', encoding='utf-8') as f:
            f.writelines([url + '\n' for url in urls])

    except Exception as e:
        print(f"Erreur lors de la mise à jour du fichier d'URLs : {str(e)}")

def download_multiple_videos_as_mp3_from_file(url_file, output_path, music_info_file):
    try:
        with open(url_file, 'r', encoding='utf-8') as f:
            urls = f.readlines()
        
        urls = [url.strip() for url in urls if url.strip()]
        for url in urls:
            download_youtube_video_as_mp3(url, output_path, music_info_file)
            update_url_file(url_file, url)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier d'URLs : {str(e)}")

# Interface graphique
fenetre = Tk()
fenetre.title("Convertisseur YouTube en MP3")
fenetre.geometry("600x300")

Label(fenetre, text="Fichier d'URLs :").grid(row=0, column=0, padx=10, pady=10, sticky='w')
entree_fichier_url = Entry(fenetre, width=50)
entree_fichier_url.grid(row=0, column=1, padx=10, pady=10)
Button(fenetre, text="Parcourir", command=choisir_fichier_url).grid(row=0, column=2, padx=10, pady=10)

Label(fenetre, text="Dossier de sortie :").grid(row=1, column=0, padx=10, pady=10, sticky='w')
entree_dossier_sortie = Entry(fenetre, width=50)
entree_dossier_sortie.grid(row=1, column=1, padx=10, pady=10)
Button(fenetre, text="Parcourir", command=choisir_dossier_sortie).grid(row=1, column=2, padx=10, pady=10)

Label(fenetre, text="Fichier JSON :").grid(row=2, column=0, padx=10, pady=10, sticky='w')
entree_fichier_json = Entry(fenetre, width=50)
entree_fichier_json.grid(row=2, column=1, padx=10, pady=10)
Button(fenetre, text="Parcourir", command=choisir_fichier_json).grid(row=2, column=2, padx=10, pady=10)

Button(fenetre, text="Télécharger", command=telecharger_videos).grid(row=3, column=1, pady=20)

fenetre.mainloop()
