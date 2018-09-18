from cell import Cell
from PIL import Image

class Board:

    def __init__(self, filename):
        self.board = self.read_file(filename)
        self.set_adjacents()
        self.goal_coords

    def read_file(self, filename):
        path = "boards/" + filename
        f = open(path, "r")
        result = []
        for l in f:
            l = l.replace("\n", "")
            linelist = []          
            for c in l:
                cell = Cell(c, len(linelist), len(result)) #Legger til index på celle
                linelist.append(cell)
                if c == "B":
                    self.goal_coords = (linelist.index(cell), len(result)) #Gir forhåpentligvis koordinatene til B
            result.append(linelist)
        return result
    
    def set_adjacents(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                cell = self.board[i][j]
                adj = []
                adj.append(try_coords[i-1][j])
                adj.append(try_coords[i][j-1])
                adj.append(try_coords[i+1][j])
                adj.append(try_coords[i][j+1])
                for k in range(4):
                    if not adj[k] == 0:
                        cell.add_adjacent(adj[k])

    def try_coords(i,j):
        try:
            return self.board[i][j]
        except:
            return 0
   
    def __str__(self):
        res = ""
        for line in self.board:
            for c in line:
                res += str(c)
            res += "\n"
        return res

    def boardToImage(self):
        xc = len(self.board[0])
        yc = len(self.board)
        img = Image.new("RGB",(xc,yc),(255,255,255))
        for x in range(xc):
            for y in range(yc):
                cell = self.board[y][x]
                img.putpixel((x,y),cell.get_color(cell.c))
        img.show()
        

b = Board("board-1-1.txt")

#b.boardToImage()


                
        