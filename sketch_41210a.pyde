import random

class Gameboard():
    def __init__(self):
        pass
    def draw(self):
        fill(255)
        strokeWeight(9)
        rect(100,50,620,620)
        line(100,205,720,205)
        line(100,360,720,360)
        line(100,515,720,515)
        line(255,50,255,670)
        line(410,50,410,670)
        line(565,50,565,670)

class Player_info():
    def __init__(self):
        self.plist=[]
        self.name = ""
        self.score = 0
        self.moves = 0
    def playername(self):
        self.name = p
        self.plist.append(self.name)
    def playerscore(self):
        self.score = sum_number
        self.plist.append(self.score)
    def playerlevel(self):
        self.moves = moves
        self.plist.append(self.moves)

class Username_board():
    def draw(self):
        fill(0)
        textSize(50)
        text("Username:",200,90)
        fill(255)
        strokeWeight(5)
        rect(500,40,550,70)
        strokeWeight(7)
        rect(50,180,1180,472)
        line(168,180,168,652)
        line(286,180,286,652)
        line(404,180,404,652)
        line(522,180,522,652)
        line(640,180,640,652)
        line(758,180,758,652)
        line(876,180,876,652)
        line(994,180,994,652)
        line(1112,180,1112,534)
        line(50,298,1230,298)
        line(50,416,1230,416)
        line(50,534,1230,534)
        fill(0)
        textSize(65)
        text("1",92,259)
        text("2",210,259)
        text("3",328,259)
        text("4",446,259)
        text("5",564,259)
        text("6",682,259)
        text("7",800,259)
        text("8",918,259)
        text("9",1036,259)
        text("0",1154,259)
        text("Q",82,377)
        text("W",200,377)
        text("E",328,377)
        text("R",446,377)
        text("T",564,377)
        text("Y",682,377)
        text("U",795,377)
        text("I",928,377)
        text("O",1030,377)
        text("P",1154,377)
        text("A",89,495)
        text("S",210,495)
        text("D",323,495)
        text("F",446,495)
        text("G",560,495)
        text("H",677,495)
        text("J",810,495)
        text("K",918,495)
        text("L",1036,495)
        text("Z",92,613)
        text("X",210,613)
        text("C",323,613)
        text("V",441,613)
        text("B",564,613)
        text("N",680,613)
        text("M",792,613)
        textSize(70)
        text("/",1147,494)
        textSize(100)
        text("_",900,611)
        textSize(50)
        text("Enter",1050,611)
        if counter%50<=25:
            fill(250,218,154)
            strokeWeight(0)
            rect(n+13,m+13,92,92)
            if n==994 and m==534:
                rect(1007,547,210,92)
            if n==1112 and m==534:
                rect(1007,547,210,92)
        if counter%50<=25:
            fill(0)
            textSize(65)
            if n==50 and m==180:
                text("1",92,259)
            if n==168 and m==180:
                text("2",210,259)
            if n==286 and m==180:
                text("3",328,259)
            if n==404 and m==180:
                text("4",446,259)
            if n==522 and m==180:
                text("5",564,259)
            if n==640 and m==180:
                text("6",682,259)
            if n==758 and m==180:
                text("7",800,259)
            if n==876 and m==180:
                text("8",918,259)
            if n==994 and m==180:
                text("9",1036,259)
            if n==1112 and m==180:
                text("0",1154,259)
            if n==50 and m==298:
                text("Q",82,377)
            if n==168 and m==298:
                text("W",200,377)
            if n==286 and m==298:
                text("E",328,377)
            if n==404 and m==298:
                text("R",446,377)
            if n==522 and m==298:
                text("T",564,377)
            if n==640 and m==298:
                text("Y",682,377)
            if n==758 and m==298:
                text("U",795,377)
            if n==876 and m==298:
                text("I",928,377)
            if n==994 and m==298:
                text("O",1030,377)
            if n==1112 and m==298:
                text("P",1154,377)
            if n==50 and m==416:
                text("A",89,495)
            if n==168 and m==416:
                text("S",210,495)
            if n==286 and m==416:
                text("D",323,495)
            if n==404 and m==416:
                text("F",446,495)
            if n==522 and m==416:
                text("G",560,495)
            if n==640 and m==416:
                text("H",677,495)
            if n==758 and m==416:
                text("J",810,495)
            if n==876 and m==416:
                text("K",918,495)
            if n==994 and m==416:
                text("L",1036,495)
            if n==1112 and m==416:
                textSize(70)
                text("/",1147,494)
            if n==50 and m==534:
                text("Z",92,613)
            if n==168 and m==534:
                text("X",210,613)
            if n==286 and m==534:
                text("C",323,613)
            if n==404 and m==534:
                text("V",441,613)
            if n==522 and m==534:
                text("B",564,613)
            if n==640 and m==534:
                text("N",680,613)
            if n==758 and m==534:
                text("M",792,613)
            if n==876 and m==534:
                textSize(100)
                text("_",900,611)
            if n>=994 and m==534:
                textSize(50)
                text("Enter",1050,611)
        textSize(50)
        fill(0)
        text(p,520,90)
        if colour2%510<=255:
            fill(colour,colour,colour)
            textSize(40)
            text("   Press ENTER to select         Press SPACE to delete",170,160)
        if colour2%510>=255:
            fill(255-colour,255-colour,255-colour)
            textSize(40)
            text("   Press ENTER to select         Press SPACE to delete",170,160)  
           

class Leaderboard():
    def __ini__(self):
        self.players = []
    def draw(self):
        fill(0)
        textSize(70)
        text(f,420,100)
        textSize(40)
        text("Rank",135,160)
        text("Name",390,160)
        text("Score",705,160)
        text("Moves",1000,160)
        textSize(30)
        text("1",170,205)
        text("2",170,250)
        text("3",170,295)
        text("4",170,340)
        text("5",170,385)
        text("6",170,430)
        text("7",170,475)
        text("8",170,520)
        text("9",170,565)
        text("10",170,610)
        if len(self.players)==1:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
        if len(self.players)==2:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250)   
        if len(self.players)==3: 
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250) 
            text(self.players[2][0],390,295)   
            text(self.players[2][1],710,295)
            text(self.players[2][2],1040,295)
        if len(self.players)==4:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250) 
            text(self.players[2][0],390,295)   
            text(self.players[2][1],710,295)
            text(self.players[2][2],1040,295)
            text(self.players[3][0],390,340)
            text(self.players[3][1],710,340)
            text(self.players[3][2],1040,340)
        if len(self.players)==5:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250) 
            text(self.players[2][0],390,295)   
            text(self.players[2][1],710,295)
            text(self.players[2][2],1040,295)
            text(self.players[3][0],390,340)
            text(self.players[3][1],710,340)
            text(self.players[3][2],1040,340)
            text(self.players[4][0],390,385)
            text(self.players[4][1],710,385)
            text(self.players[4][2],1040,385)
        if len(self.players)==6:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250) 
            text(self.players[2][0],390,295)   
            text(self.players[2][1],710,295)
            text(self.players[2][2],1040,295)
            text(self.players[3][0],390,340)
            text(self.players[3][1],710,340)
            text(self.players[3][2],1040,340)
            text(self.players[4][0],390,385)
            text(self.players[4][1],710,385)
            text(self.players[4][2],1040,385)
            text(self.players[5][0],390,430)
            text(self.players[5][1],710,430)
            text(self.players[5][2],1040,430)
        if len(self.players)==7:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250) 
            text(self.players[2][0],390,295)   
            text(self.players[2][1],710,295)
            text(self.players[2][2],1040,295)
            text(self.players[3][0],390,340)
            text(self.players[3][1],710,340)
            text(self.players[3][2],1040,340)
            text(self.players[4][0],390,385)
            text(self.players[4][1],710,385)
            text(self.players[4][2],1040,385)
            text(self.players[5][0],390,430)
            text(self.players[5][1],710,430)
            text(self.players[5][2],1040,430)
            text(self.players[6][0],390,475)
            text(self.players[6][1],710,475)
            text(self.players[6][2],1040,475)
        if len(self.players)==8:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250) 
            text(self.players[2][0],390,295)   
            text(self.players[2][1],710,295)
            text(self.players[2][2],1040,295)
            text(self.players[3][0],390,340)
            text(self.players[3][1],710,340)
            text(self.players[3][2],1040,340)
            text(self.players[4][0],390,385)
            text(self.players[4][1],710,385)
            text(self.players[4][2],1040,385)
            text(self.players[5][0],390,430)
            text(self.players[5][1],710,430)
            text(self.players[5][2],1040,430)
            text(self.players[6][0],390,475)
            text(self.players[6][1],710,475)
            text(self.players[6][2],1040,475)
            text(self.players[7][0],390,520)
            text(self.players[7][1],710,520)
            text(self.players[7][2],1040,520)
        if len(self.players)==9:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250) 
            text(self.players[2][0],390,295)   
            text(self.players[2][1],710,295)
            text(self.players[2][2],1040,295)
            text(self.players[3][0],390,340)
            text(self.players[3][1],710,340)
            text(self.players[3][2],1040,340)
            text(self.players[4][0],390,385)
            text(self.players[4][1],710,385)
            text(self.players[4][2],1040,385)
            text(self.players[5][0],390,430)
            text(self.players[5][1],710,430)
            text(self.players[5][2],1040,430)
            text(self.players[6][0],390,475)
            text(self.players[6][1],710,475)
            text(self.players[6][2],1040,475)
            text(self.players[7][0],390,520)
            text(self.players[7][1],710,520)
            text(self.players[7][2],1040,520)
            text(self.players[8][0],390,565)
            text(self.players[8][1],710,565)
            text(self.players[8][2],1040,565)
        if len(self.players)==10:
            text(self.players[0][0],390,205)
            text(self.players[0][1],710,205)
            text(self.players[0][2],1040,205)
            text(self.players[1][0],390,250)
            text(self.players[1][1],710,250)
            text(self.players[1][2],1040,250) 
            text(self.players[2][0],390,295)   
            text(self.players[2][1],710,295)
            text(self.players[2][2],1040,295)
            text(self.players[3][0],390,340)
            text(self.players[3][1],710,340)
            text(self.players[3][2],1040,340)
            text(self.players[4][0],390,385)
            text(self.players[4][1],710,385)
            text(self.players[4][2],1040,385)
            text(self.players[5][0],390,430)
            text(self.players[5][1],710,430)
            text(self.players[5][2],1040,430)
            text(self.players[6][0],390,475)
            text(self.players[6][1],710,475)
            text(self.players[6][2],1040,475)
            text(self.players[7][0],390,520)
            text(self.players[7][1],710,520)
            text(self.players[7][2],1040,520)
            text(self.players[8][0],390,565)
            text(self.players[8][1],710,565)
            text(self.players[8][2],1040,565)
            text(self.players[9][0],390,610)
            text(self.players[9][1],710,610)
            text(self.players[9][2],1040,610)

def writting():
    
    #///////////////////////write the number on the board///////////////////////
    for n in range(4):
        for m in range(4):
            if tilesnum[m][n] !=0 and tilesnum[m][n] < 128:
                textSize(80)
                fill(0)
                text(tilesnum[m][n],130+n*150,150+m*150)
            if tilesnum[m][n] ==0:
                fill(255)
                text(tilesnum[m][n],130+n*150,150+m*150)
            if tilesnum[m][n] >= 128 and tilesnum[m][n] < 1024:
                fill(0)
                textSize(60)
                text(tilesnum[m][n],130+n*150,150+m*150)
            if tilesnum[m][n] >= 1024:
                fill(0)
                textSize(40)
                text(tilesnum[m][n],130+n*150,150+m*150)

            


def add_tile_2():
    
    #////////////////////////////add a tile 2 into the board, search and recurse/////////////////////////////////
    
    ran_int = random.randint(1,16)
    if ran_int == 1:
        if tilesnum[0][0] == 0 :
            tilesnum[0][0] = random.randint(1,16)
            if tilesnum[0][0]>14:
                tilesnum[0][0]=4
            else:
                tilesnum[0][0]=2
        else:
            #RECURSION
            add_tile_2()
    elif ran_int == 2: 
        if tilesnum[0][1] == 0 :
            tilesnum[0][1] = random.randint(1,16)
            if tilesnum[0][1]>14:
                tilesnum[0][1]=4
            else:
                tilesnum[0][1]=2
        else:
            add_tile_2()
    elif ran_int == 3: 
        if tilesnum[0][2] == 0 :
            tilesnum[0][2] = random.randint(1,16)
            if tilesnum[0][2]>14:
                tilesnum[0][2]=4
            else:
                tilesnum[0][2]=2
        else:
            add_tile_2()
    elif ran_int == 4: 
        if tilesnum[0][3] == 0 :
            tilesnum[0][3] = random.randint(1,16)
            if tilesnum[0][3]>14:
                tilesnum[0][3]=4
            else:
                tilesnum[0][3]=2
        else:
            add_tile_2()
    elif ran_int == 5: 
        if tilesnum[1][0] == 0 :
            tilesnum[1][0] = random.randint(1,16)
            if tilesnum[1][0]>14:
                tilesnum[1][0]=4
            else:
                tilesnum[1][0]=2
        else:
            add_tile_2()
    elif ran_int == 6: 
        if tilesnum[1][1] == 0 :
            tilesnum[1][1] = random.randint(1,16)
            if tilesnum[1][1]>14:
                tilesnum[1][1]=4
            else:
                tilesnum[1][1]=2
        else:
            add_tile_2()            
    elif ran_int == 7: 
        if tilesnum[1][2] == 0 :
            tilesnum[1][2] = random.randint(1,16)
            if tilesnum[1][2]>14:
                tilesnum[1][2]=4
            else:
                tilesnum[1][2]=2
        else:
            add_tile_2()
    elif ran_int == 8: 
        if tilesnum[1][3] == 0 :
            tilesnum[1][3] = random.randint(1,16)
            if tilesnum[1][3]>14:
                tilesnum[1][3]=4
            else:
                tilesnum[1][3]=2
        else:
            add_tile_2()
    elif ran_int == 9: 
        if tilesnum[2][0] == 0 :
            tilesnum[2][0] = random.randint(1,16)
            if tilesnum[2][0]>14:
                tilesnum[2][0]=4
            else:
                tilesnum[2][0]=2
        else:
            add_tile_2()
    elif ran_int == 10: 
        if tilesnum[2][1] == 0 :
            tilesnum[2][1] = random.randint(1,16)
            if tilesnum[2][1]>14:
                tilesnum[2][1]=4
            else:
                tilesnum[2][1]=2
        else:
            add_tile_2()
    elif ran_int == 11: 
        if tilesnum[2][2] == 0 :
            tilesnum[2][2] = random.randint(1,16)
            if tilesnum[2][2]>14:
                tilesnum[2][2]=4
            else:
                tilesnum[2][2]=2
        else:
            add_tile_2()
    elif ran_int == 12: 
        if tilesnum[2][3] == 0 :
            tilesnum[2][3] = random.randint(1,16)
            if tilesnum[2][3]>14:
                tilesnum[2][3]=4
            else:
                tilesnum[2][3]=2
        else:
            add_tile_2()
    elif ran_int == 13: 
        if tilesnum[3][0] == 0 :
            tilesnum[3][0] = random.randint(1,16)
            if tilesnum[3][0]>14:
                tilesnum[3][0]=4
            else:
                tilesnum[3][0]=2
        else:
            add_tile_2()
    elif ran_int == 14: 
        if tilesnum[3][1] == 0 :
            tilesnum[3][1] = random.randint(1,16)
            if tilesnum[3][1]>14:
                tilesnum[3][1]=4
            else:
                tilesnum[3][1]=2
        else:
            add_tile_2()
    elif ran_int == 15: 
        if tilesnum[3][2] == 0 :
            tilesnum[3][2] = random.randint(1,16)
            if tilesnum[3][2]>14:
                tilesnum[3][2]=4
            else:
                tilesnum[3][2]=2
        else:
            add_tile_2()
    elif ran_int == 16: 
        if tilesnum[3][3] == 0 :
            tilesnum[3][3] = random.randint(1,16)
            if tilesnum[3][3]>14:
                tilesnum[3][3]=4
            else:
                tilesnum[3][3]=2
        else:
            return
            
def move_up(index):
    
    #//////////////////////////////move up while keypress, ///////////////////////
    
    if tilesnum[0][index] == tilesnum[1][index] and tilesnum[0][index] !=0  and tilesnum[1][index] !=0:
        tilesnum[0][index]=tilesnum[0][index]*2
        tilesnum[1][index]=0
    if tilesnum[0][index] == tilesnum[2][index] and tilesnum[0][index] !=0  and tilesnum[2][index] !=0 and tilesnum[1][index] ==0:
        tilesnum[0][index]=tilesnum[0][index]*2
        tilesnum[2][index]=0
    if tilesnum[0][index] == tilesnum[3][index] and tilesnum[0][index] !=0  and tilesnum[3][index] !=0 and tilesnum[1][index] ==0 and tilesnum[2][index] ==0:
        tilesnum[0][index]=tilesnum[0][index]*2
        tilesnum[3][index]=0
    if tilesnum[1][index] == tilesnum[2][index] and tilesnum[1][index] !=0  and tilesnum[2][index] !=0:
        tilesnum[1][index]=tilesnum[1][index]*2
        tilesnum[2][index]=0
    if tilesnum[1][index] == tilesnum[3][index] and tilesnum[1][index] !=0  and tilesnum[3][index] !=0 and tilesnum[2][index] ==0:
        tilesnum[1][index]=tilesnum[1][index]*2
        tilesnum[3][index]=0
    if tilesnum[2][index] == tilesnum[3][index] and tilesnum[2][index] !=0  and tilesnum[3][index] !=0:
        tilesnum[2][index]=tilesnum[2][index]*2
        tilesnum[3][index]=0
    for x in range(4):
        if tilesnum[0][index]==0:
            tilesnum[0][index] = tilesnum[1][index]
            tilesnum[1][index] = 0
        if tilesnum[1][index]==0:
            tilesnum[1][index] = tilesnum[2][index]
            tilesnum[2][index] = 0
        if tilesnum[2][index]==0:
            tilesnum[2][index] = tilesnum[3][index]
            tilesnum[3][index] = 0
            
            
def move_down(index):
    
    #////////////////////////////move down///////////////////////////////////////
    
    if  tilesnum[2][index] == tilesnum[3][index] and tilesnum[2][index] !=0  and tilesnum[3][index] !=0:
        tilesnum[2][index]=tilesnum[2][index]*2
        tilesnum[3][index]=0
    if tilesnum[1][index] == tilesnum[3][index] and tilesnum[1][index] !=0  and tilesnum[3][index] !=0 and tilesnum[2][index] ==0:
        tilesnum[1][index]=tilesnum[1][index]*2
        tilesnum[3][index]=0
    if tilesnum[1][index] == tilesnum[2][index] and tilesnum[1][index] !=0  and tilesnum[2][index] !=0:
        tilesnum[1][index]=tilesnum[1][index]*2
        tilesnum[2][index]=0
    if tilesnum[0][index] == tilesnum[3][index] and tilesnum[0][index] !=0  and tilesnum[3][index] !=0 and tilesnum[1][index] ==0 and tilesnum[2][index] ==0:
        tilesnum[0][index]=tilesnum[0][index]*2
        tilesnum[3][index]=0
    if tilesnum[0][index] == tilesnum[2][index] and tilesnum[0][index] !=0  and tilesnum[2][index] !=0 and tilesnum[1][index] ==0:
        tilesnum[0][index]=tilesnum[0][index]*2
        tilesnum[2][index]=0
    if tilesnum[0][index] == tilesnum[1][index] and tilesnum[0][index] !=0  and tilesnum[1][index] !=0:
        tilesnum[0][index]=tilesnum[0][index]*2
        tilesnum[1][index]=0
    for x in range(4):
        if tilesnum[3][index]==0:
            tilesnum[3][index] = tilesnum[2][index]
            tilesnum[2][index] = 0
        if tilesnum[2][index]==0:
            tilesnum[2][index] = tilesnum[1][index]
            tilesnum[1][index] = 0
        if tilesnum[1][index]==0:
            tilesnum[1][index] = tilesnum[0][index]
            tilesnum[0][index] = 0

def draw_tile():
    
    #//////////////////////////////draw squares with diff colors, insert into draw method/////////////////////
    
    strokeWeight(0)

    if tilesnum[0][0] != 0:
        if tilesnum[0][0] == 2:
            fill(238,228,218)
        if tilesnum[0][0]==4:
            fill(211,130,211)
        if tilesnum[0][0]==8:
            fill(63,112,232)
        if tilesnum[0][0]==16:
            fill(242,209,20)
        if tilesnum[0][0]==32:
            fill(255,127,39)
        if tilesnum[0][0]==64:
            fill(145,65,196)
        if tilesnum[0][0]==128:
            fill(240,5,60)
        if tilesnum[0][0]==256:
            fill(187,24,196)
        if tilesnum[0][0]==512:
            fill(70,240,48)
        if tilesnum[0][0]==1024:
            fill(229,250,13)
        if tilesnum[0][0]==2048:
            fill(242,145,54)
        if tilesnum[0][0]==4096:
            fill(159,242,241)
        rect(105,55,145,145)
    if tilesnum[0][1] != 0:
        if tilesnum[0][1] == 2:
            fill(238,228,218)
        if tilesnum[0][1]==4:
            fill(211,130,211)
        if tilesnum[0][1]==8:
            fill(63,112,232)
        if tilesnum[0][1]==16:
            fill(242,209,20)
        if tilesnum[0][1]==32:
            fill(255,127,39)
        if tilesnum[0][1]==64:
            fill(145,65,196)
        if tilesnum[0][1]==128:
            fill(240,5,60)
        if tilesnum[0][1]==256:
            fill(187,24,196)
        if tilesnum[0][1]==512:
            fill(70,240,48)
        if tilesnum[0][1]==1024:
            fill(229,250,13)
        if tilesnum[0][1]==2048:
            fill(242,145,54)
        if tilesnum[0][1]==4096:
            fill(159,242,241)
        rect(260,55,145,145)
    if tilesnum[0][2] != 0:
        if tilesnum[0][2] == 2:
            fill(238,228,218)
        if tilesnum[0][2]==4:
            fill(211,130,211)
        if tilesnum[0][2]==8:
            fill(63,112,232)
        if tilesnum[0][2]==16:
            fill(242,209,20)
        if tilesnum[0][2]==32:
            fill(255,127,39)
        if tilesnum[0][2]==64:
            fill(145,65,196)
        if tilesnum[0][2]==128:
            fill(240,5,60)
        if tilesnum[0][2]==256:
            fill(187,24,196)
        if tilesnum[0][2]==512:
            fill(70,240,48)
        if tilesnum[0][2]==1024:
            fill(229,250,13)
        if tilesnum[0][2]==2048:
            fill(242,145,54)
        if tilesnum[0][2]==4096:
            fill(159,242,241)
        rect(415,55,145,145)
    if tilesnum[0][3] != 0:
        if tilesnum[0][3] == 2:
            fill(238,228,218)
        if tilesnum[0][3]==4:
            fill(211,130,211)
        if tilesnum[0][3]==8:
            fill(63,112,232)
        if tilesnum[0][3]==16:
            fill(242,209,20)
        if tilesnum[0][3]==32:
            fill(255,127,39)
        if tilesnum[0][3]==64:
            fill(145,65,196)
        if tilesnum[0][3]==128:
            fill(240,5,60)
        if tilesnum[0][3]==256:
            fill(187,24,196)
        if tilesnum[0][3]==512:
            fill(70,240,48)
        if tilesnum[0][3]==1024:
            fill(229,250,13)
        if tilesnum[0][3]==2048:
            fill(242,145,54)
        if tilesnum[0][3]==4096:
            fill(159,242,241)
        rect(570,55,145,145)
    if tilesnum[1][0] != 0:
        if tilesnum[1][0] == 2:
            fill(238,228,218)
        if tilesnum[1][0]==4:
            fill(211,130,211)
        if tilesnum[1][0]==8:
            fill(63,112,232)
        if tilesnum[1][0]==16:
            fill(242,209,20)
        if tilesnum[1][0]==32:
            fill(255,127,39)
        if tilesnum[1][0]==64:
            fill(145,65,196)
        if tilesnum[1][0]==128:
            fill(240,5,60)
        if tilesnum[1][0]==256:
            fill(187,24,196)
        if tilesnum[1][0]==512:
            fill(70,240,48)
        if tilesnum[1][0]==1024:
            fill(229,250,13)
        if tilesnum[1][0]==2048:
            fill(242,145,54)
        if tilesnum[1][0]==4096:
            fill(159,242,241)
        rect(105,210,145,145)
    if tilesnum[1][1] != 0:
        if tilesnum[1][1] == 2:
            fill(238,228,218)
        if tilesnum[1][1]==4:
            fill(211,130,211)
        if tilesnum[1][1]==8:
            fill(63,112,232)
        if tilesnum[1][1]==16:
            fill(242,209,20)
        if tilesnum[1][1]==32:
            fill(255,127,39)
        if tilesnum[1][1]==64:
            fill(145,65,196)
        if tilesnum[1][1]==128:
            fill(240,5,60)
        if tilesnum[1][1]==256:
            fill(187,24,196)
        if tilesnum[1][1]==512:
            fill(70,240,48)
        if tilesnum[1][1]==1024:
            fill(229,250,13)
        if tilesnum[1][1]==2048:
            fill(242,145,54)
        if tilesnum[1][1]==4096:
            fill(159,242,241)
        rect(260,210,145,145)
    if tilesnum[1][2] != 0:
        if tilesnum[1][2] == 2:
            fill(238,228,218)
        if tilesnum[1][2]==4:
            fill(211,130,211)
        if tilesnum[1][2]==8:
            fill(63,112,232)
        if tilesnum[1][2]==16:
            fill(242,209,20)
        if tilesnum[1][2]==32:
            fill(255,127,39)
        if tilesnum[1][2]==64:
            fill(145,65,196)
        if tilesnum[1][2]==128:
            fill(240,5,60)
        if tilesnum[1][2]==256:
            fill(187,24,196)
        if tilesnum[1][2]==512:
            fill(70,240,48)
        if tilesnum[1][2]==1024:
            fill(229,250,13)
        if tilesnum[1][2]==2048:
            fill(242,145,54)
        if tilesnum[1][2]==4096:
            fill(159,242,241)
        rect(415,210,145,145) 
    if tilesnum[1][3] != 0:
        if tilesnum[1][3] == 2:
            fill(238,228,218)
        if tilesnum[1][3]==4:
            fill(211,130,211)
        if tilesnum[1][3]==8:
            fill(63,112,232)
        if tilesnum[1][3]==16:
            fill(242,209,20)
        if tilesnum[1][3]==32:
            fill(255,127,39)
        if tilesnum[1][3]==64:
            fill(145,65,196)
        if tilesnum[1][3]==128:
            fill(240,5,60)
        if tilesnum[1][3]==256:
            fill(187,24,196)
        if tilesnum[1][3]==512:
            fill(70,240,48)
        if tilesnum[1][3]==1024:
            fill(229,250,13)
        if tilesnum[1][3]==2048:
            fill(242,145,54)
        if tilesnum[1][3]==4096:
            fill(159,242,241)
        rect(570,210,145,145) 
    if tilesnum[2][0] != 0:
        if tilesnum[2][0] == 2:
            fill(238,228,218)
        if tilesnum[2][0]==4:
            fill(211,130,211)
        if tilesnum[2][0]==8:
            fill(63,112,232)
        if tilesnum[2][0]==16:
            fill(242,209,20)
        if tilesnum[2][0]==32:
            fill(255,127,39)
        if tilesnum[2][0]==64:
            fill(145,65,196)
        if tilesnum[2][0]==128:
            fill(240,5,60)
        if tilesnum[2][0]==256:
            fill(187,24,196)
        if tilesnum[2][0]==512:
            fill(70,240,48)
        if tilesnum[2][0]==1024:
            fill(229,250,13)
        if tilesnum[2][0]==2048:
            fill(242,145,54)
        if tilesnum[2][0]==4096:
            fill(159,242,241)
        rect(105,365,145,145)
    if tilesnum[2][1] != 0:
        if tilesnum[2][1] == 2:
            fill(238,228,218)
        if tilesnum[2][1]==4:
            fill(211,130,211)
        if tilesnum[2][1]==8:
            fill(63,112,232)
        if tilesnum[2][1]==16:
            fill(242,209,20)
        if tilesnum[2][1]==32:
            fill(255,127,39)
        if tilesnum[2][1]==64:
            fill(145,65,196)
        if tilesnum[2][1]==128:
            fill(240,5,60)
        if tilesnum[2][1]==256:
            fill(187,24,196)
        if tilesnum[2][1]==512:
            fill(70,240,48)
        if tilesnum[2][1]==1024:
            fill(229,250,13)
        if tilesnum[2][1]==2048:
            fill(242,145,54)
        if tilesnum[2][1]==4096:
            fill(159,242,241)
        rect(260,365,145,145)
    if tilesnum[2][2] != 0:
        if tilesnum[2][2] == 2:
            fill(238,228,218)
        if tilesnum[2][2]==4:
            fill(211,130,211)
        if tilesnum[2][2]==8:
            fill(63,112,232)
        if tilesnum[2][2]==16:
            fill(242,209,20)
        if tilesnum[2][2]==32:
            fill(255,127,39)
        if tilesnum[2][2]==64:
            fill(145,65,196)
        if tilesnum[2][2]==128:
            fill(240,5,60)
        if tilesnum[2][2]==256:
            fill(187,24,196)
        if tilesnum[2][2]==512:
            fill(70,240,48)
        if tilesnum[2][2]==1024:
            fill(229,250,13)
        if tilesnum[2][2]==2048:
            fill(242,145,54)
        if tilesnum[2][2]==4096:
            fill(159,242,241)
        rect(415,365,145,145)
    if tilesnum[2][3] != 0:
        if tilesnum[2][3] == 2:
            fill(238,228,218)
        if tilesnum[2][3]==4:
            fill(211,130,211)
        if tilesnum[2][3]==8:
            fill(63,112,232)
        if tilesnum[2][3]==16:
            fill(242,209,20)
        if tilesnum[2][3]==32:
            fill(255,127,39)
        if tilesnum[2][3]==64:
            fill(145,65,196)
        if tilesnum[2][3]==128:
            fill(240,5,60)
        if tilesnum[2][3]==256:
            fill(187,24,196)
        if tilesnum[2][3]==512:
            fill(70,240,48)
        if tilesnum[2][3]==1024:
            fill(229,250,13)
        if tilesnum[2][3]==2048:
            fill(242,145,54)
        if tilesnum[2][3]==4096:
            fill(159,242,241)
        rect(570,365,145,145)
    if tilesnum[3][0] != 0:
        if tilesnum[3][0] == 2:
            fill(238,228,218)
        if tilesnum[3][0]==4:
            fill(211,130,211)
        if tilesnum[3][0]==8:
            fill(63,112,232)
        if tilesnum[3][0]==16:
            fill(242,209,20)
        if tilesnum[3][0]==32:
            fill(255,127,39)
        if tilesnum[3][0]==64:
            fill(145,65,196)
        if tilesnum[3][0]==128:
            fill(240,5,60)
        if tilesnum[3][0]==256:
            fill(187,24,196)
        if tilesnum[3][0]==512:
            fill(70,240,48)
        if tilesnum[3][0]==1024:
            fill(229,250,13)
        if tilesnum[3][0]==2048:
            fill(242,145,54)
        if tilesnum[3][0]==4096:
            fill(159,242,241)
        rect(105,520,145,145)
    if tilesnum[3][1] != 0:
        if tilesnum[3][1] == 2:
            fill(238,228,218)
        if tilesnum[3][1]==4:
            fill(211,130,211)
        if tilesnum[3][1]==8:
            fill(63,112,232)
        if tilesnum[3][1]==16:
            fill(242,209,20)
        if tilesnum[3][1]==32:
            fill(255,127,39)
        if tilesnum[3][1]==64:
            fill(145,65,196)
        if tilesnum[3][1]==128:
            fill(240,5,60)
        if tilesnum[3][1]==256:
            fill(187,24,196)
        if tilesnum[3][1]==512:
            fill(70,240,48)
        if tilesnum[3][1]==1024:
            fill(229,250,13)
        if tilesnum[3][1]==2048:
            fill(242,145,54)
        if tilesnum[3][1]==4096:
            fill(159,242,241)
        rect(260,520,145,145)
    if tilesnum[3][2] != 0:
        if tilesnum[3][2] == 2:
            fill(238,228,218)
        if tilesnum[3][2]==4:
            fill(211,130,211)
        if tilesnum[3][2]==8:
            fill(63,112,232)
        if tilesnum[3][2]==16:
            fill(242,209,20)
        if tilesnum[3][2]==32:
            fill(255,127,39)
        if tilesnum[3][2]==64:
            fill(145,65,196)
        if tilesnum[3][2]==128:
            fill(240,5,60)
        if tilesnum[3][2]==256:
            fill(187,24,196)
        if tilesnum[3][2]==512:
            fill(70,240,48)
        if tilesnum[3][2]==1024:
            fill(229,250,13)
        if tilesnum[3][2]==2048:
            fill(242,145,54)
        if tilesnum[3][2]==4096:
            fill(159,242,241)
        rect(415,520,145,145)
    if tilesnum[3][3] != 0:
        if tilesnum[3][3] == 2:
            fill(238,228,218)
        if tilesnum[3][3]==4:
            fill(211,130,211)
        if tilesnum[3][3]==8:
            fill(63,112,232)
        if tilesnum[3][3]==16:
            fill(242,209,20)
        if tilesnum[3][3]==32:
            fill(255,127,39)
        if tilesnum[3][3]==64:
            fill(145,65,196)
        if tilesnum[3][3]==128:
            fill(240,5,60)
        if tilesnum[3][3]==256:
            fill(187,24,196)
        if tilesnum[3][3]==512:
            fill(70,240,48)
        if tilesnum[3][3]==1024:
            fill(229,250,13)
        if tilesnum[3][3]==2048:
            fill(242,145,54)
        if tilesnum[3][3]==4096:
            fill(159,242,241)
        rect(570,520,145,145)        
                
      
                
#  ///////////////////global variables///////////////// 
counter = 0 
n = 50
m = 180
p = ""
f=""
colour = 0
colour2 = 0
ran_int = 0
moves = 0
sum_number = 0
login1="2048"
login2="   Press  ENTER"
username_isopen = False
game_isopen = False
leaderboard_isopen = False
openning_isopen = True
gameboard = Gameboard()
usernameboard = Username_board()
leaderboard = Leaderboard()
leaderboard.players = [["Yifan",1062714243,524]]
username= []
tiles = [] 
tilesnum = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
                
                
        
def setup():
    size(1280,720)
    
def draw():
    global gameover,player,moves,score,counter,colour2,colour
    background(255)
    
    counter +=1
    colour2 +=5
    colour+=5
    if colour == 255:
        colour = 0
    if openning_isopen:
        fill(0)
        textSize(250)
        text(login1,280,370)  #Asteroids!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if colour2%510<=255:
            fill(colour,colour,colour)
            textSize(45)
            text(login2,400,500)   #Press Enter!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
        if colour2%510>=255:
            fill(255-colour,255-colour,255-colour)
            textSize(45)
            text(login2,400,500) 
    
    if username_isopen:
        player=Player_info()
        usernameboard.draw()

    if game_isopen:
        gameboard.draw()
        draw_tile()
        
        sum_number = sum(tilesnum[0])+sum(tilesnum[1])+sum(tilesnum[2])+sum(tilesnum[3])  
        #///////////////////////////////////////build TRY AGAIN button////////////////////////////////////////
        fill(255)
        strokeWeight(5)   
        rect(830,400,320,100)
        fill(0)
        textSize(60)
        text("Try Again",850,470)
        
        
        fill(255)
        strokeWeight(5)   
        rect(830,550,320,100)
        fill(0)
        textSize(60)
        text("Exit Game",850,620)
        writting()
        
        #/////////////////////////moves counter//////////////////////////////////////
        fill(0)
        textSize(60)
        text("Moves  "+ str(moves), 840,200)
        text("Score  "+ str(sum_number), 840,300)
        
        
    if leaderboard_isopen:
        f = "Leader Board"
        a = ""
        scoreboard = ""
        levelnum = ""
        bombnumber = ""
        leaderboard.draw()    
        
        
    
def keyPressed():
    global tilesnum, tile,counter, openning_isopen,game_isopen,leaderboard_isopen,username_isopen,\
    m,n,p,username,moves
    
    if openning_isopen and counter > 0:
        if key == ENTER:
            openning_isopen = False
            username_isopen = True
            counter = 0
    
    if game_isopen:
        if keyCode == RIGHT:
            moves += 1
            for row in tilesnum:
                if row[2] == row[3] and row[2] !=0 and row[3] !=0:
                    row[2]*=2
                    row[3]=0
                if row[1] == row[3] and row[1] !=0 and row[3] !=0 and row[2] ==0:
                    row[1]*=2
                    row[3]=0 
                if row[1] == row[2] and row[1] !=0 and row[2] !=0 :
                    row[1]*=2
                    row[2]=0
                    
                if  row[0] == row[3] and row[0] !=0 and row[3] !=0 and row[1] ==0 and row[2] ==0:
                    row[0]*=2
                    row[3]=0
                if row[0] == row[2] and row[0] !=0 and row[2] !=0 and row[1] ==0:
                    row[0]*=2
                    row[2]=0
                if row[0] == row[1] and row[0] !=0 and row[1] !=0:
                    row[0]=row[0]*2
                    row[1]=0
            for x in range(4):
                for row in tilesnum:    
                    if row[3]==0:
                        row[3]=row[2]
                        row[2]=0
    
                    if row[2]==0:
                        row[2]=row[1]
                        row[1]=0
    
                    if row[1]==0:
                        row[1]=row[0]
                        row[0]=0
    
            add_tile_2()
            print tilesnum
        if keyCode == LEFT:
            moves +=1
            for row in tilesnum:
                if row[0] == row[1] and row[0] !=0 and row[1] !=0:
                    row[0]=row[0]*2
                    row[1]=0
                    
                if row[0] == row[2] and row[0] !=0 and row[2] !=0 and row[1] ==0:
                    row[0]*=2
                    row[2]=0
    
                    
                if row[0] == row[3] and row[0] !=0 and row[3] !=0 and row[1] ==0 and row[2] ==0:
                    row[0]*=2
                    row[3]=0
                
                    
                if  row[1] == row[2] and row[1] !=0 and row[2] !=0:
                    row[1]*=2
                    row[2]=0
                    
                if row[1] == row[3] and row[1] !=0 and row[3] !=0 and row[2] ==0:
                    row[1]*=2
                    row[3]=0 
                    
                if row[2] == row[3] and row[2] !=0 and row[3] !=0:
                    row[2]*=2
                    row[3]=0
            for x in range(4):
                for row in tilesnum:    
                    if row[0]==0:
                        row[0]=row[1]
                        row[1]=0
                    if row[1]==0:
                        row[1]=row[2]
                        row[2]=0
                    if row[2]==0:
                        row[2]=row[3]
                        row[3]=0
            add_tile_2()
            print tilesnum
        if keyCode == UP:
            moves+=1
            move_up(0)
            move_up(1)
            move_up(2)
            move_up(3)
            add_tile_2()
            print tilesnum
        if keyCode == DOWN:
            moves+=1
            move_down(0)
            move_down(1)
            move_down(2)
            move_down(3)
            add_tile_2()
            print tilesnum
    if username_isopen and counter > 0:    
        if keyCode==RIGHT:
            if n<1112:
                n=n+118
        if keyCode==LEFT:
            if n>50:
                n=n-118
        if keyCode==UP:
            if m>180:
                m=m-118
        if keyCode==DOWN:
            if m<534:
                m=m+118
        if key == " ":
            if len(username)>0:
                username.pop(len(username)-1)
                p=str("".join(username))
        if key == ENTER and counter>0:
            if len(p)<=10:
                if n==50 and m==180:
                    username.append("1")
                    p=str("".join(username))
                if n==168 and m==180:
                    username.append("2")
                    p=str("".join(username))
                if n==286 and m==180:
                    username.append("3")
                    p=str("".join(username))
                if n==404 and m==180:
                    username.append("4")
                    p=str("".join(username))
                if n==522 and m==180:
                    username.append("5")
                    p=str("".join(username))
                if n==640 and m==180:
                    username.append("6")
                    p=str("".join(username))
                if n==758 and m==180:
                    username.append("7")
                    p=str("".join(username))
                if n==876 and m==180:
                    username.append("8")
                    p=str("".join(username))
                if n==994 and m==180:
                    username.append("9")
                    p=str("".join(username))
                if n==1112 and m==180:
                    username.append("0")
                    p=str("".join(username))
                if n==50 and m==298:
                    username.append("Q")
                    p=str("".join(username))
                if n==168 and m==298:
                    username.append("W")
                    p=str("".join(username))
                if n==286 and m==298:
                    username.append("E")
                    p=str("".join(username))
                if n==404 and m==298:
                    username.append("R")
                    p=str("".join(username))
                if n==522 and m==298:
                    username.append("T")
                    p=str("".join(username))
                if n==640 and m==298:
                    username.append("Y")
                    p=str("".join(username))
                if n==758 and m==298:
                    username.append("U")
                    p=str("".join(username))
                if n==876 and m==298:
                    username.append("I")
                    p=str("".join(username))
                if n==994 and m==298:
                    username.append("O")
                    p=str("".join(username))
                if n==1112 and m==298:
                    username.append("P")
                    p=str("".join(username))
                if n==50 and m==416:
                    username.append("A")
                    p=str("".join(username))
                if n==168 and m==416:
                    username.append("S")
                    p=str("".join(username))
                if n==286 and m==416:
                    username.append("D")
                    p=str("".join(username))
                if n==404 and m==416:
                    username.append("F")
                    p=str("".join(username))
                if n==522 and m==416:
                    username.append("G")
                    p=str("".join(username))
                if n==640 and m==416:
                    username.append("H")
                    p=str("".join(username))
                if n==758 and m==416:
                    username.append("J")
                    p=str("".join(username))
                if n==876 and m==416:
                    username.append("K")
                    p=str("".join(username))
                if n==994 and m==416:
                    username.append("L")
                    p=str("".join(username))
                if n==1112 and m==416:
                    username.append("/")
                    p=str("".join(username))
                if n==50 and m==534:
                    username.append("Z")
                    p=str("".join(username))
                if n==168 and m==534:
                    username.append("X")
                    p=str("".join(username))
                if n==286 and m==534:
                    username.append("C")
                    p=str("".join(username))
                if n==404 and m==534:
                    username.append("V")
                    p=str("".join(username))
                if n==522 and m==534:
                    username.append("B")
                    p=str("".join(username))
                if n==640 and m==534:
                    username.append("N")
                    p=str("".join(username))
                if n==758 and m==534:
                    username.append("M")
                    p=str("".join(username))
                if n==876 and m==534:
                    username.append("_")
                    p=str("".join(username))
            if n>=994 and m==534 and len(p)>0:
                player.playername()
                username_isopen = False
                game_isopen = True
                counter = 0
    if leaderboard_isopen:
        if key == ENTER:
            leaderboard_isopen = False
            openning_isopen = True
            counter = 0
            tilesnum = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
            moves = 0
            p = ""
            username = []
def mousePressed():
    global game_isopen
    #/////////////////////////////////TRY AGAIN while mouse pressed/////////////////////////////////
    if game_isopen:
        if 830 < mouseX < 1150 and 400 < mouseY <500:
            tilesnum = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
            moves = 0
           
        if 830 < mouseX < 1150 and 550 <mouseY <650:
            player.playerscore()
            player.playerlevel()
            leaderboard.players.append(player.plist)
            game_isopen = False
            leaderboard_isopen = True
        
        
        