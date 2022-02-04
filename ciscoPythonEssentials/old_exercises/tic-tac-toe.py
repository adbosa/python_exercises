board = """
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   5   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+"""

width  = 24
height = int(width / 2)

def printRule(width):
    for x in range(width + 1):
        if x == 0 or (x % 8 == 0):
            print("+", end="")
        else:
            print("-", end="")
    print()
    return

def printEmptyLine(width, line):
    position = 1
    for x in range(width + 1):
        if x == 0 or (x % 8 == 0):
            print("|", end="")
        elif x % 4 == 0 and x % 8 != 0 and line == 2:
            print(position, end="")
            position += 1
        else:
            print(" ", end="")
    print()
    return

def makeBoard(width, height):
    line_position = 0
    for line in range(height + 1):
        if line == 0 or (line % 4 == 0):
            printRule(width)
        else:
            line_position += 1
            printEmptyLine(width, line_position)
            if line_position >= 3: line_position = 0
    return

makeBoard(width, height)
print(board)
