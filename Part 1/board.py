from cell import Cell
from PIL import Image

class Board:

    def __init__(self, filename):
        self.board = self.read_file(filename)
        self.set_adjacents()
        self.goal_coords
        self.start_cell

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
                elif c == "A":
                    self.start_cell = cell
            result.append(linelist)
        return result
    
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

    def boardToImage(self):
        xc = len(self.board[0])
        yc = len(self.board)
        img = Image.new("RGB",(xc,yc),(255,255,255))
        for x in range(xc):
            for y in range(yc):
                cell = self.board[y][x]
                img.putpixel((x,y),cell.get_color(cell.c))
        img.show()

    def path_image(self, closed):
        xc = len(self.board[0])
        yc = len(self.board)
        img = Image.new("RGB",(xc,yc),(255,255,255))
        for x in range(xc):
            for y in range(yc):
                cell = self.board[y][x]
                img.putpixel((x,y),cell.get_color(cell.c))

        for c in closed:
            img.putpixel(c.coords, (255,0,0))
        img = img.resize((xc*25,yc*25 ), Image.ANTIALIAS)
        img.show()
    
    def path_repr(self, closed):
        b = self.board
        for c in closed:
            coo = c.coords
            b[coo[1]][coo[0]] = "*"
        s = ""
        for line in b:
            for c in line:
                s += str(c)
            s+="\n"
        return s

        

b = Board("board-1-1.txt")

#b.boardToImage()


                
        