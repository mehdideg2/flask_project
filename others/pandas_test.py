import pandas as pd

df = pd.read_csv('AirPassengersX.csv')

print(df['time'][135])


names = ['Damien','Florian','Mehdi']
total = [55, 50, 44]
data_set = list(zip(names, total))
data_frame =pd.DataFrame(data = data_set, columns=['Names', 'Total'])
data_frame.to_csv('point.csv', index=False, header= False)