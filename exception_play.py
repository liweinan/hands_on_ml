while True:
    try:
        print("Press CTRL-D to exit")
        x = input("x -> ")
        y = input("y -> ")
        try:
            answer = int(x) / int(y)
        except ZeroDivisionError:
            print("ZeroDivisionError!")
    except EOFError:
        print("> Exited <")
        break

    print(answer)

