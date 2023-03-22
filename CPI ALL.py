import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Read the Excel file into a pandas dataframe
df = pd.read_excel('projectdata_FW2022.xlsx')
df.dropna(inplace=True)

# set the independent and dependent variables
X = df[[ 'UNEMPC', 'CEIR', 'MSC', 'TSX', 'BLIC', 'RGDP', 'IRGDP', 'SRGDP', 'CBR', 'CIR']]
# assuming CPICANALL represents inflation
y = df['CPICANALL']

# add a constant term to the independent variables
X = sm.add_constant(X)

# fit the OLS regression model
model = sm.OLS(y, X).fit()

cov_matrix = model.cov_params()
print("Covariance Matrix:")
print(cov_matrix)

mse = model.mse_resid
rmse = mse ** 0.5
print("MSE:", mse)
print("RMSE:", rmse)

# # Print F-statistic and p-value
# f_statistic, p_value = sm.stats.anova_lm(model, typ=2)["F"]["x1"]
# print("F-statistic:", f_statistic)
# print("p-value:", p_value)

# # Print Jarque-Bera test statistic and p-value (tests for normality of residuals)
# jb_statistic, jb_p_value, _, _ = sm.stats.stattools.jarque_bera(model.resid)
# print("Jarque-Bera statistic:", jb_statistic)
# print("p-value:", jb_p_value)

# sorted_params_abs = model.params.abs().sort_values()
sorted_params = model.params.sort_values()
# print the sorted beta values
print(sorted_params)
print(model.summary())


# Predicted values of the dependent variable
y_pred = model.predict(X)

# Mean of the dependent variable
y_mean = np.mean(y)

# Total Sum of Squares (TSS)
TSS = np.sum((y - y_mean) ** 2)

# Residual Sum of Squares (RSS) or Sum of Squared Residuals (SSR)
SSR = np.sum((y - y_pred) ** 2)

# Explained Sum of Squares (ESS)
ESS = TSS - SSR

# Degrees of Freedom
n = len(y)
k = len(X.columns)
df_resid = n - k
df_total = n - 1

# Standard Error of Regression (SER)
SER = np.sqrt(SSR / df_resid)

# Print the results
print("Sum of Squared Residuals (SSR): ", SSR)
print("Total Sum of Squares (TSS): ", TSS)
print("Explained Sum of Squares (ESS): ", ESS)
print("Standard Error of Regression (SER): ", SER)



# plot residuals against predicted values
fig, ax = plt.subplots()
ax.scatter(model.predict(X), model.resid)
ax.axhline(y=0, color='red', linestyle='--')
ax.set_xlabel('Predicted Values')
ax.set_ylabel('Residuals')
plt.show()





# Results
# const     2.614972e+01
# UNEMPC    5.731830e-01
# CEIR      1.394406e-01
# MSC       1.594357e-11
# TSX      -6.188484e-04
# BLIC     -4.828265e-02
# RGDP     -5.717480e-04
# IRGDP     6.736992e-04
# SRGDP     7.411693e-04
# CBR      -1.353645e+00
# CIR       2.964797e-02

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