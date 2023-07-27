import pandas as pd
import matplotlib.pyplot as plt

#Read the data from the CSV file
data = pd.read_csv('us_disaster_declarations.csv')
#2 Analyzing the frequency and severity of disasters over the years to see if there are any significant trends or changes.

data['declaration_date'] = pd.to_datetime(data['declaration_date'])
data['Year'] = data['declaration_date'].dt.year

disaster_frequency = data.groupby('Year')['declaration_title'].count()
disaster_severity = data.groupby('Year')['declaration_title'].size() 


plt.figure(figsize=(12, 6))
plt.plot(disaster_frequency.index, disaster_frequency.values, marker='o', label='Frequency', color='blue')
plt.plot(disaster_severity.index, disaster_severity.values, marker='o', label='Severity', color='red')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Frequency and Severity of Natural Disasters Over the Years')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
