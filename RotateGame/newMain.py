from matplotlib import pyplot as plt

majorCirclesCentersOuter = [(-50, 28.867513), (-50, 28.867513), (0, -57.735027), (0, -57.735027), (50, 28.867513), (50, 28.867513)]
majorCirclesRadiiOuter = [110, 90, 110, 90, 110, 90]

positions = [(0, 126.847103), (-20, 113.720327), (20, 113.720327), (0, 103.700661), (-38.484692, 45.313158), (-59.852814, 34.556038), (-39.807407, 22.982817), (-58.484692, 10.672142), (38.484692, 45.313158), (59.852814, 34.556038), (39.807407, 22.982817), (58.484692, 10.672142), (-108.484692, -39.539656), (-89.807407, -51.850331), (-109.852814, -63.423552), (-88.484692, -74.180672), (0, -45.965634), (-20, -55.9853), (20, -55.9853), (0, -69.112076), (108.484692, -39.539656), (89.807407, -51.850331), (109.852814, -63.423552), (88.484692, -74.180672)]
face1 = [0, 1, 2, 3]
face2 = [4, 5, 6, 7]
face3 = [8, 9, 10, 11]
face4 = [12, 13, 14, 15]
face5 = [16, 17, 18, 19]
face6 = [20, 21, 22, 23]

rotateCircle1CounterClockwise = [(0, 15), (2, 14), (15, 18), (14, 19), (18, 9), (19, 11), (9, 0), (11, 2), (21, 20), (20, 22), (22, 23), (23, 21)]
rotateCircle2CounterClockwise = [(1, 13), (3, 12), (13, 16), (12, 17), (16, 8), (17, 10), (8, 1), (10, 3), (4, 5), (5, 7), (7, 6), (6, 4)]
rotateCircle3CounterClockwise = [(0, 5), (1, 7), (5, 17), (7, 19), (17, 23), (19, 22), (23, 0), (22, 1), (13, 15), (15, 14), (14, 12), (12, 13)]
rotateCircle4CounterClockwise = [(2, 4), (3, 6), (4, 16), (6, 18), (16, 21), (18, 20), (21, 2), (20, 3), (9, 8), (8, 10), (10, 11), (11, 9)]
rotateCircle5CounterClockwise = [(4, 12), (5, 14), (12, 22), (14, 20), (22, 9), (20, 8), (9, 4), (8, 5), (2, 3), (3, 1), (1, 0), (0, 2)]
rotateCircle6CounterClockwise = []

axisLimits = 200
fig, ax = plt.subplots()
ax.axis('equal')
ax.set_xlim(-axisLimits, axisLimits)
ax.set_ylim(-axisLimits, axisLimits)
ax.set_xticks([])
ax.set_yticks([])

for i, (x, y) in enumerate(positions, 0):
    colorChar = 'r'
    if i <= 3:
        colorChar = 'r'
    elif i <= 7:
        colorChar = 'b'
    elif i <= 11:
        colorChar = 'g'
    elif i <= 15:
        colorChar = 'm'
    elif i <= 19:
        colorChar = 'y'
    else:
        colorChar = 'c'
    ax.scatter(x, y, color=colorChar)
    ax.text(x, y, str(i), verticalalignment='bottom', horizontalalignment='right')
    plt.pause(0.25)
plt.show()


