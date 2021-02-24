def car_speed(speed, time_to_speed):
    acceleration = speed/time_to_speed
    return acceleration

def direction(turn):
    if turn >= 0 and turn <= 1:
        return 'turning right'
    elif turn <= 0 and turn >= -1:
        return 'turning left'
    elif turn == 0:
        return 'going straight'
    else:
        return 'drifting a lot'

def time_travel(vel, dist):
    time = vel/dist
    return time

def accelerating(vel, time):
    a = vel/time
    return a


def car():
    print("You are currently stationary")
    current_speed = 0
    t = True
    while t:
        choice = input("Choose what do you want the car to do (A,B,D,R): ").lower()

        if choice == "a":
            speed = int(input("At what speed do you want to travel? "))
            time_to_speed = int(input("How fast do you want to get to this speed "))
            s = car_speed(speed, time_to_speed)
            print(f"The car needs to accelerate at a ratio of {s} km/h to reach that speed")

        elif choice == "d":
            turn = int(input("How much are you turning? left < 0 > right "))
            print(f"The car is {direction(t)}")

        elif choice == "b":
            brake = current_speed/time

        elif choice == "r":
            initial_speed = int(input("At what speed do you want to travel? "))
            time_travel = int(input("How long do you want to travel for at this speed? "))

        else:
            choice = input("Invalid input, choose what do you want the car to do (A,B,R)").lower()







    vel = int(input("Enter the car velocity in km/h: "))
    turn = int(input("Is the car turning? (Y/N):"))
    dir = direction(turn)
    print(dir)
    print(f"The car is {car_speed(vel)} at {vel} km/h")
    print(f"The car is accelerating at {accelerating(vel, time)}")

car()










