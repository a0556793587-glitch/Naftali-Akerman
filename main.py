from working import *
def x_o():
    for item in range(9):
        show_table()
        if irem % 2 == 0:
            line_o()
        if item % 2 == 1:
            line_x()
        if cheek_winwer() == False:
            break
        if item == 8:
            print("It's a draw!") 


if __name__ == "__main__":
    x_o()


        

