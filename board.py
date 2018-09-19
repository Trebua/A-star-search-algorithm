from cell import Cell
from PIL import Image, ImageDraw, ImageFont

class Board:

    #Initializes board with file, and finds adjacent cells (N,S,E,W)
    def __init__(self, filename):
        self.board = self.read_file(filename)
        self.set_adjacents()
        self.goal_coords
        self.start_cell

    #Reads file from boards and finds coordinates of start and goal
    def read_file(self, filename):
        path = "boards/" + filename
        f = open(path, "r")
        result = []
        for l in f:
            l = l.replace("\n", "")
            linelist = []          
            for c in l:
                cell = Cell(c, len(linelist), len(result))
                linelist.append(cell)
                if c == "B":
                    self.goal_coords = (linelist.index(cell), len(result))
                elif c == "A":
                    self.start_cell = cell
            result.append(linelist)
        return result
    
    #Finds all adjacent cells for every cell
    def set_adjacents(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                cell = self.board[i][j]
                adj = []
                adj.append(self.try_coords(i-1,j))
                adj.append(self.try_coords(i,j-1))
                adj.append(self.try_coords(i+1,j))
                adj.append(self.try_coords(i,j+1))
                for k in range(4):
                    if not adj[k] == 0:
                        cell.add_adjacent(adj[k])

    #Checks if coordinates is withing board constraints
    def try_coords(self,i,j):
        if i < 0 or j < 0 or i > len(self.board)-1 or j > len(self.board[0])-1:
            return 0
        return self.board[i][j]
   
    def __str__(self):
        res = ""
        for line in self.board:
            for c in line:
                res += str(c)
            res += "\n"
        return res

    #Generates visualization for a board with PILLOW. Colors are specified in cells
    def board_to_image(self, path):
        xp = len(self.board[0])
        yp = len(self.board)
        width = 100 * xp
        height = 100 * yp
        img = Image.new("RGB", size=(width, height), color=255)
        font = ImageFont.truetype("arial_narrow_7.ttf", 100)
        draw = ImageDraw.Draw(img)
        xstep = width/xp
        ystep = height/yp
        x = 0
        y = 0
        for row in self.board:
            for cell in row:
                color = cell.color
                draw.rectangle((x*xstep, y*ystep, xstep*(x+1), ystep*(y+1)), color)
                if cell.start or cell.stop:
                    text = "A" if cell.start else "B"
                    draw.text(((x+0.3)*xstep, (y+0.12)*ystep),text,(255,255,255), font)
                if cell in path and (not cell.start and not cell.stop):
                    draw.rectangle(((x+0.25)*xstep, (y+0.25)*ystep, xstep*(x+0.75), ystep*(y+0.75)), "yellow")
                x = (x+1)%len(self.board[0])
                if x == 0:
                    y += 1
        del draw
        img.show()
                
        