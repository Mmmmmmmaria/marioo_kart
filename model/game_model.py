from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile
from model.terrain import Ice
from model.terrain import Void


class GameModel:

    def __init__(self):
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car: Car | None = None

    def load_circuit(self) -> None:
        grid = [[RoadTile(col=col_idx, row=row_idx)
                for row_idx in range(GRID_COLS)] for col_idx in range(GRID_ROWS)]
        for row in range (2, 6):
            for col in range (3, 7):
                grid[row][col] = RoadTile(col = col, row = row, terrain = Ice())        
        self.circuit = Circuit(grid=grid)
        self.spawn_car()

    def spawn_car(self) -> None:
        self.car = Car(7, 1)
        # enregistrement des trois informations nécessaires à la téléportation
        self.last_checkpoint = (self.car.x, self.car.y, self.car.angle)

    def update(self) -> None:
        if self.state != GameState.RACING or self.circuit is None:
            return
        
        # identifier le terrain sur lequel se trouve la voiture
        case = self.circuit.get_tile_at_pixel(self.car.x, self.car.y)
        if case is not None : 
            terrain = case.terrain
        else :
            terrain = Void() 
        # déclencher la téléportation    
        if terrain.est_vide:
            x, y, cap = self.last_checkpoint
            self.car.teleporter_vers(x, y, cap)
            return 
            # return permet de quitter la méthode update après la téléportation                                        
        
    
           
