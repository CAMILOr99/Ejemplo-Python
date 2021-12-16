def divisiors(num):
    try:
        if num < 0:
            raise ValueError("Positive numbers")
        divisiors = [i for i in range (1,num+1) if num%i == 0]
        return divisiors
    
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        num = int(input("Give a number please: "))
        print(divisiors(num))
        print("End program")
    except ValueError:
        print("please only numbers")

if __name__ == "__main__":
    run()