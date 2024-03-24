import time


def countdown(t):

    while t > 0:
        minutes, seconds = divmod(t, 60)
        timer = "time remaining: {:02d} : {:02d} ".format(minutes, seconds)
        print(timer)

        time.sleep(1)
        t -= 1

    print("Time's up!")


def main():
    try:
        t = int(input("Please enter countdown time(Please enter second): "))
        countdown(t)
    except ValueError:
        print("Invalid input. Please enter a valid number of seconds")


if __name__ == "__main__":
    main()
