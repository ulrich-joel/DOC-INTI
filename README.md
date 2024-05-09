# Procédure d'installation/déploiement du logiciel INTIA Assurance

## Introduction:

Ce document décrit les étapes nécessaires pour installer et déployer le logiciel INTIA Assurance sur un environnement de production.

## Prérequis:

Avant de commencer l'installation, assurez-vous que les éléments suivants sont installés sur votre système :

- Base de données SQLite3
- Python 3.11 ou 3.12
- Django framework
- Virtualenv

## Etapes d'installation:

1. **Cloner le dépôt Git:**
   Creer un dossier intia_app
   à l'intérieur du dossiers intia_app cloner le fichier source du projet
   ```
   git clone https://github.com/ulrich-joel/DOC-INTIA.git
   ```

3. **Créer un environnement virtuel:**
   ```
   cd DOC-INTIA
   py -m venv venv
   venv\Scripts\activate
   ```

4. **Installer les dépendances:**
   ```
   pip install -r requirements.txt
   ```

5. **Configurer la base de données:**
   - Ouvrez le fichier `settings.py` dans le répertoire `DOC-INTIA/intia_app`.
   - Modifiez les informations de connexion à la base de données selon vos besoins.

6. **Migrer les bases de données:**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Télécharger Matérial Design Bootstrap:**
   - Visitez le site officiel [Matérial Design Bootstrap](https://mdbootstrap.com/) pour télécharger le package.
   - Dézippez le fichier et renommez-le en `static`.
   - Copiez le contenu et collez-le dans le répertoire racine du projet `DOC-INTIA`.

8. **Lancer le serveur Django:**
   ```
   py manage.py runserver
   ```

## Organisation du projet et suivi des avancées:

Pour obtenir plus de détails sur l'organisation du projet INTIA Assurance ainsi que pour suivre les avancées, veuillez vous référer à notre tableau Trello dédié :

[Trello INTIA Assurance](https://trello.com/invite/b/9MjM56Vn/ATTI346f1b09309523d1f0d1a300ede0ce7fEB0D215D/intiaapp)

Sur ce tableau Trello, vous trouverez :

- Les différentes tâches et fonctionnalités planifiées pour le projet.
- L'état d'avancement de chaque tâche, les difficultés rencontrées, les technologies utilisées et celles qui seront utilisées.
- Les informations sur le déploiement sur AWS.
- Les risques identifiés et les ressources utilisées.
- Des descriptions détaillées des fonctionnalités.
- Quelques commentaires sur le projet et des mises à jour régulières sur les progrès réalisés.

N'hésitez pas à nous rejoindre sur Trello pour suivre de près l'évolution du projet et pour interagir avec notre équipe de développement. Nous sommes ouverts à toute suggestion ou commentaire qui pourrait contribuer à l'amélioration du logiciel INTIA Assurance.
