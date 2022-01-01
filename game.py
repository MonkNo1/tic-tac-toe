def show_board(b):
    print("------------------------------")
    print("|        |         |        |")
    print("|",b[7],"| ",b[8]," | ",b[9],"|")
    print("|        |         |        |")
    print("-----------------------------")
    print("|        |         |        |")
    print("|",b[4]," | ",b[5]," | ",b[6],"|")
    print("|        |         |       |")
    print("-----------------------------")
    print("|        |         |        |")
    print("|",b[1]," | ",b[2]," | ",b[3],"|")
    print("|        |         |        |")
    print("------------------------------")



def Input():
    pos=int(input("plz enter the position"))
    return pos


def start():
    sel=input("player 1 eneter the val as x or o")
    p1=sel
    if p1=="X" or p1=="x":
        p2="O"
    else:
        p2="X"
    b=[""]*10
    print("the board positons are:")
    print("------------------------------")
    print("|        |         |        |")
    print("|   7    |     8   |   9    |")
    print("|        |         |        |")
    print("-----------------------------")
    print("|        |         |        |")
    print("|    4   |    5    |   6    |")
    print("|        |         |        |")
    print("-----------------------------")
    print("|        |         |        |")
    print("|    1   |    2    |   3    |")
    print("|        |         |        |")
    print("------------------------------")
    print("press y to continue")
    y=input("enter y:")
    if y=="y" or y=="Y":
        game(b)
    else:
        exit()
    
    
def check(b,i):
    if not "" in b:
        if b[7]==b[8] and b[8]==b[9]:
            win(b[8])
        elif b[7]==b[4] and b[4]==b[1]:
            win(b[4])
        elif b[7]==b[5] and b[5]==b[3]:
            win(b[5])
        elif b[4]==b[5] and b[5]==b[6]:
            win(b[5])
        elif b[1]==b[2] and b[2]==b[3]:
            win(b[2])
        elif b[1]==b[5] and b[5]==b[9]:
            win(b[5])
        elif b[8]==b[5] and b[5]==b[2]:
            win(b[5])
        elif b[9]==b[6] and b[6]==b[3]:
            win(b[6])
        elif b[9]==b[5] and b[5]==b[1]:
            win(b[5])
        if i==8:
            win("xo")
           
def finnaly():
    print("1-->replay")
    print("2-->exit")
    inp=int(inpu("enter the val  : "))
    if inp==1:
        start()
    else:
        exit()
def win(ak):
    if ak=="X" or ak=="x":
        print("player 1 wins the game")
    elif ak=="O" or ak=="o":
        print("player 2 wins the game")
    elif  ak=="xo" or ak=="XO":
        print("match draw")
    print("press y to continue")
    y=input("enter y : ")
    if y=="y" or y=="Y":
        finnaly()
    else:
        exit()
def game(b):
    i=0
    while i<=8:
        #clrscr()  
        if i%2==0:
            print("player 1")
            inp=int(input("ener ur position  :"))
        else:
            print("player 2")
            inp=int(input("enter ur position  :"))
        if inp==1:
            if i%2==0:
                b[1]="X"
            else:
                b[1]="O"
        elif inp==2:
            if i%2==0:
                b[2]="X"
            else:
                b[2]="O"
        elif inp==3:
            if i%2==0:
                b[3]="X"
            else:
                b[3]="O"
        elif inp==4:
            if i%2==0:
                b[4]="X"
            else:
                b[4]="O" 
        elif inp==5:
            if i%2==0:
                b[5]="X"
            else:
                b[5]="O" 
        elif inp==6:
            if i%2==0:
                b[6]="X"
            else:
                b[6]="O" 
        elif inp==7:
            if i%2==0:
                b[7]="X"
            else:
                b[7]="O" 
        elif inp==8:
            if i%2==0:
                b[8]="X"
            else:
                b[8]="O" 
        elif inp==9:
            if i%2==0:
                b[9]="X"
            else:
                b[9]="O"
        check(b,i)
        show_board(b)
        i=i+1




start()
