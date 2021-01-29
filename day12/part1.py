with open('input') as f:
    dirlist = f.read().splitlines()

angle = 0
x = 0
y = 0
for line in dirlist:
    order = line[0]
    magnitude = int(line[1:])
    if order == "N": y += magnitude
    elif order == "S": y -= magnitude
    elif order == "E": x += magnitude
    elif order == "W": x -= magnitude
    elif order == "L": angle = (angle + magnitude) % 360
    elif order == "R": angle = (angle - magnitude) % 360
    elif order == "F":
        x += ((angle == 0) - (angle == 180)) * magnitude
        y += ((angle == 90) - (angle == 270)) * magnitude
    else:
        print(line)
        quit()

print(x, y, abs(x) + abs(y))
