OLS Regression Results                            
==============================================================================
Dep. Variable:            body_mass_g   R-squared:                       0.347
Model:                            OLS   Adj. R-squared:                  0.345
Method:                 Least Squares   F-statistic:                     176.2
Date:                Tue, 14 Jan 2025   Prob (F-statistic):           1.54e-32
Time:                        12:03:02   Log-Likelihood:                -2629.1
No. Observations:                 333   AIC:                             5262.
Df Residuals:                     331   BIC:                             5270.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==================================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------
Intercept        388.8452    289.817      1.342      0.181    -181.271     958.961
bill_length_mm    86.7918      6.538     13.276      0.000      73.931      99.652
==============================================================================
Omnibus:                        6.141   Durbin-Watson:                   0.845
Prob(Omnibus):                  0.046   Jarque-Bera (JB):                4.899
Skew:                          -0.197   Prob(JB):                       0.0864
Kurtosis:                       2.555   Cond. No.                         360.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

![image](https://github.com/user-attachments/assets/20bb98df-1c9c-4797-9c62-e8d6c8c6b498)


The predicted body mass is: 2992.60 g
(input: Bill=30)

------

OLS Regression Results
This section provides an overview of the regression model and its performance metrics.

Dep. Variable: body_mass_g

The dependent variable we are trying to predict is body_mass_g (body mass in grams).
R-squared: 0.347

The R-squared value indicates that approximately 34.7% of the variance in the body mass can be explained by the model.
Adj. R-squared: 0.345

The adjusted R-squared value accounts for the number of predictors in the model. It is slightly lower than the R-squared value, indicating a good fit.
F-statistic: 176.2

The F-statistic tests the overall significance of the model. A high value indicates that the predictor is significantly related to the dependent variable.
Prob (F-statistic): 1.54e-32

The p-value associated with the F-statistic is extremely low, indicating that the model is statistically significant.
Log-Likelihood: -2629.1

The log-likelihood value measures the goodness of fit of the model. Higher values (less negative) indicate a better fit.
No. Observations: 333

The number of observations (data points) used in the model.
AIC: 5262.

The Akaike Information Criterion, used for model comparison. Lower values indicate a better fit.
BIC: 5270.

The Bayesian Information Criterion, similar to AIC but with a higher penalty for models with more parameters.
Coefficients
This section provides the estimated coefficients for each predictor in the model, along with their standard errors, t-values, p-values, and confidence intervals.

| Coefficient | Value | Std. Err | t | P>|t| | [0.025 | 0.975] | |-------------|-------|----------|---|-----|-------|-------| | Intercept | 388.8452 | 289.817 | 1.342 | 0.181 | -181.271 | 958.961 | | bill_length_mm | 86.7918 | 6.538 | 13.276 | 0.000 | 73.931 | 99.652 |

Intercept: 388.8452

The estimated body mass when the bill length is zero. This coefficient is not statistically significant (p = 0.181).
bill_length_mm: 86.7918

The effect of bill length on body mass. This coefficient is positive and highly significant (p < 0.000), indicating that an increase in bill length is associated with an increase in body mass.
Diagnostics
Omnibus: 6.141

A test for normality of the residuals. A low value indicates that the residuals are normally distributed.
Prob(Omnibus): 0.046

The p-value associated with the Omnibus test. A value below 0.05 suggests that there is some evidence against the normality of the residuals.
Durbin-Watson: 0.845

A test for autocorrelation of the residuals. Values close to 2 indicate no autocorrelation. A value of 0.845 suggests some positive autocorrelation.
Jarque-Bera (JB): 4.899

Another test for normality of the residuals.
Prob(JB): 0.0864

The p-value associated with the Jarque-Bera test. A value above 0.05 suggests that there is no strong evidence against the normality of the residuals.
Skew: -0.197

A measure of the asymmetry of the residuals. Values close to zero indicate symmetry.
Kurtosis: 2.555

A measure of the "tailedness" of the residuals. Values close to 3 indicate a normal distribution.
Cond. No.: 360.

A measure of multicollinearity. Values much higher than 30 may indicate multicollinearity problems.
Notes
Standard Errors: Assume that the covariance matrix of the errors is correctly specified.
Prediction
The predicted body mass is: 2992.60 g
This is the predicted body mass based on the input value for bill length provided by the operator.

Summary
The regression model shows that bill length is a significant predictor of body mass in penguins. 
The R-squared value indicates that the model explains about 34.7% of the variance in body mass. 
The coefficient for bill length is positive and highly significant, suggesting that longer bills are associated with higher body mass. 
The diagnostics indicate that the residuals are approximately normally distributed, although there is some evidence of positive autocorrelation. 
The predicted body mass based on the input value is 2992.60 grams.



