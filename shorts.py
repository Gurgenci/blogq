import pandas as pd

# The following function reads a text file that is organised as line pairs.
# The function creates a new text file where the ordering of the pairs is reversed:

def reverse_pairs(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    n=len(lines)
    with open(output_file, 'w') as f:
        for i in range(n-1, 0, -2):
            f.write(lines[i-1])
            f.write(lines[i])
reverse_pairs('data/blog/pagelist.txt','reversed.txt')

# The following function reads a csv file into a data frame and displays the column names:

def read_csv(file):
    import pandas as pd
    df = pd.read_csv(file)
    # print(df.columns)
    return df
df=read_csv('/Users/Halim/Downloads/BP3.csv')
print(df.columns)
print(df.head(5))
# plot df['Systolic'] against df['Date']
# X axis should show only the first and last date

import matplotlib.pyplot as plt
import numpy as np
import datetime

# Calculate the four-point rolling average
df['Systolic_avg'] = df['Systolic'].rolling(window=4).mean()

df['Date'] = pd.to_datetime(df['Date'])
df['Date_ordinal'] = df['Date'].map(datetime.datetime.toordinal)

# Perform linear regression
coeffs = np.polyfit(df['Date_ordinal'], df['Systolic'], 1)
df['Systolic_fit'] = np.polyval(coeffs, df['Date_ordinal'])

# Plot the original 'Systolic' data
plt.plot(df['Date'], df['Systolic'], 'o', label='Systolic')

# Plot the four-point average
# plt.plot(df['Date'], df['Systolic_avg'], label='4-point Average')

# Plot the linear fit
plt.plot(df['Date'], df['Systolic_fit'], label='Linear Fit')

plt.xlabel('Date')
plt.ylabel('Systolic')
plt.title('Systolic Blood Pressure')

# Set x-axis ticks to show only the first and last date
plt.xticks([df['Date'].iloc[0], df['Date'].iloc[-1]])

# Enable grid lines
plt.grid(True)

# Add a legend
plt.legend()

plt.show()
