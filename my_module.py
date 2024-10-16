
def ifib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a)
    return a

if __name__ == "__main__":
    import sys
    print(sys.argv)
    ifib(int(sys.argv[1]))

