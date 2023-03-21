## F test

```
# set the independent and dependent variables
X = df[[ 'UNEMPC', 'CEIR', 'MSC', 'TSX', 'BLIC', 'RGDP', 'IRGDP', 'SRGDP', 'CBR', 'CIR']]
# assuming CPICANALL represents inflation
y = df['CPICANALL']

# add a constant term to the independent variables
X = sm.add_constant(X)

# fit the OLS regression model
model = sm.OLS(y, X).fit()

mse = model.mse_resid
rmse = mse ** 0.5
print("MSE:", mse)
print("RMSE:", rmse)

# Define the null hypothesis as all independent variables having a coefficient of 0
null_hypothesis = 'MSC = RGDP = TSX = IRGDP = SRGDP = 0' 

# Perform the F-test
f_test = model.f_test(null_hypothesis)

# Print the F-statistic and p-value
print('F-statistic:', round(float(f_test.fvalue), 2))
print('p-value:', round(float(f_test.pvalue), 2))
```

F-statistic: 107.41
p-value: 0.0


The code defines a multiple linear regression model with 10 independent variables (UNEMPC, CEIR, MSC, TSX, BLIC, RGDP, IRGDP, SRGDP, CBR, and CIR) and 1 dependent variable (CPICANALL). It then uses OLS regression to fit the model to the data.

After fitting the model, it calculates the mean squared error (MSE) and root mean squared error (RMSE) of the residuals.

The code then performs an F-test to test the hypothesis that MSC, RGDP, TSX, IRGDP, and SRGDP have a coefficient of 0, i.e. they are not statistically significant in the model. The F-statistic is calculated as 107.41 and the p-value is less than 0.05, indicating that we reject the null hypothesis and conclude that at least one of the variables MSC, RGDP, TSX, IRGDP, and SRGDP has a non-zero coefficient in the model.


## After eliminating (MSC, RGDP, TSX, IRGDP, SRGDP)

```
CBR        -6.700985
UNEMPC     -1.652641
BLIC        0.003392
CEIR        0.144015
CIR         0.633087
const     135.837568
```

Biggest factor that affects inflation is CBR, the Bank of Canada's policy interest rate. As the interest rate increases inflation decreases by a factor of 6.7 per percent increase in of the Bank of Canada Rate.

### Covariance Matrix
```
Covariance Matrix:
            const    UNEMPC      CEIR      BLIC       CBR       CIR
const   18.723393 -0.404412 -0.165442  0.001528  0.102002  0.028573
UNEMPC  -0.404412  0.084505 -0.000951  0.001128 -0.077058  0.050061
CEIR    -0.165442 -0.000951  0.001794 -0.000165  0.002339 -0.002703
BLIC     0.001528  0.001128 -0.000165  0.001185 -0.003310  0.003739
CBR      0.102002 -0.077058  0.002339 -0.003310  0.164940 -0.128937
CIR      0.028573  0.050061 -0.002703  0.003739 -0.128937  0.111459
```

The variance of UNEMPC is 0.084505, and the covariances between UNEMPC and the other variables are all negative, indicating that UNEMPC tends to move in the opposite direction of the other variables.

The variances of CEIR, BLIC, CBR, and CIR are all relatively small, ranging from 0.001185 to 0.001794.


There are some relatively large covariances between certain variables, such as the negative covariance between UNEMPC and CBR, and the positive covariance between BLIC and CIR. 

These covariances suggest that there may be some linear dependence between these variables.