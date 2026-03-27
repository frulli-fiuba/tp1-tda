

def main(turnos: list[tuple[int, int]]) -> tuple[list[int], int]:
    """
    1 - Ordeno por beneficio
    2 - Trato de asignar a cada solicitud el turno mas tarde posible antes del deadline
    3 - Si no hay lugar voy viendo mas temprano hasta encontrar turno libre o descarto  
    """
    slots = [None] * max(turnos, key=lambda x: x[0])[0]
    
    applications = [(index, *value) for index, value in enumerate(turnos)]
    applications.sort(key=lambda x: x[2], reverse=True)
    
    total_benefit = 0
    for application in applications:
        deadline = application[1]
        benefit = application[2]
        for x in range(deadline, 0, -1):
            if not slots[x-1]:
                slots[x-1] = application
                total_benefit += benefit
                break
	
    return [slot[0] for slot in slots if slot], total_benefit 
