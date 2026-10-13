<div align="center">

![AI-SIEM Logo](ai-siem-logo.png)

#  Projet : Moteur SIEM Propulsé par l'IA (AI-SIEM)

*Démarche complète de détection d'anomalies réseau via le Machine Learning, avec conteneurisation.*

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://www.docker.com/)
[![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg)](https://scikit-learn.org/)

Ce projet implémente un système intelligent de gestion des informations et des événements de sécurité (SIEM). Conçu pour analyser le trafic réseau, il utilise l'algorithme Isolation Forest pour identifier les cybermenaces potentielles ou les comportements inhabituels en temps réel, le tout dans un environnement Dockerisé.

📄 [Consulter le Rapport Technique (PDF)](Rapport%20Technique%20Final.pdf) · ⚙️ [Voir le Plan de Projet (PDF)](Plan%20de%20Projet.pdf)

</div>

---

##  Table des matières
1. [À Propos du Projet](#-à-propos-du-projet)
2. [Fonctionnalités Clés](#-fonctionnalités-clés)
3. [Technologies & Environnement](#-technologies--environnement)
4. [Pour Commencer](#-pour-commencer)
5. [Résultats / Livrables (PDF)](#-résultats--livrables-pdf)
6. [Captures d'Écran et Preuves](#-captures-décran-et-preuves)
7. [Auteurs & Crédits](#-auteurs--crédits)

---

##  À Propos du Projet

L'analyse traditionnelle des logs peine souvent à suivre le volume et la complexité des cyberattaques modernes. Le projet AI-SIEM intègre une approche basée sur l'Intelligence Artificielle (Machine Learning) pour établir une base de référence du trafic réseau normal et détecter les déviations (anomalies) sans se fier uniquement aux signatures connues.

**Objectifs Académiques & Techniques :**
* Développer un modèle de Machine Learning robuste pour la classification du trafic réseau.
* Mettre en place un pipeline de prétraitement des données (normalisation, encodage).
* Appliquer les principes d'Infrastructure as Code (IaC) via la conteneurisation.
* Produire des livrables de qualité professionnelle (Rapports techniques, schémas d'architecture).

##  Fonctionnalités Clés

* **Détection d'Anomalies (Machine Learning) :** Utilisation de l'algorithme `Isolation Forest` de Scikit-Learn pour isoler les comportements réseau suspects.
* **Prétraitement Automatisé :** Pipeline de traitement incluant le `Label Encoding` pour les variables catégorielles (ex: protocol_type) et le `Feature Scaling` (StandardScaler) pour la normalisation des flux de données.
* **Architecture Conteneurisée :** Environnement d'exécution totalement isolé via un conteneur `Python 3.11-slim`, orchestré par Docker Compose pour garantir la reproductibilité.
* **Modulaire et Évolutif :** Séparation stricte entre les données, le modèle, la logique d'entraînement et l'infrastructure.

##  Technologies & Environnement

* **Logique Centrale & Scripting :** Python 3.11 (`src/data_prep.py`, `src/train.py`).
* **Intelligence Artificielle :** Scikit-Learn, Pandas, NumPy, Joblib (pour la sérialisation du modèle).
* **Infrastructure / DevOps :** Docker (`Dockerfile`), Docker Compose (`infrastructure/docker-compose.yml`).
* **Contrôle de Version :** Git, GitHub.

##  Pour Commencer

### Prérequis
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installé sur votre système (ou Docker Engine).
* Git pour le clonage du dépôt.

### Exécution avec Docker Compose

L'ensemble de l'application (prétraitement, entraînement, évaluation) est conçu pour s'exécuter via Docker Compose.

1. **Cloner le dépôt :**
```bash
git clone https://github.com/mohamed-aitbella/ai-siem-project.git
cd ai-siem-project
```

2. **Lancer l'orchestration :**
```bash
docker-compose up --build
```

---

##  Résultats / Livrables (PDF)

Le projet est documenté de manière exhaustive à travers des rapports PDF professionnels.

* 📄 **[Plan de Projet (PDF)](Plan%20de%20Projet.pdf)** : Document initial définissant la feuille de route, les objectifs et la pile technologique.
* 📄 **[Rapport Technique Final (PDF)](Rapport%20Technique%20Final.pdf)** : Bilan complet du projet, incluant l'analyse des métriques du modèle (Accuracy, Precision, Recall) et les perspectives d'amélioration.

---

##  Captures d'Écran et Preuves

###  Architecture du Système AI SIEM
Schéma illustrant le flux de données, du chargement du fichier CSV jusqu'à la sauvegarde du modèle ML sérialisé.
<div align="center">
  <img src="Architecture%20du%20Système%20AI%20SIEM.png" alt="Architecture du Système AI SIEM" width="800">
</div>

###  Structure Initiale du Projet
Organisation claire des répertoires séparant les données, les modèles, le code source et l'infrastructure.
<div align="center">
  <img src="Structure%20initiale%20du%20projet.png" alt="Structure initiale du projet" width="800">
</div>

###  Espace de Travail et Structure Finale
Vue d'ensemble de l'environnement de développement (VS Code) avec tous les scripts finalisés.
<div align="center">
  <img src="Espace%20de%20travail%20et%20structure%20finale.png" alt="Espace de travail et structure finale" width="800">
</div>

###  Configuration de Docker Compose
Infrastructure as Code permettant de définir et de lancer le moteur SIEM dans un environnement isolé de manière reproductible.
<div align="center">
  <img src="Configuration%20de%20Docker%20Compose.png" alt="Configuration de Docker Compose" width="800">
</div>

###  Exécution et Résultats d'Entraînement du Modèle
Trace de l'outil en action. L'interface affiche l'Accuracy (précision globale) et le rapport de classification détaillé prouvant le bon fonctionnement de l'algorithme d'anomalie.
<div align="center">
  <img src="Exécution%20et%20résultats%20d'entraînement%20du%20modèle.png" alt="Exécution et résultats d'entraînement du modèle" width="800">
</div>

---

##  Auteurs & Crédits

* **Mohamed Ait Bella**
  *Conception, Développement ML, Conteneurisation & Documentation*

*Projet réalisé pour démontrer l'application de l'apprentissage automatique dans un contexte de cybersécurité (SIEM) et l'intégration des pratiques DevOps.*ٍ