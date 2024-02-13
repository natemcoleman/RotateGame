import TwoMain
import math
from matplotlib import pyplot as plt

positions = TwoMain.ReturnPositions()

currMajorCircleCenter = 1
index1 = 0
index2 = 1

circleCenter = TwoMain.ReturnCircleCoordsAndRadii()[0][currMajorCircleCenter]
angle1, angle2 = TwoMain.ReturnAngleOneAndAngleTwo(0, 1, 1)

fig, ax = plt.subplots()
plt.plot([positions[index1][0], circleCenter[0]], [positions[index1][1], circleCenter[1]], 'k')
plt.plot([positions[index2][0], circleCenter[0]], [positions[index2][1], circleCenter[1]], 'k')
plt.plot(positions[index1][0], positions[index1][1], 'r*')
plt.plot(positions[index2][0], positions[index2][1], 'r*')
plt.plot(circleCenter[0], circleCenter[1], 'bo')


plt.show()

print("point 1:", positions[index1])
print("point 2:", positions[index2])
print("circleCenter:", circleCenter)
print("Angle1:", math.degrees(angle1), " Angle2:", math.degrees(angle2))



