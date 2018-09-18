#Algorithm goes here
def astar(board):
    cell = board.start_cell
    opened = [] #Unexplored nodes, most promising nodes first sort by ascending f value
    closed = [] #Explored nodes
    g = 0
    h = cell.calculate_h(board)
    f = g + h
    opened.append(cell) #Legger inn startcellen
    cell.opened = True

    #agenda-loop
    while True:
        if len(opened) == 0: #Har feilet om opened blir tom
            return False
        cell = opened.pop() #Popper siste element i closed, altså det mest promising
        closed.append(cell) #Legger cellen i closed fordi den er explored
        cell.closed = True
        if cell.stop: #Suksess om man treffer stopp-cellen
            path = [cell]
            parent = cell.best_parent
            while not parent == None:
                path.append(parent)
                parent = parent.best_parent
            return path[::-1]
            #return cell

        adjacents = cell.get_adjacents() #Henter alle nabo-celler av cellen
        for succ in adjacents:
            #If node S* has previously been created, and if state(S*) = state(S), then S ← S*.
            cell.kids.append(succ) #push(S,kids(X))
            if not succ.opened and not succ.closed:
                attach_and_eval(succ, cell, board)
                opened = insert_ascending(opened, succ)
            elif cell.g + succ.cost < succ.g:
                attach_and_eval(succ, cell, board)
                if succ.closed:
                    propagate_path_improvements(succ)
            


def insert_ascending(l, cell):
    for i in range(len(l)):
        i_cell = l[i]
        if cell.f <= i_cell.f:
            l.insert(i, cell)
            cell.opened = True
            return l
    l.append(cell)
    cell.opened = True
    return l


def attach_and_eval(child, parent, board):
    child.set_parent(parent)
    child.g = parent.g + child.cost #arc cost på siste der enkli, mulig det skal være childcost istedet
    child.h = child.calculate_h(board)
    child.f = child.g + child.h

def propagate_path_improvements(parent):
    children = parent.kids
    for child in children:
        if parent.g + child.cost < child.g: #child.cost skal være arc-cost
            child.set_parent(parent)
            child.g = parent.g + child.cost #child.cost skal være arc-cost
            child.f = child.g + child.h
            propagate_path_improvements(child)



