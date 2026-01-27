# Lab 01 — Azure ACI : PHP / MySQL / phpMyAdmin

## 📌 Description

Ce laboratoire démontre le déploiement d’une application web 3-tiers sur Microsoft Azure à l’aide d’Azure Container Instances.

L’architecture comprend :
- Un serveur MySQL (Base de données)
- phpMyAdmin (Administration)
- Un serveur Apache/PHP (Frontend web)

---

## 🏗 Architecture
Client Web
↓
Apache + PHP (ACI)
↓
MySQL (ACI)


---

## 🚀 Technologies utilisées

- Microsoft Azure (ACI)
- Docker Containers
- MySQL 8
- phpMyAdmin
- Apache2
- PHP 8.2
- Debian 12
- Linux CLI

---

## ⚙️ Déploiement

### 1️⃣ Création du conteneur MySQL

``bash
Image: mysql:8.0
Port: 3306
Env:
MYSQL_ROOT_PASSWORD=*****

2️⃣ Création du conteneur phpMyAdmin
Image: phpmyadmin
Port: 80
Env:
PMA_HOST=<mysql-fqdn>
MYSQL_ROOT_PASSWORD=*****

3️⃣ Création du conteneur Web (Debian)
Image: debian:12
Port: 80
Command: tail -f /dev/null


Installation des services :

apt update
apt install apache2 php php-mysql

🗄 Base de données

La base ecommerce contient la table clients.

Structure :

CREATE TABLE clients (
  client_id INT AUTO_INCREMENT PRIMARY KEY,
  client_fname VARCHAR(50),
  client_lname VARCHAR(50),
  client_email VARCHAR(100)
);

💻 Application PHP

Le fichier index.php permet :

Connexion à MySQL

Lecture des clients

Affichage HTML dynamique

📸 Résultat

🔐 Sécurité

Améliorations possibles :

Utilisation d’un compte MySQL dédié

Variables d’environnement

HTTPS (TLS)

Restriction réseau

📚 Compétences démontrées

Déploiement cloud

Conteneurisation

Administration Linux

Gestion de base de données

Développement PHP

Réseau Azure

Documentation technique

👨‍💻 Auteur

Wassim Ben Younes
Infrastructure & Cybersécurité — AEC

