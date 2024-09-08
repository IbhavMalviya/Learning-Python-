import matplotlib.pyplot as plt

xv=range(1,5000)
yv=[x**3 for x in xv]

plt.style.use("seaborn-v0_8")
fig,ax=plt.subplots()

ax.scatter(xv,yv,c=xv,cmap=plt.cm.Blues,s=1)
ax.ticklabel_format(style='plain')
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cubes of Value", fontsize=14)
plt.show()