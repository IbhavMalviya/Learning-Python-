import matplotlib.pyplot as plt

xv = range(1, 1001)
yv = [x**2 for x in xv]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(xv,yv,color='red',s=1)
ax.ticklabel_format(style='plain')
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(labelsize=14)

plt.show()
