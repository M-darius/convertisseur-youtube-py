# convertisseur-youtube-py

![Licence MIT](https://img.shields.io/badge/Licence-MIT-blue.svg)
![Version Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)

**Convertisseur YouTube en Python** est un outil simple et efficace permettant de télécharger des vidéos YouTube, de les convertir en fichiers MP3, et de gérer les informations des musiques téléchargées via un fichier JSON. Ce projet utilise la bibliothèque `yt_dlp` pour l'extraction et la conversion des vidéos.

## 🚀 Fonctionnalités

- **Téléchargement de vidéos YouTube en MP3** : Téléchargez l'audio des vidéos YouTube dans le format MP3 avec une qualité de 192 kbps.
- **Téléchargement en masse** : Importez une liste d'URLs depuis un fichier texte (`urls.txt`) et téléchargez-les automatiquement.
- **Gestion des informations** : Stockez les informations des musiques téléchargées dans un fichier JSON (`blindtestFiles.json`).
- **Mise à jour automatique des URLs** : Supprimez automatiquement les URLs téléchargées du fichier source pour éviter les doublons.
- **Configuration flexible des chemins** : Personnalisez les chemins de sortie pour les fichiers MP3 et le fichier JSON.

## 📦 Installation

### 1. **Prérequis**

- **Python 3.6** ou une version supérieure
- **FFmpeg** : Nécessaire pour la conversion des vidéos en MP3.

#### **Installer FFmpeg**

- **Windows** :
  1. Téléchargez la dernière version de FFmpeg depuis [ffmpeg.org](https://ffmpeg.org/download.html).
  2. Extrayez le contenu et ajoutez le chemin vers le dossier `bin` de FFmpeg à votre variable d'environnement `PATH`.

- **macOS** :
  ```bash
  brew install ffmpeg
