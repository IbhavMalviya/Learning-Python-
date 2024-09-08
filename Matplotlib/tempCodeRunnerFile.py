import matplotlib.pyplot as plt
xv=(1,1001)
yv=[x**2 for x in xv]

plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()


ax.scatter(xv,yv,s=10000)
ax.set_title("Sqaure Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Sqaure Of Value",fontsize=14)

ax.tick_params(labelsize=14)

ax.axis([0,1100,0,1100000])

plt.show()