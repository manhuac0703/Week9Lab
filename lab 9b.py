
"""
Created on Fri May 16 11:29:29 2024

@author: manhuachen
"""

#Manhua Chen and Duoshu Xu
import numpy as np

class Agent():
    def __init__(self, world):
        self.world = world
        self.location = None

    def move(self):
        """Find a vacant spot and move to it."""
        vacant = self.world.find_vacant()
        if vacant is not None:
            self.world.grid[self.location] = None
            self.world.grid[vacant] = self
            self.location = vacant

class World:
    def __init__(self, size, num_agents):
        self.size = size
        self.grid = { (x, y): None for x in range(size[0]) for y in range(size[1]) }
        self.agents = [Agent(self) for _ in range(num_agents)]
        self.init_world()

    def init_world(self):
        """Place agents in random initial locations."""
        for agent in self.agents:
            loc = self.find_vacant()
            if loc is None:
                raise ValueError("Not enough space to place all agents.")
            self.grid[loc] = agent
            agent.location = loc

    def find_vacant(self):
        """Return a random vacant location from the grid."""
        vacant_spots = [loc for loc, occupant in self.grid.items() if occupant is None]
        if vacant_spots:
            index = np.random.choice(len(vacant_spots))  # Get a random index
            return vacant_spots[index]
        return None

    def run(self, num_iterations):
        """Run the simulation for a set number of iterations."""
        for _ in range(num_iterations):
            for agent in self.agents:
                agent.move()

params = {
    'size': (5, 5),    
    'num_agents': 5,    
    'num_iterations': 5  
}

world = World(params['size'], params['num_agents'])
world.run(params['num_iterations'])