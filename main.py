n = int(input())
def watermelon(n):
    if n == 2:
        print('NO')
    elif n % 2 == 0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    watermelon(n)

