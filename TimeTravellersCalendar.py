
from datetime import datetime, timedelta

lastJumps = [0]

# Function returns the number of days jumped from # of
# time travelling trips taken
def daysTravelled(n):
    global lastJumps
    # n is the nuber of time travel trips taken
    for i in range(n + 1):
        if i == 0:
            lastJumps.append(1)
        else:
            newJump = lastJumps[-1] + lastJumps[-2]
            lastJumps.append(newJump)
    print(lastJumps)
    add_days(lastJumps[-1])
    
def add_days(n):
    print("Number of days passed:", n)
    start_date = datetime(2028, 1, 1)
    new_date = start_date + timedelta(days=n)
    formatted_date = new_date.strftime("%B %d, %Y")
    print(formatted_date)

if __name__ == "__main__":
    daysTravelled(10)
    