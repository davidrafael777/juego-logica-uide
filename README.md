# 🎮 El Impacto de las Nuevas Tecnologías en la Sociedad: Desarrollo y Proyección de Soluciones Informáticas

## 📝 Caso de Estudio: Sistema Automatizado e Interactivo "Piedra, Papel o Tijera" bajo Arquitectura MVC y Teoría de Juegos

---

### 👤 Información del Integrante
*   **Autor:** David Rafael Dueñas Ripalda
*   **Institución:** Universidad Internacional del Ecuador (UIDE)
*   **Facultad:** Facultad de Ingenierías Digitales y Tecnologías Emergentes
*   **Escuela:** Ingeniería en Inteligencia Artificial
*   **Asignatura:** LÓGICA DE PROGRAMACIÓN 1-SIN-1B
*   **Docente Tutor:** Mgs. Estefanía Vanessa Heredia Jiménez
*   **Fecha:** Junio 2026

---

## 🎯 1. Objetivo del Sistema
El propósito fundamental de este sistema es diseñar e implementar una solución informática modular y de acoplamiento débil para el juego de lógica clásica "Piedra, Papel o Tijera". El software busca:
1.  **Validar la separación de responsabilidades** mediante la aplicación estricta del patrón de diseño arquitectónico **Modelo-Vista-Controlador (MVC)**, garantizando que el núcleo lógico sea 100% independiente de la interfaz de usuario.
2.  **Simular un entorno estratégico justo y equitativo** aplicando los conceptos matemáticos del *Equilibrio de Nash* (Teoría de Juegos) a través de un Generador de Números Pseudoaleatorios (PRNG) con una distribución de probabilidad uniforme (P = 1/3).
3.  **Evidenciar el impacto de las nuevas tecnologías** en la resolución automatizada de conflictos lúdicos y la correcta persistencia temporal del estado del sistema (control de marcadores y sesiones).

---

## 🚀 2. Descripción de Funcionalidades
El sistema interactivo despliega las siguientes capacidades operativas y funcionales:

*   **RF-01 (Gestión de Identidad):** Captura de forma síncrona el nombre o identificador del jugador para personalizar los mensajes de la interfaz, reportes de rondas e historial de la sesión.
*   **RF-02 (Captura y Validación de Entradas):** Filtra y restringe los comandos de consola del usuario periférico, admitiendo únicamente jugadas lícitas y válidas (Piedra, Papel o Tijera) y mitigando excepciones por datos erróneos.
*   **RF-03 (Toma de Decisiones Inteligente de la CPU):** Determina la acción del oponente informático en tiempo de ejecución de manera puramente estocástica (aleatoria uniforme), impidiendo la predicción de patrones por parte del humano.
*   **RF-04 (Motor de Reglas de Negocio):** Contrata de forma determinista la jugada concurrente del usuario contra la de la CPU basándose en la matriz de pagos clásica para dictaminar inmediatamente el estado de la ronda (Victoria, Derrota o Empate).
*   **RF-05 (Persistencia de Estado del Marcador):** Gestiona e incrementa de manera continua en memoria local el contador de partidas ganadas, perdidas y empatadas durante el ciclo de vida de la sesión activa.
*   **RF-06 (Inicialización / Reset):** Provee una función explícita dentro del menú para limpiar el marcador general de partidas y restablecer todos los contadores lógicos a cero sin necesidad de reiniciar la aplicación.

---

## 🏗️ 3. Arquitectura del Software (Patrón MVC)
Para cumplir con el requerimiento de acoplamiento débil, el código fuente está rígidamente fragmentado en tres componentes o capas independientes:

1.  **Capa de Dominio (Modelo):** Contiene las entidades base y el motor algorítmico central del sistema.
    *   `Player`: Administra la identidad del usuario.
    *   `CPUOpponent`: Ejecuta la lógica matemática probabilística de selección uniforme.
    *   `Scoreboard`: Salvaguarda los datos mutables del marcador.
    *   `GameEngine`: Aplica las reglas lógicas para resolver los enfrentamientos.
2.  **Capa de Presentación (Vista):** Administra los canales de Entrada/Salida (E/S).
    *   `ConsoleInterface` / `InputScanner`: Lee las pulsaciones del teclado y renderiza los menús de texto de forma ordenada.
3.  **Capa de Control (Controlador):** El núcleo orquestador intermedio.
    *   `GameController`: Atrapa los estímulos de la Vista, invoca los cambios de estado en el Modelo y ordena la actualización de la pantalla de interfaz.

---

**[Enlace Oficial a las Evidencias del Proyecto (Video y Capturas)](https://photos.app.goo.gl/MG1PMoomo43QG9dh8)**

---

## ⚙️ 4. Estructura del Repositorio y Archivos
El proyecto está organizado bajo la estructura modular estándar:
```bash
├── src/
│   ├── modelo/
│   │   ├── Player.py
│   │   ├── CPUOpponent.py
│   │   ├── Scoreboard.py
│   │   └── GameEngine.py
│   ├── vista/
│   │   └── ConsoleInterface.py
│   └── controlador/
│       └── GameController.py
├── diagramas/
│   ├── diagrama_casos_uso.png    # Límites lógicos del sistema (UML)
│   └── diagrama_arquitectura.png # Flujo de capas del patrón MVC
├── Main.py                       # Punto de entrada del programa
└── README.md                     # Documentación técnica obligatoria


