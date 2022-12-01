import mesa

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from model import FireFlyWorld

COLORS = {
    "FLASHING": "#DAA520",
    "DARK": "#8B4513",
}


def portrayal(agent):
    if agent is None:
        return

    p = {
        "Shape": "circle",
        "r": 1,
        "Filled": "true",
        "Layer": 2,
        "Color": COLORS[agent.state],
        "text_color": "black"
    }

    return p


canvas_element = CanvasGrid(portrayal, 30, 30, 500, 500)

model_params = {
    "height": 30,
    "width": 30,
    "cycle_length": mesa.visualization.Slider("Cycle Length", 10, 0, 20, 1),
    "flashing_length": mesa.visualization.Slider("Flashing Length", 1, 0, 20, 1),
    "density": mesa.visualization.Slider("Density", 0.1, 0, 1, 0.1),
}

server = ModularServer(
    FireFlyWorld, [canvas_element], "Fireflies", model_params
)
