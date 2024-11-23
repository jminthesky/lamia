import RPi.GPIO as GPIO


class ButtonMatrixService:
    # Variables de classe
    rows_pins = []
    cols_pins = []

    @classmethod
    def setup(cls, rows_pins, cols_pins):
        """
        Initialise les broches.
        """
        cls.rows_pins = rows_pins
        cls.cols_pins = cols_pins

        # Configurer les GPIO
        GPIO.setmode(GPIO.BCM)
        cls._setup_matrix()

    @classmethod
    def _setup_matrix(cls):
        """
        Configure les rangées comme sorties et les colonnes comme entrées avec pull-up.
        """
        for row in cls.rows_pins:
            GPIO.setup(row, GPIO.OUT)
            GPIO.output(row, GPIO.LOW)
        for col in cls.cols_pins:
            GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    @classmethod
    def _calculate_button_id(cls, row_index, col_index):
        """
        Calcule dynamiquement l'ID du bouton pressé.
        """
        num_cols = len(cls.cols_pins)
        return row_index * num_cols + col_index + 1

    @classmethod
    def detect_buttons(cls):
        """
        Détecte les boutons pressés en parcourant la matrice.
        """
        pressed_buttons = []
        for row_index, row_pin in enumerate(cls.rows_pins):
            # Activer une rangée à la fois
            GPIO.output(row_pin, GPIO.HIGH)
            for col_index, col_pin in enumerate(cls.cols_pins):
                if GPIO.input(col_pin) == GPIO.LOW:  # Bouton pressé
                    button_id = cls._calculate_button_id(row_index, col_index)
                    pressed_buttons.append(button_id)
            GPIO.output(row_pin, GPIO.LOW)
        return pressed_buttons

    @classmethod
    def cleanup(cls):
        """
        Réinitialise les GPIO pour éviter les conflits.
        """
        GPIO.cleanup()
