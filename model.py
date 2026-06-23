import random

class Player:
    """Clase que representa al usuario jugador (Cumple RF-01)"""
    def __init__(self, name: str):
        self.name = name

class Scoreboard:
    """Clase encargada de la persistencia y gestión de puntuaciones (Cumple RF-05)"""
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def reset(self):
        """Reinicia las variables del marcador general a cero (Cumple RF-06)"""
        self.wins = 0
        self.losses = 0
        self.ties = 0

class GameEngine:
    """Clase que procesa las reglas del negocio y la lógica de la CPU"""
    def __init__(self):
        self.options = ["Piedra", "Papel", "Tijera"]

    def generate_cpu_move(self) -> str:
        """
        Genera la jugada de la CPU utilizando un algoritmo pseudoaleatorio (PRNG).
        Garantiza que la probabilidad uniforme sea de 1/3 para simular con total
        exactitud el Equilibrio de Nash en interacciones de suma cero (Cumple RF-03).
        """
        return random.choice(self.options)

    def evaluate_round(self, player_move: str, cpu_move: str) -> str:
        """
        Contrasta de manera síncrona las jugadas concurrentes para resolver la ronda.
        Aplica estructuras condicionales estrictas para dictaminar el ganador (Cumple RF-04).
        """
        if player_move == cpu_move:
            return "Empate"
        
        # Aplicación de combinaciones de victoria del jugador humano
        if (player_move == "Piedra" and cpu_move == "Tijera") or \
           (player_move == "Papel" and cpu_move == "Piedra") or \
           (player_move == "Tijera" and cpu_move == "Papel"):
            return "Victoria"
        else:
            return "Derrota"