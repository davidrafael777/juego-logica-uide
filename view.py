class ConsoleInterface:
    """Clase que interactúa directamente con la interfaz CLI del usuario"""
    
    def show_welcome(self):
        print("\n==================================================")
        print("    UNIVERSIDAD INTERNACIONAL DEL ECUADOR (UIDE)  ")
        print("  FACULTAD DE INGENIERÍAS DIGITALES Y TECNOLOGÍAS  ")
        print("==================================================")
        print("  Juego: Piedra, Papel o Tijera (Arquitectura MVC)")
        print("==================================================\n")

    def get_player_name(self) -> str:
        """Captura la identidad inicial del usuario (Cumple RF-01)"""
        return input("Por favor, ingrese su nombre de jugador: ").strip()

    def get_player_move(self) -> str:
        """
        Despliega el menú iterativo y captura una jugada válida.
        Implementa un bucle repetitivo para validar las entradas (Cumple RF-02).
        """
        while True:
            print("\n--- MENÚ DE JUEGO ---")
            print("1. Elegir Piedra")
            print("2. Elegir Papel")
            print("3. Elegir Tijera")
            print("4. Reiniciar Marcador General")
            print("5. Salir de la Aplicación")
            
            choice = input("Seleccione una opción (1-5): ").strip()
            
            if choice == "1": return "Piedra"
            if choice == "2": return "Papel"
            if choice == "3": return "Tijera"
            if choice == "4": return "Reiniciar"
            if choice == "5": return "Salir"
            
            print("[ERROR] Selección no válida. Por favor, intente de nuevo.")

    def show_result(self, name: str, p_move: str, c_move: str, result: str, score, elapsed_ms: float):
        """Muestra en pantalla el desenlace detallado de la ronda"""
        print("\n--------------------------------------------------")
        print(f" JUGADOR: {name} ({p_move}) vs COMPUTADORA ({c_move})")
        print(f" RESULTADO DE LA RONDA: ¡{result.upper()}!")
        print("--------------------------------------------------")
        print(f" MARCADOR GENERAL ACUMULADO:")
        print(f"   Partidas Ganadas: {score.wins}")
        print(f"   Partidas Perdidas: {score.losses}")
        print(f"   Partidas Empatadas: {score.ties}")
        print("--------------------------------------------------")
        print(f" Eficiencia Temporal: {elapsed_ms:.4f} ms (Límite: 100ms)")
        print("--------------------------------------------------\n")

    def show_reset_notification(self):
        print("\n[NOTIFICACIÓN] El marcador general se ha inicializado a cero.")