import matplotlib.pyplot as plt

with open('time_linha.txt') as f:
    time_linha = [float(time_linha.rstrip()) for time_linha in f]

with open('time_star.txt') as f:
    time_star = [float(time_star.rstrip()) for time_star in f]

with open('obj_linha.txt') as f:
    obj_linha = [int(obj_linha.rstrip()) for obj_linha in f]

with open('obj_star.txt') as f:
    obj_star = [int(obj_star.rstrip()) for obj_star in f]

plt.plot(time_linha,obj_linha)
plt.plot(time_star,obj_star)
plt.xlabel('tempo')
plt.ylabel('objetivo')
plt.show()