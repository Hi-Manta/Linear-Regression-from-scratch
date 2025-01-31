#importing numpy library
import numpy as np

#initiating train_set(x) and target_set(y)
x = np.array([[1, 2], [2,3]])
y = np.array([[4], [7]])

#initial weights for prediction function
w = 8
b = 5

#iteration range
for _ in range(100000):

    #function for prediction
    def predict(x, w, b):
        #Source: https://www.cuemath.com/algebra/linear-equations/
        return np.array([[w * x[0,0] + b *x[0,1]], [w * x[1,0] + b *x[1,1]]])

    #function for calculating error
    def rmse(prediction):
        #Source: https://www.kaggle.com/discussions/general/215997
        return np.sqrt(np.mean(np.square(y - prediction)))

    #function for calculating gradient of the prediction equation
    def gradient(w,b):
        return w + b

    def cost(w, b):
        return np.sqrt(np.mean(np.square(y - prediction)))

    prediction = predict(x, w, b)

    learning_rate = 0.01
    #changing weights by using learning rate and gradient
    w = w - learning_rate * gradient(w, b)
    b = b - learning_rate * gradient(w, b)

    #printing the cost/error, prediction of the targets and both weights for the predictions
    if (rmse(prediction) < 0.5):
        print("COST:", rmse(prediction), "  Prediction:", prediction, "  W:", round(w), "  b:", round(b) )