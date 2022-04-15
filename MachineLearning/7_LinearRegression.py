import pandas as pd
import matplotlib.pyplot as plt
dataframe = pd.read_csv('Advertising.csv')
#print(dataframe)
X = dataframe.values[:, 2]
y = dataframe.values[:, 4]
#plt.scatter(X, y, marker='o')
#plt.show()
def cost_function(X, y, weight, bias):
    total_cost = 0
    for i in range(len(X)):
        y_pred = predict(X[i], weight, bias)
        total_cost += (y[i] - y_pred) ** 2
    return total_cost / len(X)
def predict(new_radio, weight, bias):
    return new_radio * weight + bias

def update_weight(X, y, weight, bias, learning_rate):
    weight_temp = 0
    bias_temp = 0
    for i in range(len(X)):
        weight_temp += -2 * X[i] * (y[i] - predict(X[i], weight, bias))
        bias_temp += -2 * (y[i] - predict(X[i], weight, bias))
    weight -= learning_rate * weight_temp/len(X)
    bias -= learning_rate * bias_temp/len(X)
    return weight, bias
def train(X, y , weight, bias, learning_rate, iter):
    cos_his = []
    for i in range(iter):
        weight, bias = update_weight(X, y, weight, bias, learning_rate)
        cost = cost_function(X, y, weight, bias)
        cos_his.append(cost)
    return weight , bias, cos_his
weight, bias, cost = train(X, y, 0.03, 0.0014, 0.001, 100)
print(weight, bias, cost)
print(predict(19, weight, bias))
solanlap = [i for i in range(100)]
plt.plot(solanlap, cost)
plt.show()
