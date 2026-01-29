Déploiement Azure IoT \& Cosmos DB

1\. Création IoT Hub



Azure Portal



SKU: Free / Basic



Enregistrer les clés



2\. Création Cosmos DB



API: NoSQL



Partition Key: /deviceId



Key-based auth: Enabled



3\. Routing IoT Hub



Endpoint: Cosmos DB



Route: true



Source: Telemetry



4\. Sécurité



IP Firewall



Accès portail autorisé

