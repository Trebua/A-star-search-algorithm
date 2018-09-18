#Algorithm goes here
def astar(cell, board):
    opened = [] #Unexplored nodes, most promising nodes first
    closed = [] #Explored nodes
    g = 0
    h = cell.calculate_h(board)
    f = g + h
    opened.append(cell) #Legger inn startcellen

    #agenda-loop
    while True:
        if len(opened) == 0: #Har feilet om opened blir tom
            return False
        cell = opened.pop() #Popper siste element i closed, altså det mest promising
        closed.append(cell) #Legger cellen i closed fordi den er explored
        if cell.stop: #Suksess om man treffer stopp-cellen
            return cell

        adjacents = cell.get_adjacents() #Henter alle nabo-celler av cellen
        for cell in adjacents: #Legger alle celler som ikke allerede er åpnet eller lukket inn i opened
            if cell not in opened and cell not in closed:
                opened.append(cell)

def attach_and_eval(child, parent, board):
    child.set_parent(parent)
    child.g = parent.g + child.cost #arc cost på siste der enkli, mulig det skal være childcost istedet
    child.h = child.calculate_h(board)
    child.f = child.g + child.h

def propagate_path_improvements(parent):
    children = parent.get_adjacents()
    for child in children:
        if parent.g + child.cost < child.g: #child.cost skal være arc-cost
            child.set_parent(parent)
            child.g = parent.g + child.cost #child.cost skal være arc-cost
            child.f = child.g + child.h
            propagate_path_improvements(child)



