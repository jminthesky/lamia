# Lamia
Voici un projet de programme python qui permet de réaliser un dispositif avec lecteur RFID et bouton multi interraction.
# Préparation d'un raspberry pi 
Installation de dietPi :
- Téléchargement de l'image depuis le site https://dietpi.com/
- Décompression et installation sur une carte SD avec Belena Etcher
- Modifier les fichiers dietpi et dietpi-wifi sur la carte SD

Activer SPI pour la communication avec le lecteur RFID:
sudo dietpi-config

Installation de python et des modules necessaire
sudo apt install python3-rpi.gpio

création d'un env python et installation du module python SimpleMFRC522


