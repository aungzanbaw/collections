"""
    Tower of Hanoi
    The Tower of Hanoi is a mathematical game or puzzle consisting of three rods and a number of disks of various diameters, which can slide onto any rod. The puzzle begins with the disks stacked on one rod in order of decreasing size, the smallest at the top, thus approximating a conical shape.

    The solution can be found using two mutually recursive procedures: To move n disks counterclockwise to the neighbouring target peg: move n − 1 disks counterclockwise to the target peg. move disk #n one step clockwise.
"""
def TOH(n, a, b, c):
    # n = number of disk
    # a,b,c = pegs
    if(n > 0):
        TOH(n-1, a,c,b)
        print(f"Moving a disc from {a} to {c}")
        TOH(n-1, b,a,c)
TOH(3,1,2,3)