import pandas as pd
import numpy as np
import statsmodels.api as sm

# Read the Excel file into a pandas dataframe
df = pd.read_excel('projectdata_FW2022.xlsx')
df.dropna(inplace=True)

# set the independent and dependent variables
X = df[['UNEMPC', 'CEIR', 'MSC', 'TSX', 'BLIC', 'RGDP', 'IRGDP', 'SRGDP', 'CBR', 'CIR']]
# assuming CPICANALL represents inflation
y = df['CPICANALL']

# add a constant term to the independent variables
X = sm.add_constant(X)

# fit the OLS regression model
model = sm.OLS(y, X).fit()

# print the beta values
print(model.params)

sorted_params = model.params.abs().sort_values()

# print the sorted beta values
print(sorted_params)

# Results
# CBR      -1.353645e+00
# BLIC     -4.828265e-02
# TSX      -6.188484e-04
# RGDP     -5.717480e-04
# MSC       1.594357e-11
# IRGDP     6.736992e-04
# SRGDP     7.411693e-04
# CIR       2.964797e-02
# CEIR      1.394406e-01
# UNEMPC    5.731830e-01
# const     2.614972e+01

# sorted abs
# MSC       1.594357e-11
# RGDP      5.717480e-04
# TSX       6.188484e-04
# IRGDP     6.736992e-04
# SRGDP     7.411693e-04
# CIR       2.964797e-02
# BLIC      4.828265e-02
# CEIR      1.394406e-01
# UNEMPC    5.731830e-01
# CBR       1.353645e+00
# const     2.614972e+01
# dtype: float64

# CPICANALL represents the all-items Consumer Price Index for Canada
# CPIGROCANALL represents the growth rate of the all-items Consumer Price Index for Canada
# CPICANEXC represents the Consumer Price Index for Canada excluding energy
# CPICANSER represents the Consumer Price Index for Canada excluding energy and seasonally sensitive products
# CPICANGDS represents the Consumer Price Index for Canada excluding energy and food
# CPICANENG represents the Consumer Price Index for Canada for energy products

# Variables:
# UNEMPC represents the unemployment rate in Canada
# CEIR represents the Consumer Expectations Index for Canada
# MSC represents the Money Supply in Canada
# TSX represents the Toronto Stock Exchange Composite Index
# BLIC represents the Bank of Canada's Business Outlook Survey Indicator
# RGDP represents the Real Gross Domestic Product in Canada
# IRGDP represents the growth rate of the Real Gross Domestic Product in Canada
# SRGDP represents the seasonally adjusted Real Gross Domestic Product in Canada
# CBR represents the Bank of Canada's policy interest rate
# CIR represents the inflation expectations implied by the difference between nominal and real Government of Canada bond yields