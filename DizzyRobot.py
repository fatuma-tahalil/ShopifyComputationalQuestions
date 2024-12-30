directionFacing = "north"
directionsFacedString = []

def findDirection():
    global directionFacing
    global directionsFacedString
    print("The robot is facing north")
    print("")
    while True:
        rotate = input("Rotate (right/left/exit): ")
        if rotate == "exit":
            return directionFacing
            break
        degree = int(input("Degree (0/90/180/270): "))
        
        if directionFacing == "north":
            if rotate == "right":
                if degree == 0:
                    directionFacing = "east"
                elif degree == 90:
                    directionFacing = "east"
                elif degree == 180:
                    directionFacing = "south"
                elif degree == 270:
                    directionFacing = "west"
            elif rotate == "left":
                if degree == 0:
                    directionFacing = "west"
                elif degree == 90:
                    directionFacing = "west"
                elif degree == 180:
                    directionFacing = "south"
                elif degree == 270:
                    directionFacing = "east"
        elif directionFacing == "east":
            if rotate == "right":
                if degree == 0:
                    directionFacing = "south"
                elif degree == 90:
                    directionFacing = "south"
                elif degree == 180:
                    directionFacing = "west"
                elif degree == 270:
                    directionFacing = "north"
            elif rotate == "left":
                if degree == 0:
                    directionFacing = "north"
                elif degree == 90:
                    directionFacing = "north"
                elif degree == 180:
                    directionFacing = "west"
                elif degree == 270:
                    directionFacing = "south"
        elif directionFacing == "south": 
            if rotate == "right":
                if degree == 0:
                    directionFacing = "west"
                elif degree == 90:
                    directionFacing = "west"
                elif degree == 180:
                    directionFacing = "north"
                elif degree == 270:
                    directionFacing = "east"
            elif rotate == "left":
                if degree == 0:
                    directionFacing = "east"
                elif degree == 90:
                    directionFacing = "east"
                elif degree == 180:
                    directionFacing = "north"
                elif degree == 270:
                    directionFacing = "west"
        elif directionFacing == "west":
            if rotate == "right":
                if degree == 0:
                    directionFacing = "north"
                elif degree == 90:
                    directionFacing = "north"
                elif degree == 180:
                    directionFacing = "east"
                elif degree == 270:
                    directionFacing = "south"
            elif rotate == "left":
                if degree == 0:
                    directionFacing = "south"
                elif degree == 90:
                    directionFacing = "south"
                elif degree == 180:
                    directionFacing = "east"
                elif degree == 270:
                    directionFacing = "north"
        print("The robot is facing", directionFacing)
        directionsFacedString.append(directionFacing)
                    
if __name__ == "__main__":
    print(findDirection())
    print("The robot has faced the following directions: ",directionsFacedString)