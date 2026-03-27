
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
    permutations = []
    for index, caja in enumerate(cajas):
        permutations.append(Box(index=index, x=min(caja[0], caja[1]), y=max(caja[0], caja[1]), z=caja[2]))
        permutations.append(Box(index=index, x=min(caja[2], caja[1]), y=max(caja[2], caja[1]), z=caja[0]))
        permutations.append(Box(index=index, x=min(caja[2], caja[0]), y=max(caja[2], caja[0]), z=caja[1]))

    permutations.sort(key=lambda box: box.x * box.y, reverse=True)
    
    opt = [0] * len(permutations)
    previous = [None] * len(permutations)

    for i in range(1, len(permutations)):
        max_local_height = permutations[i].z
        
        for j in range(1, i - 1):
            if permutations[i].x < permutations[j].x and permutations[i].y < permutations[j].y:
                if opt[j] + permutations[i].z > max_local_height:
                    max_local_height = opt[j] + permutations[i].z
                    previous[i] = j
            
        opt[i] = max_local_height
    
    max_global_height = 0
    last_box_index = 0
    
    for i in range(0, len(permutations)):
        if opt[i] > max_global_height:
            max_global_height = opt[i]
            last_box_index = i
    
    tower_top = permutations[last_box_index]
    tower = deque([(tower_top.index, (tower_top.x, tower_top.y))])
    index = last_box_index
    
    while previous[index]: 
        box = permutations[previous[index]]
        tower.appendleft((box.index, (box.x, box.y)))
        index = previous[index]
    
    return [max_global_height, list(tower)]
