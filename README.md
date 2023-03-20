 # CPI ALL

```
 Results
const     2.614972e+01
UNEMPC    5.731830e-01
CEIR      1.394406e-01
MSC       1.594357e-11
TSX      -6.188484e-04
BLIC     -4.828265e-02
RGDP     -5.717480e-04
IRGDP     6.736992e-04
SRGDP     7.411693e-04
CBR      -1.353645e+00
CIR       2.964797e-02
 ```

 Looking at the results of the OLS model, we can see the estimated coefficients (beta values) for each of the independent variables. The constant term is 26.15.

From the coefficients, we can see that UNEMPC (unemployment rate) has a positive coefficient of 0.57, which suggests that there is a positive relationship between inflation (CPICANALL) and the unemployment rate. Similarly, CEIR (Consumer Expectations Index) has a positive coefficient of 0.14, indicating that there is a positive relationship between inflation and consumer expectations.

On the other hand, we can see that CBR (Bank of Canada's policy interest rate) has a negative coefficient of -1.35, implying that there is an inverse relationship between inflation and the policy interest rate. CIR (inflation expectations implied by bond yields) has a positive coefficient of 0.03, suggesting that there is a positive relationship between inflation and inflation expectations.

The coefficients for the other independent variables (MSC, RGDP, TSX, IRGDP, SRGDP) are relatively small compared to the other variables - on the order of < e^-4. Therefore, they may not have a significant impact on inflation. Using all the variables we have an R-squared of `0.987`. After removing the above variables we get an r squared value of `0.906`

Based on these results, we can conclude that the unemployment rate, consumer expectations, policy interest rate, and inflation expectations are important factors to consider when predicting inflation. However, we should keep in mind that these results are based on a specific dataset and should be interpreted accordingly.

The values sorted (absolute)
```
MSC       1.594357e-11
RGDP      5.717480e-04
TSX       6.188484e-04
IRGDP     6.736992e-04
SRGDP     7.411693e-04
CIR       2.964797e-02
BLIC      4.828265e-02
CEIR      1.394406e-01
UNEMPC    5.731830e-01
CBR       1.353645e+00
const     2.614972e+01
```

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

## Summary for all vs 'UNEMPC', 'CEIR', 'BLIC', 'CBR', 'CIR'

```
X = df[['UNEMPC', 'CEIR', 'BLIC', 'CBR', 'CIR']]
# assuming CPICANALL represents inflation
y = df['CPICANALL']
```
MSE: 63.37442110787486
RMSE: 7.960805305236076
```
                            OLS Regression Results
==============================================================================
Dep. Variable:              CPICANALL   R-squared:                       0.906
Model:                            OLS   Adj. R-squared:                  0.905
Method:                 Least Squares   F-statistic:                     953.3
Date:                Fri, 17 Mar 2023   Prob (F-statistic):          2.20e-251
Time:                        18:24:56   Log-Likelihood:                -1747.2
No. Observations:                 501   AIC:                             3506.
Df Residuals:                     495   BIC:                             3532.
Df Model:                           5
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const        135.8376      4.327     31.393      0.000     127.336     144.339
UNEMPC        -1.6526      0.291     -5.685      0.000      -2.224      -1.081
CEIR           0.1440      0.042      3.400      0.001       0.061       0.227
BLIC           0.0034      0.034      0.099      0.922      -0.064       0.071
CBR           -6.7010      0.406    -16.500      0.000      -7.499      -5.903
CIR            0.6331      0.334      1.896      0.059      -0.023       1.289
==============================================================================
Omnibus:                      130.039   Durbin-Watson:                   0.058
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              322.107
Skew:                           1.304   Prob(JB):                     1.14e-70
Kurtosis:                       5.938   Cond. No.                     1.19e+03
==============================================================================
```

The R-squared value of 0.906 indicates that the model explains 90.6% of the variance in the dependent variable, which is a high value. The F-statistic of 953.3 is significant at a high level, suggesting that the model is a good fit for the data. The low Durbin-Watson statistic of 0.058 indicates the presence of significant autocorrelation in the residuals, which may need to be addressed. Overall, the model seems to provide a good fit to the data and explains a high proportion of the variance in the dependent variable.