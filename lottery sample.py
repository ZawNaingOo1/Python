"""
Lottery checker
Solution by Dr. Thiri The Wut Yee
There are many other possible solutions
"""
    
true=0              #variable use to check whether input has valid format or not
ticket=[]           #variable to store a lottery ticket number
tickets= dict()     #{key:value = ticket=prize}, per user, there are mulitple tickets 
users=[]            #object array to store multiple users 

class user:
    def __init__(self,ID,tickets,total):
        self.ID=ID
        self.tickets=tickets
            
def userID(seed):
    """
    User ID generation. ID has yearmonthdayidnumber format.
    """
    import datetime
    currentDate = datetime.datetime.today().strftime("%Y%m%d")
    return str(currentDate)+str(seed+1)
    

def checknumbers(ticket):
    """
    Lottery ticket must begin with one alphabet follow by 5 digits. 
    """
    for i in ticket[1:]:
        if i.isdigit():
            res=1
        else:
            res=0
    return res

def generate():
    """
    Winning number generation. We only interest 5 digits.
    The initial alphabet is neglect to consider winning case.
    """
    import random
    win=[]
    for i in range(0,5):
        win.append(str(random.randint(0,9)))
    print("Winning Number ",win)
    return win

def cal_prize(win,ticket):
    """
    5 number match = 5000,000
    4 number match = 8%
    3 number match = 0.6%
    2 number match = 0.04%
    1 number = 0.002%
    """
    result=0
    for w in win:
        result=result+ ticket.count(w)
    if result==5:
        prize= 5000000
    elif result==4:
        prize = 5000000 * (8/100)
    elif result==3:
        prize = 5000000 * (0.6/100)
    elif result==2:
        prize = 5000000 * (0.04/100)
    elif result==1:
        prize = 5000000 * (0.002/100)
    else:
        prize=0
    return prize

#main
#Step 1: User input
#Step 1.1: User ID generation
seed=100
ID=userID(seed)
seed=seed+1
loop=int(input("How many tickets you want to buy"))
#Step 1.2: Mulitple user input
for i in range(loop):
    ticket=input("Input lottery number seperated by space e.g. Z12345 ").split()
    #Step 2: Check validity for input format
    while not ticket[0].isalpha() or checknumbers(ticket)==0:
        print("Wrong input! Try again. \n")
        ticket=input("Input lottery number seperated by space e.g. A12345 ").split()
    #Step 3: Generate winning number
    #STep 4: Calculate winning prize
    prize=cal_prize(generate(),ticket)
    tk=""
    tk=tk.join(ticket)
    tickets[tk]=prize
u = user(ID,tickets,0)
users.append(u)

# Step 5: Print output 
for i in users:
    total=0
    for j in i.tickets.keys():
            if i.tickets[j]>0:
                print("Winning ticket",j,"\n")
                total=total+i.tickets[j]
                print("Ticket Prize",i.tickets[j],"\n")
    
    print("User ID",i.ID,"has win Total=",total)
