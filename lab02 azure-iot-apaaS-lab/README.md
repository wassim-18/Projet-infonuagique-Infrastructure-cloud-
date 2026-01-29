📌 Azure IoT aPaaS Lab — Data Pipeline & Visualization
🎯 Objectif

Mettre en place une architecture IoT complète sur Microsoft Azure permettant :

La collecte de données capteurs simulées

Le routage via Azure IoT Hub

Le stockage dans Azure Cosmos DB

La visualisation via une application Web Flask

🏗 Architecture

🛠 Technologies utilisées

Azure IoT Hub

Azure Cosmos DB (NoSQL API)

Python 3

Flask

Azure SDK for Python

GitHub

🔄 Pipeline de données
Python Simulator → IoT Hub → Cosmos DB → Flask WebApp → Browser

📁 Structure du projet
azure-iot-apaaS-lab/
├── docs/        # Captures d’écran
├── infra/       # Procédures Azure
├── python/      # Simulation IoT
├── webapp/      # Application Web

⚙️ Installation
1. Cloner le projet
git clone https://github.com/wassim-18/azure-iot-apaaS-lab.git
cd azure-iot-apaaS-lab

2. Installer les dépendances
pip install azure-iot-device azure-cosmos flask

3. Variables d’environnement

Sous PowerShell :

$env:COSMOS_CONNSTR="YOUR_CONNECTION_STRING"

▶️ Exécution
Lancer le simulateur IoT
python python/send_telemetry.py

Lancer le serveur Web
python webapp/app.py


Accès :

http://localhost:5000

📊 Résultat

Les données température/humidité sont affichées en temps réel depuis Cosmos DB.

Voir /docs/screenshots/.

🔐 Sécurité

Authentification par clé Cosmos DB

Pare-feu IP Azure

Accès restreint

👨‍💻 Auteur

Wassim Ben Younes
Étudiant — Infrastructure & Cybersécurité
GitHub: https://github.com/wassim-18

📜 Licence

Projet académique — Usage éducatif.