import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

# Generate synthetic data
X, y = make_regression(n_samples=4, n_features=1, n_informative=1, n_targets=1, noise=20, random_state=13)

# Plot the generated data points
plt.scatter(X, y)
plt.show()

# Apply Ordinary Least Squares (OLS) regression
reg = LinearRegression()
reg.fit(X, y)
print("Coefficient from OLS:", reg.coef_)
print("Intercept from OLS:", reg.intercept_)

# Plot the OLS regression line
plt.scatter(X, y)
plt.plot(X, reg.predict(X), color='red', label='OLS')
plt.show()

# --- Gradient Descent Demonstration ---

# Assume a constant slope and an initial intercept of 0
m = 78.35
b = 0

# Calculate initial prediction with b=0
y_pred = ((m * X) + b).reshape(4)

# Plot OLS line vs. initial guess line (b=0)
plt.scatter(X, y)
plt.plot(X, reg.predict(X), color='red', label='OLS')
plt.plot(X, y_pred, color='#00a65a', label='b = 0')
plt.legend()
plt.show()

# Set the learning rate
lr = 0.1

# --- Iteration 1 ---
# Calculate the loss slope (gradient) for the intercept
loss_slope = - np.sum(y - m * X.ravel() - b)
print("Iteration 1, Loss Slope:", loss_slope)

# Calculate the step size
step_size = loss_slope * lr
print("Iteration 1, Step Size:", step_size)

# Update the intercept
b = b - step_size
print("Iteration 1, New Intercept (b):", b)

# Calculate new predictions
y_pred1 = ((m * X) + b).reshape(4)

# Plot the updated line
plt.scatter(X, y)
plt.plot(X, reg.predict(X), color='red', label='OLS')
plt.plot(X, y_pred, color='#A3E4D7', label='b = 0')
plt.plot(X, y_pred1, color='#00a65a', label=f'b = {b}')
plt.legend()
plt.show()

# --- Iteration 2 ---
loss_slope = - np.sum(y - m * X.ravel() - b)
print("Iteration 2, Loss Slope:", loss_slope)
step_size = loss_slope * lr
print("Iteration 2, Step Size:", step_size)
b = b - step_size
print("Iteration 2, New Intercept (b):", b)
y_pred2 = ((m * X) + b).reshape(4)

# Plot the updated line
plt.scatter(X, y)
plt.plot(X, reg.predict(X), color='red', label='OLS')
plt.plot(X, y_pred, color='lightcyan', label='b = 0')
plt.plot(X, y_pred1, color='paleturquoise', label=f'b after 1st iter')
plt.plot(X, y_pred2, color='#00a65a', label=f'b = {b}')
plt.legend()
plt.show()


# --- Gradient Descent using a Loop ---
b = -100  # Starting intercept
m = 78.35 # Constant slope
lr = 0.01 # Learning rate
epochs = 100 # Number of iterations

plt.figure(figsize=(9, 5))
plt.scatter(X, y)

for i in range(epochs):
    loss_slope = - np.sum(y - m * X.ravel() - b)
    b = b - (lr * loss_slope)
    y_pred_loop = m * X + b
    plt.plot(X, y_pred_loop)

plt.show()