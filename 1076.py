data = {}
data['black']={'value':0,'times':1}
data['brown']={'value':1,'times':10}
data['red']={'value':2,'times':100}
data['orange']={'value':3,'times':1000}
data['yellow']={'value':4,'times':10000}
data['green']={'value':5,'times':100000}
data['blue']={'value':6,'times':1000000}
data['violet']={'value':7,'times':10000000}
data['grey']={'value':8,'times':100000000}
data['white']={'value':9,'times':1000000000}

value = data[input()]['value']*10
value += data[input()]['value']
value *= data[input()]['times']

print(value)
