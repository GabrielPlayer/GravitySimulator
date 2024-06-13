# GravitySimulator

## Overview

**GravitySimulator** is a 2D gravitational simulation created using Python and Pygame. The project simulates the gravitational attraction between planets and allows users to interact with the system by creating, destroying, and observing the orbits of celestial bodies. The simulation aims to provide an intuitive and engaging way to visualize the dynamics of planetary motion and gravitational interactions.

## Key Features

- **Create and Destroy Planets:** Easily add new planets to the simulation with a left-click and remove them with a right-click.
- **Dynamic Camera Controls:** Zoom in and out using the scroll wheel and move the camera view with arrow keys to explore the simulation space.
- **Pause and Resume:** Pause the simulation with the space bar to closely examine planetary movements and interactions.
- **Orbit Visualization:** Observe the realistic orbits of the planets as they move under gravitational forces.
- **Intuitive Interaction:** A user-friendly interface for exploring and manipulating the simulation environment.

## Installation

To run **GravitySimulator**, you need to have Python installed on your system. The required libraries are listed in the `requirements.txt` file.

### Prerequisites

- Python 3.12
- Pygame library

### Installing Dependencies

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/GabrielPlayer/GravitySimulator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd GravitySimulator
    ```

3. Install the required libraries using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Simulation

To start the simulation, simply run the `main.py` file:

```bash
python main.py
```
No additional command-line arguments are needed.

## Usage Instructions

### Controls

- **Create Planet**: Left-click in the simulation window to create a new planet at the cursor's location.
- **Destroy Planet**: Right-click on a planet to remove it from the simulation.
- **Zoom In/Out**: Use the scroll wheel to zoom in and out of the scene.
- **Move Camera**: Use the arrow keys to pan the camera view around the simulation space.
- **Pause/Resume**: Press the space bar to pause or resume the simulation.

## Simulation Mechanics

GravitySimulator models the gravitational interactions between planets based on their masses. The planets are attracted to each other following Newton's law of universal gravitation. Each planet's mass determines its gravitational pull and influences its orbit.

## Scaling and Visualization

- The radius of each planet is scaled proportionally based on its mass. However, due to the significant mass difference between the Sun and smaller planets like Earth, there is a noticeable size discrepancy, making Earth-like planets appear very small relative to the Sun.
- The camera zoom and movement allow you to explore different parts of the simulation and observe planets at various scales.

## Known Issues and Limitations

- **Planet Size Discrepancy**: Due to the high mass of the Sun compared to smaller planets, planets like Earth appear disproportionately small. This issue arises from scaling the radius directly based on mass.
- **Performance**: Adding a large number of planets may impact the simulation's performance, especially on lower-end systems.
