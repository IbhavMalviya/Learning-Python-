from random import randint
import plotly.express as px

class Die:
    
    def __init__(self,num_side=6):
        self.num_side=num_side
        
    def roll(self):
        return randint(1, self.num_side)
    

die1=Die()
die2=Die(10)

results=[]

for roll_num in range(50000):
    result=die1.roll()+die2.roll()
    results.append(result)
    
frequencies=[]
max_result=die1.num_side+die2.num_side
poss_results=range(1,max_result+1)

for value in poss_results:
    frequency=results.count(value)
    frequencies.append(frequency)
    
print(frequencies)


title="Result Of Rolling Two Dice 50000 Times"
label={'x':'Results','y':'Frequency of Result'}
fig=px.bar(x=poss_results,y=frequencies,title=title,labels=label)
fig.update_layout(xaxis_dtick=1)
fig.write_html('Dice.html')
fig.show()
