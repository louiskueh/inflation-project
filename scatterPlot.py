import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Read the Excel file into a pandas dataframe
df = pd.read_excel('projectdata_FW2022.xlsx')
df.dropna(inplace=True)

# list of dependent variables
dependent_vars = ['UNEMPC', 'CEIR', 'MSC', 'TSX', 'BLIC', 'RGDP', 'IRGDP', 'SRGDP', 'CBR', 'CIR']

# create a figure with multiple subplots
fig, axs = plt.subplots(nrows=5, ncols=2, figsize=(10, 12))
# np.log(X['MSC'])
# X = X[[ 'log_MSC' ]]
# loop through dependent variables and plot scatter plot on corresponding subplot
for i, var in enumerate(dependent_vars):
    row = i // 2
    col = i % 2
    axs[row, col].scatter(df['CPICANALL'], np.log(df[var]))
    axs[row, col].set_xlabel('CPICANALL')
    axs[row, col].set_ylabel(var)
    axs[row, col].set_title(f'Scatter plot between CPIALL and {var}')
    
# adjust spacing between subplots and show plot
plt.tight_layout()
plt.show()
# UNEMPC is not related 