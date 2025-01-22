import os
import json
import yt_dlp

def download_youtube_video_as_mp3(url, output_path, music_info_file):
    try:
        # Configuration pour télécharger l'audio et convertir en MP3
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Nom du fichier de sortie
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', None)
            new_file = os.path.join(output_path, f"{title}.mp3")
        
        # Construire le chemin relatif pour le JSON
        relative_path = os.path.join(output_path, f"{title}.mp3").replace("\\", "/")

        # Extraire les informations de la musique
        music_info = {
            "name": title,
            "theme": "unknown",  # Tu peux définir un style ici si tu le connais
            "path": relative_path
        }
        
        # Ajouter ces informations au fichier JSON
        if os.path.exists(music_info_file):
            with open(music_info_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = []

        data.append(music_info)

        with open(music_info_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"Téléchargement terminé. Fichier sauvegardé sous : {new_file}")
        print(f"Information sauvegardée dans {music_info_file}")
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
        
        urls = [url.strip() for url in urls if url.strip()]  # Nettoyage des URLs
        for url in urls:
            download_youtube_video_as_mp3(url, output_path, music_info_file)
            update_url_file(url_file, url)  # Met à jour le fichier pour supprimer l'URL téléchargée
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier d'URLs : {str(e)}")

# Chemin du fichier contenant les URLs
url_file = "urls.txt"  # Nom du fichier texte contenant les URLs
output_path = "./musics/"  # Chemin de sortie
music_info_file = "blindtestFiles.json"  # Fichier JSON où stocker les informations

download_multiple_videos_as_mp3_from_file(url_file, output_path, music_info_file)
