# 🕒 GitHub Actions Auto-Updater

[![GitHub Actions Status](https://img.shields.io/github/actions/workflow/status/USERNAME/REPO-NAME/update-time.yml?label=Automated%20Update&style=flat-square)](https://github.com/USERNAME/REPO-NAME/actions)

Un petit projet démo qui utilise **GitHub Actions** pour mettre à jour automatiquement un fichier toutes les 5 minutes. Parfait pour apprendre l'automatisation CI/CD !

---

## 🚀 Fonctionnalités
- ✅ Exécution planifiée toutes les 5 minutes
- ✅ Génération d'un fichier `current_time.txt` avec l'heure actuelle
- ✅ Commit et push automatiques des modifications
- ✅ Déclenchement manuel possible

## 🛠️ Comment ça marche ?
1. **Un script Python** (`generate_time.py`) génère un fichier avec la date/heure.
2. **Un workflow GitHub Actions** ([`.github/workflows/update-time.yml`](.github/workflows/update-time.yml)) :
   ```yaml
   on:
     schedule:
       - cron: '*/5 * * * *'  # Toutes les 5 minutes
   ```
3. À chaque exécution, le fichier est mis à jour et poussé dans le dépôt.

## ⚙️ Installation
1. **Fork** ce dépôt
2. **Clone** ton fork :
   ```bash
   git clone https://github.com/USERNAME/REPO-NAME.git
   ```
3. Les fichiers nécessaires sont déjà inclus :
   - `generate_time.py` : Script Python
   - `.github/workflows/update-time.yml` : Configuration GitHub Actions

## 🔍 Vérification
- Allez dans l'onglet **Actions** de ton dépôt GitHub
- Surveillez les exécutions du workflow "Update Time File"
- Le fichier `current_time.txt` sera mis à jour automatiquement !

## 🎨 Personnalisation
- Modifiez la fréquence dans `update-time.yml` :
  ```yaml
  cron: '*/5 * * * *'  # Changez le chiffre pour ajuster l'intervalle
  ```
- Modifiez le script Python pour ajouter d'autres fonctionnalités
- Ajoutez des étapes au workflow (tests, notifications, etc.)

## 📄 License
MIT License - Voir le fichier [LICENSE](LICENSE)
peux maintenant pousser ce fichier dans ton dépôt, et il apparaîtra automatiquement sur la page principale de ton projet GitHub ! 😊