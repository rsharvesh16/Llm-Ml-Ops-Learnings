import numpy as np
print("hi")
def gradient_descent(x, y):
    m_val = b_val = 0
    learning_rate = 0.001
    iterations = 30
    n = len(x)

    for i in range(iterations):
        y_prediction = m_val * x + b_val
        cost = (1/n) * sum([val**2 for val in (y-y_prediction)])
        md = -(2/n) * sum(x*(y - y_prediction))
        bd = -(2/n) * sum(y-y_prediction)
        m_val = m_val - learning_rate * md
        b_val = b_val - learning_rate * bd
        print("m {}, b {}, cost {} iteration {}".format(m_val, b_val, cost, i)) 

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
gradient_descent(x,y)

