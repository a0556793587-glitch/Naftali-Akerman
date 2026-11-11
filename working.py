
from data import s,wine

def show_table():
    print(f"""
[1]{s[1]} | [2]{s[2]} | [3]{s[3]}
------+-------+----
[4]{s[4]} | [5]{s[5]} | [6]{s[6]}
------+-------+----
[7]{s[7]} | [8]{s[8]} | [9]{s[9]}

""")



def cheek():
    x = []
    o = []
    for k,v in s.items():
        if v == "x":
            x.append(k)
        elif v == "o":
            o.append(k)
    return x,o

def cheek_winwer():
    for item in wine:
        if "x" == s[item[0]] and "x" == s[item[1]] and "x" == s[item[2]]:
            print("x won,  you are winner")
            return False
        elif "o" == s[item[0]] and "o" == s[item[1]] and "o" == s[item[2]]:
            print("0 won, you are winner")
            return False
    return True
        
def line_o():
    print("new yout turn o")
    user = cheek_num()
    s[user] = "o"

def line_x():
    print("new your turn x")
    user = cheek_num()
    s[user] = "x"


def cheek_num():
    choose_number = None
    while True:
        try:
            choose_number = int(input("enter your chooce??"))
            if choose_number > 0 and choose_number < 10 and s[choose_number] == "":
                return choose_number
            else: 
                print("try again")
        except ValueError:
            print("You must choose only from the possible options, so you will choose between 1 and 9.")

        
