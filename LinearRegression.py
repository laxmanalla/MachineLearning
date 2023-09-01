import numpy as np
from sklearn.preprocessing import add_dummy_feature
import matplotlib.pyplot as plt

np.random.seed(43)
m = 100
X = 2 * np.random.rand(m, 1)
y = 4 + 3 * X + np.random.randn(m, 1)

X_b = add_dummy_feature(X)
theta_best = np.linalg.inv(X_b .T @ X_b) @ X_b.T @ y

print(theta_best)


#prediction

X_new = np.array([[0], [2]])
X_new_b = add_dummy_feature(X_new)
y_predict = X_new_b @ theta_best
print(y_predict)


plt.plot(X_new, y_predict, "r-", label="predictions")
plt.plot(X, y, "b.")
[...]
plt.show()