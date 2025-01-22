
# convertisseur-youtube-py
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

### **2. Installer le projet**

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/M-darius/convertisseur-youtube-py.git
   cd convertisseur-youtube-py
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

- **Fichiers MP3 :** Les fichiers MP3 seront sauvegardés dans le fichiers désiré.
- **Informations JSON :** Les métadonnées des musiques seront ajoutées au fichier un fichier en .json.
- **Mise à jour du fichier `urls.txt` :** Les URLs téléchargées seront automatiquement supprimées.

---

## 📚 Ressources

- [Documentation de yt_dlp](https://github.com/yt-dlp/yt-dlp)

