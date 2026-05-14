import matplotlib.pyplot as pit
import numpy as np
import pandas as pd


def qua(n):
    s = 0
    for i in range(len(massx)):
        s = s + pow(massx[i], n)
    return s


def quay1(n):
    s = 0
    for i in range(len(massx)):
        s = s + pow(massx[i], n) * massy1[i]
    return s


def quay2(n):
    s = 0
    for i in range(len(massx)):
        s = s + pow(massx[i], n) * massy2[i]
    return s


file = open('seqv.txt', 'r')
massx = []
massy1 = np.array([])
massy2 = np.array([])
for i in range(25):
    str = file.readline()
    str = str.strip()
    mass = str.split(' ')
    y1 = float(mass[0])
    y2 = float(mass[3])
    massy1 = np.append(massy1, y1)
    massy2 = np.append(massy2, y2)
    massx.append(float(i + 1))

step = int(input("Степень полинома = "))

mass = np.zeros((step + 1, step + 1))
mass[0][0] = 25
mass[step][step] = qua(step * 2)

flag = 2
for i in range(1, step + 1):
    s1 = qua(i)
    s2 = qua(step * 2 - i)
    for j in range(flag):
        mass[i - j][j] = s1
        mass[step - j][step - i + j] = s2
    flag = flag + 1

pd.set_option('display.max_columns', 5)
df = pd.DataFrame(mass)
print(df)

massobr = np.linalg.inv(mass)

df = pd.DataFrame(massobr)

massyy1 = np.zeros(step + 1)
massyy1[0] = np.sum(massy1)
for i in range(1, step + 1):
    massyy1[i] = quay1(i)
result1 = massobr @ massyy1
print(f"Коэффициенты 1: {result1}")

massyy2 = np.zeros(step + 1)
massyy2[0] = np.sum(massy2)
for i in range(1, step + 1):
    massyy2[i] = quay2(i)
result2 = massobr @ massyy2
print(f"Коэффициенты 2: {result2}")

masy1 = np.zeros([25])
masy2 = np.zeros([25])
for i in range(25):
    masy1[i] = result1[0]
    masy2[i] = result2[0]
    for j in range(1, step + 1):
        masy1[i] = masy1[i] + result1[j] * pow(massx[i], j)
        masy2[i] = masy2[i] + result2[j] * pow(massx[i], j)
    masy1[i] = masy1[i] / pow(10, 6)
    masy2[i] = masy2[i] / pow(10, 6)
print(masy1)
print(masy2)

summ1 = 0
summ2 = 0
for i in range(25):
    summ1 = abs(masy1[i] - massy1[i]) + summ1
    summ2 = abs(masy2[i] - massy2[i]) + summ2
summ1 = summ1 / 25
summ2 = summ2 / 25
print("Погрешность 1 = ", summ1 / pow(10, 6))
print("Погрешность 2 = ", summ2 / pow(10, 6))

pit.plot(massx, masy1, 'o-y', label="first", lw=4, mec='y', mew='0.5', ms='8')
pit.plot(massx, masy2, 'o-b', label="second", lw=4, mec='b', mew='0.5', ms='8')
pit.xlabel("P, МПа")
pit.ylabel("q, МПа")
pit.title("График")
pit.legend()
pit.grid(True)
pit.show()

file.close()
