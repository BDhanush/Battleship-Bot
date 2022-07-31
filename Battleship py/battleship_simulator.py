class BattleShip:
    def __init__(self):
        self.team_name = "Not_Unsinkable"
        self.ships = ships
        self.opponent_board = opponent_board
        self.info = -1
        self.cx=-1
        self.cy=-1

    def set_ships(self):
        return self.ships

    def attack(self):
        probability=[[0 for i in range(10)] for j in range(10)]
        for z in ship_sizes:
            
            for i in range (0,10):
                for j in range(10-z+1):
                    hits=set()
                    non_misses=0
                    for k in range(j,j+z):
                        if(store[i][k]==1):
                            hits.add(k)
                        if(store[i][k]!=2):
                            non_misses+=1
                    
                    if(non_misses==z):
                        for k in range(j,j+z):
                            if(k in hits):
                                probability[i][k]=0
                            else:
                                if(z==5 or z==4):
                                    probability[i][k]+=(2*z*(bias*len(hits) if(len(hits)) else 1))
                                else:
                                    probability[i][k]+=(z*(bias*len(hits) if(len(hits)) else 1))
            
            for j in range (0,10):
                for i in range(10-z+1):
                    hits2=set()
                    non_misses2=0
                    for k in range(i,i+z):
                        if(store[k][j]==1):
                            hits2.add(k)
                        if(store[k][j]!=2):
                            non_misses2+=1
                    
                    if(non_misses2==z):
                        for k in range(i,i+z):
                            if(k in hits2):
                                probability[k][j]=0
                            else:
                                if(z==5 or z==4):
                                    probability[k][j]+=(2*z*(bias*len(hits2) if(len(hits2)) else 1))
                                else:
                                    probability[k][j]+=(z*(bias*len(hits2) if(len(hits2)) else 1))

        x=0
        y=0
        
        if(self.info==3):                                               #hawkeye
            row_sum=[0 for i in range(10)]
            column_sum=[0 for i in range(10)]
            for i in range (0,10):
                for j in range (0,10):
                    row_sum[i]+=probability[i][j]
                    column_sum[j]+=probability[j][i]
            
            row_or_column=0
            row_column_no=0
            max_sum=0
            for i in range (0,10):
                if(row_sum[i]>max_sum):
                    row_column_no=i
                    row_or_column=0
                if(column_sum[i]>max_sum):
                    row_or_column=1
                    row_column_no=i

                max_sum=max(row_sum[i],max_sum)
                max_sum=max(column_sum[i],max_sum)
            
            max_sum=0
            row_column_no2=0
            if(row_or_column):
                y=row_column_no
                for i in range(0,10):
                    row_sum[i]-=probability[i][row_column_no]
                    if(row_sum[i]>max_sum):
                        row_column_no2=i
                        max_sum=row_sum[i]
                x=row_column_no2
            else:
                x=row_column_no
                for i in range (0,10):
                    column_sum[i]-=probability[row_column_no][i]
                    if(column_sum[i]>max_sum):
                        row_column_no2=i
                        max_sum=column_sum[i]
                y=row_column_no2

            # for i in range (0,10):
            #     for j in range (0,10):
            #         print(probability[i][j],end=" ")
            #     print()
            # print()

            # for i in range (0,10):
            #     for j in range (0,10):
            #         print(store[i][j],end=" ")
            #     print()
            # print()

            # print(x," ",y)
            self.cx=x
            self.cy=y
            # print(cx,cy)
            return (x,y)

        maxi1=0

        for i in range (0,10):
            for j in range (0,10):
                if(self.cx!=i and self.cy!=j):
                    if(probability[i][j]>maxi1):
                        x=i
                        y=j
                        # print(x,y)
                        maxi1=probability[i][j]
        #         print(probability[i][j],end=" ")
        #     print()
        # print()

        # print(x," ",y)
        return (x,y)
                        
        

    def hit_or_miss(self, x, y):
        
        # info = 1 for miss, 0 for a hit, -1 for an out of range shooting, 2 for special move nullify. 3 for your next move to be a Hawkeye Shot
        if opponent_board[x][y]==1:
            return 1
        return 0

for k in range(1,22):
    store=[[0 for i in range(10)] for j in range(10)]
    store2=[[0 for i in range(10)] for j in range(10)]
    ship_sizes=[5,4,3]

    ships=[
        [1,3,4,1],
        [2,1,5,0],
        [8,4,5,1],
        [3,2,4,0],
        [9,1,3,1]
    ]

    opponent_board =[[0 for i in range(10)] for j in range(10)]

    for i in range (0,5):
        for j in range (0,ships[i][2]):
            if(ships[i][3]==0):
                opponent_board[ships[i][0]+j][ships[i][1]]=1
            else:
                opponent_board[ships[i][0]][ships[i][1]+j]=1

    opponent_board=[
[0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
]

    bias=4
    cou=0
    n=0
    cx=-1
    cy=-1
    ship=BattleShip()
    b=0


    while(n<21):
        x,y=ship.attack()
        if(ship.info==3):
            for i in range (0,10):
                if(ship.hit_or_miss(x,i)):
                    store2[x][i]=1
                    n+=1
                else:
                    store2[x][i]=2
                if(ship.hit_or_miss(i,y)):
                    store2[i][y]=1
                    n+=1
                else:
                    store2[i][y]=2
            if(ship.hit_or_miss(x,y)):
                n-=1
            ship.info=1
            b=1
        elif(ship.hit_or_miss(x,y)):
            store[x][y]=1
            store2[x][y]=1
            n+=1
        else:
            store[x][y]=2
            store2[x][y]=2
        cou+=1            
        # print(n)
        if(b==0 and n==k):
            ship.info=3
        
    print(k,cou)
# for i in range (0,10):
#     for j in range (0,10):
#         print(store[i][j],end=" ")
#     print()