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

The coefficients for the other independent variables (MSC, RGDP, TSX, IRGDP, SRGDP) are relatively small compared to the other variables - on the order of < e^-4. Therefore, they may not have a significant impact on inflation.

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

## Summary for all vs 'UNEMPC', 'CEIR', 'BLIC', 'CBR', 'CIR'

```
X = df[['UNEMPC', 'CEIR', 'BLIC', 'CBR', 'CIR']]
# assuming CPICANALL represents inflation
y = df['CPICANALL']
```

```
                            OLS Regression Results                           

==============================================================================
Dep. Variable:              CPICANALL   R-squared:                       0.906
Model:                            OLS   Adj. R-squared:                  0.905
Method:                 Least Squares   F-statistic:                     953.3
Date:                Fri, 17 Mar 2023   Prob (F-statistic):          2.20e-251
Time:                        18:09:55   Log-Likelihood:                -1747.2
No. Observations:                 501   AIC:                             3506.
Df Residuals:                     495   BIC:                             3532.
Df Model:                           5                                        

Covariance Type:            nonrobust                                        

==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
==============================================================================   
Omnibus:                      130.039   Durbin-Watson:                   0.058   
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              322.107   
Skew:                           1.304   Prob(JB):                     1.14e-70   
Kurtosis:                       5.938   Cond. No.                     1.19e+03   
==============================================================================   

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.19e+03. This might indicate that there are  
strong multicollinearity or other numerical problems.
```