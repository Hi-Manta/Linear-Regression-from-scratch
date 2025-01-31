# A Linear Regression model from scratch

## Overview
This repository contains an implementation of Linear Regression from scratch using only the NumPy library. 
The model is built step by step, including weight initialization, error calculation, and gradient descent optimization.

## Features
- Implements Linear Regression without using any built-in ML libraries.
- Uses Root Mean Squared Error (RMSE) for loss calculation.
- Performs gradient descent optimization to update weights.
- Supports custom learning rate and many iterations.

## Code Explanation
1. Initialize Train set(x) and Target set(y)
2. Initialize Random Weights(w,b)
3. Calculate Gradient(w+b in this case)
4. Calculate Error(RMSE)
5. Update Weights(w - LR * gradient)
6. Print(if RMSE < 0.5)
7. Repeat
