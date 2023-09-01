<center> <h1><u> Linear Regression </u></h1></center>

<div align="justify">Linear Regression is a supervised machine learning algorithm. More generally, a linear model makes a prediction by simply computing a weighted sum of input features, plus a constant called the bias term (also known as intercept term). - Aurelien Geron</div>
<br>
<div align="justify">Linear Regression is a linear approach to modeling the relationship between a scalar response (or dependent variable) and one or more explanatory variables (or independent variables). The case of one explanatory variable is called simple linear regression. For more than one explanatory variable, the process is called multiple linear regression.</div>
<br>
##### *Linear Regression Equation:*
>$$\hat{y} = \theta_0 + \theta_1x_1 + \theta_2x_2 + ... + \theta_nx_n$$
>$$\hat{y} = h_\theta(x) = \theta^T \cdot x$$
##### Vectorized form:
>$$\hat{y} = h_\theta(x) = \theta . x$$

##### *Minimum Cost Function:*
$$MSE(X, h_\theta) = \frac{1}{m} \sum_{i=1}^{m} (\theta^T \cdot x^{(i)} - y^{(i)})^2$$

##### *Normal Equation:*
<div algin="justify">
    To find the mathematical value of the parameters that minimizes the cost function, there is a closed-form solution - in other words, a mathematical equation that gives the result directly. This is called the Normal Equation.

$$\hat{\theta} = (X^T \cdot X)^{-1} \cdot X^T \cdot y$$

</div>

