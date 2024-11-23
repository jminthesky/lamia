import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
from button_service import ButtonMatrixService
import json
from text_to_speech_service import TextToSpeechService
import os







GPIO.setmode(GPIO.BCM)

# Initialisation des pins GPIO et du lecteur RFID
reader = SimpleMFRC522()


try:
    
  # Charger la configuration
  with open("config.json", "r") as f:
      config = json.load(f)

  # Extraire la configuration de la matrice et des options
  button_config = config["button_matrix"]
  rows_pins = button_config["rows_pins"]
  cols_pins = button_config["cols_pins"]


  # Initialiser le service avec la configuration
  ButtonMatrixService.setup(rows_pins, cols_pins)


  while True :
      #print("Approchez votre carte RFID du lecteur")
      #id, text = reader.read()
      id = reader.read_id_no_block()

      #print(f"ID de la carte: |{id}|")
      #print(f"")

      if str(id) == "584197378814":
        TextToSpeechService.lire_texte("Salut Robin! Comment ça va?")
      if str(id) == "138270518058":
        TextToSpeechService.lire_texte("Salut Alban! Comment ça va?...")
      if str(id) == "783538561520":
        TextToSpeechService.lire_texte("Salut Jean-Mi! Comment ça va?")


      # Détecter les boutons pressés
      pressed = ButtonMatrixService.detect_buttons()
      if pressed:
        print(f"Boutons pressés : {pressed}")
        if 1 in pressed:
          os.system("mpg123 mib.mp3")
 

      time.sleep(0.1)
      
except KeyboardInterrupt:
    print("Opération interrompue.")
finally:
    GPIO.cleanup()


