from math import *

def negative_to_positive_angle(angle):
    k = floor(abs(angle) / 360)
    return (angle + ((k + 1) * 360))

def normalize_angle(angle):
    new_angle = 0
    if (angle < 0):
        new_angle = negative_to_positive_angle(angle)
    
    if (angle > 360):
        k = floor(angle/360)
        new_angle = angle - (k * 360)
    
    if (new_angle >= 180):
        new_angle -= 180
    elif (angle >= 180):
        new_angle = angle - 180
    else:
        new_angle = angle
    
    return new_angle


testcases = int(input())
answers = []
for i in range(testcases):
    new_angles = []
    angles = list(map(int, input().split()))
    n_angles = angles.pop(0)
    for angle in angles:
        new_angle = normalize_angle(angle)
        if (new_angle not in new_angles):
            new_angles.append(new_angle)
    if (len(new_angles) > 0):
        answer = len(new_angles) * 2
    else:
        answer = 1
    answers.append(answer)

for x in answers:
    print(x)