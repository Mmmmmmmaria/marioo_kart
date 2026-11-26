from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile
from model.terrain import Road, Ice, Grass, Dirt, Void, Sand
from constants import TILE_SIZE
from model.car import Car, CATALOGUE_VOITURES


class GameModel:

    def __init__(self):
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car: Car | None = None

    def load_circuit(self) -> None:
        grid = [[RoadTile(col=col_idx, row=row_idx)
                for row_idx in range(GRID_COLS)] for col_idx in range(GRID_ROWS)]       
        self.circuit = Circuit(grid=grid)
        self.spawn_car()

    def spawn_car(self) -> None:
        self.car = Car(
            1, CATALOGUE_VOITURES[0],
            7 * TILE_SIZE + TILE_SIZE // 2,
            1 * TILE_SIZE + TILE_SIZE // 2,
            0
        )
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
        
    
           
