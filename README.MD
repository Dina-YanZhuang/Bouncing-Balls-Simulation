# Bouncing Balls Simulation (Pygame)

## 🧩 Overview
This project implements a modular **2D simulation of interactive bouncing balls** using the `pygame` library.  
It showcases **object-oriented design**, **randomized motion and color generation**, and **real-time user interaction** via keyboard input.

The simulation evolves across multiple versions (`ball.py` → `balls6.py`), each introducing new capabilities such as:
- Independent object behavior  
- Collision and boundary handling  
- Randomization of colors and trajectories  
- A controllable player object  

The final version (`balls6.py`) integrates all features into a cohesive, interactive environment resembling an arcade-style game.

---

## ⚙️ Requirements
- **Python 3.10+**
- **Pygame**

Install dependencies:
```bash
pip install pygame

## File Structure and Descriptions
ball.py

Basic version with multiple balls moving vertically.

Controlled via arrow keys; spacebar stops movement.

Demonstrates fundamental Pygame setup, event handling, and boundary constraints.

balls1.py

Adds horizontal movement using left/right arrow keys.

Prevents balls from leaving the window in any direction.

Establishes the foundation for full 2D control.

balls2.py

Introduces individual ball attributes:

Each ball has its own radius and randomly assigned color.

Removes global constants for size and color.

Demonstrates instance-based customization and randomization.

balls3.py

Adds independent motion for each ball:

Randomized directional velocities (dx, dy).

Balls bounce off window edges on collision.

Eliminates manual key control for autonomous animation.

balls4.py

Implements a randomize() method for each ball:

Randomly changes color and direction.

Adds keyboard interactions:

Press r to randomize all balls.

Press + to create a new randomly placed ball.

Demonstrates dynamic object creation and event-driven updates.

balls5.py

Introduces a Player class:

Player ball moves with continuous arrow-key input (pygame.key.get_pressed()).

Movement constrained to screen boundaries.

Serves as the foundation for user-controlled gameplay elements.

balls6.py

Final integrated version combining all prior functionality:

Autonomous moving balls and a controllable player.

Refactored motion logic into class methods (Ball.move(), Player.move()).

Simplified main loop for modularity and readability.

Produces a complete, interactive simulation.

prep_nn.py

Independent script implementing a minimal neural network forward pass.

Includes functions for weighted summation (z), ReLU activation (r), and feedforward computation (f_pass).

Demonstrates procedural decomposition and vector-based operations.

How to Run

Each file can be executed independently:

python balls6.py


Controls:

ESC → Quit

r → Randomize all balls

+ → Add a new ball

Arrow keys → Move the player (in balls5.py and balls6.py)

Key Features

Object-oriented simulation with encapsulated state and behavior.

Real-time animation and keyboard interaction using pygame.

Collision detection and randomized dynamics.

Extendable design for game or visual simulation prototypes.
