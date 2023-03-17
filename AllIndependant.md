# With all variables

```
X = df[[ 'UNEMPC', 'CEIR', 'MSC', 'TSX', 'BLIC', 'RGDP', 'IRGDP', 'SRGDP', 'CBR', 'CIR']]
# assuming CPICANALL represents inflation
y = df['CPICANALL']

```


```
MSE: 8.945432492110188
RMSE: 2.9908915881573153
CBR      -1.353645e+00
BLIC     -4.828265e-02
TSX      -6.188484e-04
RGDP     -5.717480e-04
MSC       1.594357e-11
IRGDP     6.736992e-04
SRGDP     7.411693e-04
CIR       2.964797e-02
CEIR      1.394406e-01
UNEMPC    5.731830e-01
const     2.614972e+01
dtype: float64
                            OLS Regression Results
==============================================================================
Dep. Variable:              CPICANALL   R-squared:                       0.987
Model:                            OLS   Adj. R-squared:                  0.987
Method:                 Least Squares   F-statistic:                     3679.
Date:                Fri, 17 Mar 2023   Prob (F-statistic):               0.00
Time:                        18:33:34   Log-Likelihood:                -1254.2
No. Observations:                 501   AIC:                             2530.
Df Residuals:                     490   BIC:                             2577.
Df Model:                          10
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         26.1497      5.916      4.420      0.000      14.527      37.773
UNEMPC         0.5732      0.189      3.033      0.003       0.202       0.945
CEIR           0.1394      0.026      5.357      0.000       0.088       0.191
MSC         1.594e-11   1.63e-12      9.784      0.000    1.27e-11    1.91e-11
TSX           -0.0006      0.000     -4.197      0.000      -0.001      -0.000
BLIC          -0.0483      0.015     -3.278      0.001      -0.077      -0.019
RGDP          -0.0006   5.93e-05     -9.639      0.000      -0.001      -0.000
IRGDP          0.0007   5.84e-05     11.539      0.000       0.001       0.001
SRGDP          0.0007   6.74e-05     10.993      0.000       0.001       0.001
CBR           -1.3536      0.195     -6.943      0.000      -1.737      -0.971
CIR            0.0296      0.147      0.201      0.841      -0.260       0.319
==============================================================================
Omnibus:                       15.107   Durbin-Watson:                   0.084
Prob(Omnibus):                  0.001   Jarque-Bera (JB):               15.994
Skew:                           0.437   Prob(JB):                     0.000336
Kurtosis:                       2.955   Cond. No.                     2.61e+13
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.61e+13. This might indicate that there are
strong multicollinearity or other numerical problems.
```