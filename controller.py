import time
from model import GameEngine, Scoreboard, Player
from view import ConsoleInterface

class GameController:
    """Clase mediadora que controla el ciclo de vida del software (Cumple RNF-01)"""
    def __init__(self):
        self.engine = GameEngine()
        self.scoreboard = Scoreboard()
        self.view = ConsoleInterface()
        self.player = None

    def start(self):
        """Inicia el bucle de ejecución principal del sistema de software"""
        self.view.show_welcome()
        
        # Bucle obligatorio hasta registrar un nombre no vacío
        name = ""
        while not name:
            name = self.view.get_player_name()
        
        self.player = Player(name)
        
        # Estructura repetitiva de control de partidas continuas (Paso 2)
        while True:
            selection = self.view.get_player_move()
            
            if selection == "Salir":
                print(f"\nGracias por jugar. Desarrollo finalizado con éxito para {self.player.name}.")
                break
                
            if selection == "Reiniciar":
                self.scoreboard.reset()
                self.view.show_reset_notification()
                continue
            
            # Captura de tiempo inicial para comprobar Eficiencia Temporal (Cumple RNF-02)
            start_time = time.time()
            
            # Ejecución de operaciones lógicas de negocio
            cpu_move = self.engine.generate_cpu_move()
            outcome = self.engine.evaluate_round(selection, cpu_move)
            
            # Actualización del estado según el resultado de la ronda
            if outcome == "Victoria":
                self.scoreboard.wins += 1
            elif outcome == "Derrota":
                self.scoreboard.losses += 1
            else:
                self.scoreboard.ties += 1
            
            # Cálculo exacto de la latencia en milisegundos
            end_time = time.time()
            elapsed_ms = (end_time - start_time) * 1000
            
            # Envío de la información procesada a la vista para su representación gráfica
            self.view.show_result(
                self.player.name, selection, cpu_move, outcome, self.scoreboard, elapsed_ms
            )