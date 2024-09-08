import matplotlib.pyplot as plt

input_values=[1,2,3,4,5]
sqs=[1,4,9,16,25]
plt.style.use('seaborn-v0_8')
fig,ax= plt.subplots()
ax.plot(input_values,sqs, linewidth=3)

ax.set_title("Sqaure Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Sqaure Of Value",fontsize=14)

ax.tick_params(labelsize=14)
plt.show()