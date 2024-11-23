import os
import subprocess

class TextToSpeechService :
    
    def lire_texte(texte, fichier_sortie="output.wav"):
        try:
            # Commande pour générer le fichier audio
            commande_pico = f'pico2wave -l fr-FR -w {fichier_sortie} "{texte}"'
            os.system(commande_pico)
            
            # Lecture du fichier généré
            subprocess.run(["aplay", fichier_sortie])
            
            # Optionnel : supprimer le fichier audio après lecture
            os.remove(fichier_sortie)
        except Exception as e:
            print(f"Erreur : {e}")