from collections.abc import Sequence
from dataclasses import dataclass
from collections import deque


@dataclass
class Box:
    index: int
    
    x: float
    y: float
    z: float


def main(cajas: Sequence[tuple[float, float, float]]) -> tuple[float, list[tuple[int, tuple[float, float]]]]:
    rotations = []
    for index, caja in enumerate(cajas):
        rotations.append(Box(index=index, x=min(caja[0], caja[1]), y=max(caja[0], caja[1]), z=caja[2]))
        rotations.append(Box(index=index, x=min(caja[2], caja[1]), y=max(caja[2], caja[1]), z=caja[0]))
        rotations.append(Box(index=index, x=min(caja[2], caja[0]), y=max(caja[2], caja[0]), z=caja[1]))

    rotations.sort(key=lambda box: box.x * box.y, reverse=True)
    
    opt = [0] * len(rotations)
    previous = [None] * len(rotations)
    opt[0] = rotations[0].z
    
    for i in range(1, len(rotations)):
        max_local_height = rotations[i].z
        
        for j in range(0, i - 1):
            if rotations[i].x < rotations[j].x and rotations[i].y < rotations[j].y:
                if opt[j] + rotations[i].z > max_local_height:
                    max_local_height = opt[j] + rotations[i].z
                    previous[i] = j
            
        opt[i] = max_local_height

    max_global_height = 0
    last_box_index = 0
    
    for i in range(0, len(rotations)):
        if opt[i] > max_global_height:
            max_global_height = opt[i]
            last_box_index = i
    
    tower_top = rotations[last_box_index]
    tower = deque([(tower_top.index, (tower_top.x, tower_top.y))])
    index = last_box_index
    
    while previous[index] is not None: 
        box = rotations[previous[index]]
        tower.appendleft((box.index, (box.x, box.y)))
        index = previous[index]
    
    return [max_global_height, list(tower)]
