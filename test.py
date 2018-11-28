''' Gfie '''
def main():
    ''' giff '''
    num = int(input())
    numx = 0
    numy = 0
    if num < 1:
        print("Exit")
    else:
        for _ in range(num):
            num1 = int(input())
            if num1 >= numx and numx >= numy:
                numy = numx
                numx = num1
                if numx == numy:
                    numx = numy
            elif numx >= num1 and num1 >= numy:
                numy = num1
                if numx == numy:
                    numx = numy
        if numy == 0:
            if numx == 0:
                print("Exit")
            else:
                print(numy)
        else:
            print(numy)
main()
