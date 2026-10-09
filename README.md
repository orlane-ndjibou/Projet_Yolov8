# 👁️ Système d'assistance visuelle en temps réel - YOLOv8

Application Python de détection d'objets en temps réel via webcam, basée sur **YOLOv8**. Le programme compte le nombre de personnes présentes à l'écran et déclenche une alerte visuelle lorsqu'un objet cible (configurable) est détecté.

## 🎯 Fonctionnalités

- Détection d'objets en temps réel à partir du flux webcam
- Compteur dynamique du nombre de personnes à l'écran
- Alerte visuelle lorsqu'une classe d'objet spécifique est détectée
- Basé sur un modèle YOLOv8 pré-entraîné (dataset COCO, 80 classes)

## 🛠️ Stack technique

- **Python 3**
- **[Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)** - détection d'objets
- **OpenCV** - capture et affichage vidéo

## 📦 Installation

```bash
# Cloner le dépôt
git clone https://github.com/<ton-user>/<ton-repo>.git
cd <ton-repo>

# Créer et activer un environnement virtuel
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS / Linux

# Installer les dépendances
pip install ultralytics opencv-python
```

## ▶️ Utilisation

```bash
python main.py
```

- Une fenêtre s'ouvre avec le flux de la webcam et les objets détectés en direct.
- Le nombre de personnes détectées s'affiche en haut à gauche.
- Une alerte rouge **"ALERTE"** apparaît si l'objet cible est détecté.
- Appuyer sur **`q`** pour quitter.

Pour changer l'objet surveillé, modifie la variable en haut du script :

```python
TARGET_CLASS = "knife"  # remplace par n'importe quelle classe COCO (ex: "cell phone", "scissors"...)
```

Un notebook Jupyter (`projet_yolo.ipynb`) est également fourni pour explorer le projet étape par étape.

## 📁 Structure du projet

```
.
├── main.py              # Script principal (webcam + détection + logique métier)
├── projet_yolo.ipynb    # Notebook explicatif étape par étape
└── README.md
```

## 🚀 Améliorations possibles

- Enregistrement vidéo automatique lors d'une alerte
- Notification sonore
- Filtrage sur plusieurs classes cibles simultanément
- Export des logs de détection (CSV / base de données)

## 📄 Licence

Projet réalisé à des fins d'apprentissage / démonstration.
