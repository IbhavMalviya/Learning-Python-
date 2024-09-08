import matplotlib.pyplot as plt
xv=[1,2,3,4,5,6,7,8,9,10]
yv=[1,4,9,16,25,36,49,64,81,100]

plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()


ax.scatter(xv,yv,s=100)
ax.set_title("Sqaure Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Sqaure Of Value",fontsize=14)

ax.tick_params(labelsize=14)

plt.show()