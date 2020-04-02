def MaxSquence(n, arg):
    MaxNum = 0
    Sum = 0
    for i in range(n):
        Sum += arg[i]
        if Sum < 0:
            Sum = 0
        if Sum > MaxNum:
            MaxNum = Sum
    return MaxNum


def main():
    while True:
        try:
            n = eval(input())
            if n <= 0:
                print("Input Error!")
            else:
                arg = [0] * n
                arg = [int(j) for j in input().split()]
                print("最大字段和为：{}".format(MaxSquence(n, arg)))
        except:
            break


main()
