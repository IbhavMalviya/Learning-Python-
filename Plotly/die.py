from random import randint
import plotly.express as px

class Die:
    
    def __init__(self,num_side=6):
        self.num_side=num_side
        
    def roll(self):
        return randint(1, self.num_side)
    

die=Die()

results=[]

for roll_num in range(1000):
    result=die.roll()
    results.append(result)
    
frequencies=[]
poss_results=range(1,die.num_side+1)

for value in poss_results:
    frequency=results.count(value)
    frequencies.append(frequency)
    
print(frequencies)


title="Result Of Rolling A Die 1000 Times"
label={'x':'Results','y':'Frequency of Result'}
fig=px.bar(x=poss_results,y=frequencies,title=title,labels=label)
fig.show()