def divisiors(num):
    divisiors = [i for i in range (1,num+1) if num%i == 0]
    return divisiors

def run():
    num = input("Give a number please: ")
    assert num.isnumeric(), "Only positive numbers"
    print(divisiors(int(num)))
    print("End program")


if __name__ == "__main__":
    run()