if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    def triangle():
        if a + b > c and a + c > b and b + c > a:
            print('Это треугольник')
        else:
            print('Это не треугольник')
    triangle()

