def dijkstra(board):
    opened, closed = list(), list() #Lager tomme opened- og closed-lister
    cell = board.start_cell #Setter start-cellen
    cell.g = 0
    cell.h = cell.calculate_h(board) #Regner ut heuristisk cost, manhattan distance
    cell.f = cell.g + cell.h #Regner ut f, summen av pathcost og heurestikk
    opened.append(cell) #Legger inn startcellen i open
    cell.opened = True
    
    while True: #agenda-loop
        if len(opened) == 0: #Har feilet om opened blir tom
            return False
        cell = opened.pop(0) #Popper første element i opened, altså det mest lovende
        closed.append(cell) #Legger cellen i closed fordi den er explored
        cell.closed = True
        if cell.stop: #Søk er ferdig om man treffer stopp-cellen
            path = [cell] #Lager liste for beste vei fra A til B
            parent = cell.best_parent #Går gjennom alle sine beste parents
            while not parent == None:
                path.append(parent)
                parent = parent.best_parent
            return path[::-1] #Returnerer pathen i omvendt rekkefølge, fra A til B

        adjacents = cell.get_adjacents() #Henter alle nabo-celler av cellen
        for succ in adjacents: #Går gjennom alle successors/naboceller
            if not succ.opened and not succ.closed:  #Hvis ikke successor er åpnet eller lukket, regn ut childs f
                attach_and_eval(succ, cell, board)
                opened = insert_ascending(opened, succ) #Legg inn successor i opened, med mest lovende først
            elif cell.g + succ.cost < succ.g: #Ser om parent og childs lengde er indre enn successors lengde
                attach_and_eval(succ, cell, board) #Regner ut f for successor og setter cell som parent
                if succ.closed:
                    propagate_path_improvements(succ) #Hvis succ er closed, oppdater alle children of childrens f
            
#Legger celle i liste, i stigende g-verdi
def insert_ascending(l, cell):
    for i in range(len(l)):
        i_cell = l[i]
        if cell.g <= i_cell.g:
            l.insert(i, cell)
            cell.opened = True
            return l
    l.append(cell)
    cell.opened = True
    return l

#Setter childs parent og regner ut childs f
def attach_and_eval(child, parent, board):
    child.set_parent(parent)
    child.g = parent.g + child.cost 
    child.h = child.calculate_h(board)
    child.f = child.g + child.h

#Går gjennom barn av barn til en parent og regner f på nytt
def propagate_path_improvements(parent):
    children = parent.get_adjacents()
    for child in children:
        if parent.g + child.cost < child.g: 
            child.set_parent(parent)
            child.g = parent.g + child.cost
            child.f = child.g + child.h
            propagate_path_improvements(child)



