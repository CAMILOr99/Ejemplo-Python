def run():
    # squares = []

    # for i in range(1, 101):
    #     if i % 3 !=0:
    #         squares.append(i**2)

    multipli= [i for i in range(1, 1001) if i % 6 ==0 and i % 9 ==0 and i % 4==0]
    
    print(multipli)


if __name__ == "__main__":
    run()