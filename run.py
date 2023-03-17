import pandas as pd
import numpy as np
import statsmodels.api as sm

# Read the Excel file into a pandas dataframe
df = pd.read_excel('projectdata_FW2022.xlsx')
df.dropna(inplace=True)

# set the independent and dependent variables
X = df[['CPIGROCANALL', 'CPICANEXC', 'CPICANSER', 'CPICANGDS', 'CPICANENG', 'UNEMPC', 'CEIR', 'MSC', 'TSX', 'BLIC', 'RGDP', 'IRGDP', 'SRGDP', 'CBR', 'CIR']]
# assuming CPICANALL represents inflation
y = df['CPICANALL']

# add a constant term to the independent variables
X = sm.add_constant(X)

# fit the OLS regression model
model = sm.OLS(y, X).fit()

# print the beta values
print(model.params)


# # Calculate the average value of CPIGROCANALL for the years 1961-1970
# cpi_avg = df.loc[(df['year'].dt.year >= 1961) & (df['year'].dt.year <= 1970), 'CPIGROCANALL'].mean()

# # Print the average value of CPIGROCANALL
# print(f"The average value of CPIGROCANALL for the years 1961-1970 is: {cpi_avg}")
