with open('input') as f:
    dirlist = f.read().splitlines()

angle = 0
shippos = {"x": 0, "y": 0}
waypos = {"x": 10, "y": 1}
for line in dirlist:
    order = line[0]
    magnitude = int(line[1:])
    if order == "N": waypos["y"] += magnitude
    elif order == "S": waypos["y"] -= magnitude
    elif order == "E": waypos["x"] += magnitude
    elif order == "W": waypos["x"] -= magnitude
    elif order == "L": 
        for i in range(int(magnitude/90)):
            temp = waypos["x"]
            waypos["x"] = -1 * waypos["y"]
            waypos["y"] = temp
    elif order == "R":
        for i in range(int(magnitude/90)):
            temp = waypos["x"]
            waypos["x"] = waypos["y"]
            waypos["y"] = -1 * temp
    elif order == "F":
        shippos["x"] += waypos["x"] * magnitude
        shippos["y"] += waypos["y"] * magnitude
    else:
        print(line)
        quit()
    print(line, shippos, waypos)

print(shippos, abs(shippos["x"]) + abs(shippos["y"]))
