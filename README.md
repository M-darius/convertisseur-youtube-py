
# convertisseur-youtube-py

![Licence MIT](https://img.shields.io/badge/Licence-MIT-blue.svg)
![Version Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)

**Convertisseur YouTube en Python** est un outil simple et efficace permettant de télécharger des vidéos YouTube, de les convertir en fichiers MP3, et de gérer les informations des musiques téléchargées via un fichier JSON. Ce projet utilise la bibliothèque `yt_dlp` pour l'extraction et la conversion des vidéos.

---

## 🚀 Fonctionnalités

- **Téléchargement de vidéos YouTube en MP3** : Téléchargez l'audio des vidéos YouTube dans le format MP3 avec une qualité de 192 kbps.
- **Téléchargement en masse** : Importez une liste d'URLs depuis un fichier texte (`urls.txt`) et téléchargez-les automatiquement.
- **Gestion des informations** : Stockez les informations des musiques téléchargées dans un fichier JSON (`blindtestFiles.json`).
- **Mise à jour automatique des URLs** : Supprimez automatiquement les URLs téléchargées du fichier source pour éviter les doublons.
- **Configuration flexible des chemins** : Personnalisez les chemins de sortie pour les fichiers MP3 et le fichier JSON.

---

## 📦 Installation

### **1. Prérequis**

- **Python 3.6** ou une version supérieure
- **FFmpeg** : Nécessaire pour la conversion des vidéos en MP3.

#### **Installation de FFmpeg**

- **Windows** :
  1. Téléchargez FFmpeg depuis [ffmpeg.org](https://ffmpeg.org/download.html).
  2. Ajoutez le chemin du dossier `bin` de FFmpeg à votre variable d'environnement `PATH`.

- **macOS** :
  ```bash
  brew install ffmpeg
  ```

- **Linux** :
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

### **2. Installer le projet**

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/votre-utilisateur/convertisseur-youtube-py.git
   cd convertisseur-youtube-py
   ```

2. **Créer un environnement virtuel (recommandé) :**
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Installer les dépendances nécessaires :**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Utilisation

### **Préparation**

1. **Créer un fichier `urls.txt` :**  
   Ajoutez une URL YouTube par ligne dans le fichier `urls.txt`. Par exemple :
   ```
   https://www.youtube.com/watch?v=exemple1
   https://www.youtube.com/watch?v=exemple2
   ```

2. **Configurer les chemins (facultatif) :**  
   Les chemins de sortie par défaut sont :
   - `./musics/` pour les fichiers MP3.
   - `blindtestFiles.json` pour le fichier d'informations des musiques.
   Vous pouvez les modifier dans le fichier `convertisseur.py`.

### **Exécution**

Pour lancer le script et télécharger les vidéos :
```bash
python convertisseur.py
```

### **Résultats**

- **Fichiers MP3 :** Les fichiers MP3 seront sauvegardés dans `./musics/`.
- **Informations JSON :** Les métadonnées des musiques seront ajoutées au fichier `blindtestFiles.json`.
- **Mise à jour du fichier `urls.txt` :** Les URLs téléchargées seront automatiquement supprimées.

---

## 📂 Structure du Projet

```
convertisseur-youtube-py/
├── musics/                  # Répertoire de sortie pour les fichiers MP3
├── urls.txt                 # Fichier contenant les URLs des vidéos YouTube
├── blindtestFiles.json      # Fichier JSON contenant les informations des musiques téléchargées
├── convertisseur.py         # Script principal de téléchargement et de conversion
├── requirements.txt         # Dépendances Python
├── .gitignore               # Exclusion des fichiers inutiles
├── README.md                # Documentation du projet
└── LICENSE                  # Licence du projet
```
---

## 📄 Licence

Ce projet est sous licence [MIT](LICENSE).

---

## 🙏 Remerciements

- Merci à [yt_dlp](https://github.com/yt-dlp/yt-dlp) pour leur bibliothèque open-source.
- Merci à [FFmpeg](https://ffmpeg.org/) pour leur outil de conversion.

---

## 📚 Ressources

- [Documentation de yt_dlp](https://github.com/yt-dlp/yt-dlp)
- [Documentation de FFmpeg](https://ffmpeg.org/documentation.html)

