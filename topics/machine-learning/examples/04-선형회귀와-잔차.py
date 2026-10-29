import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error
from 자료_불러오기 import perch
out = Path(__file__).resolve().parents[1] / 'assets'
out.mkdir(exist_ok=True)
perch_data = perch()
train_input, test_input, train_target, test_target = train_test_split(perch_data['perch_length'], perch_data['perch_weight'], random_state=42)
train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)
train_poly = np.column_stack([train_input ** 2, train_input])
test_poly = np.column_stack([test_input ** 2, test_input])
linear = LinearRegression().fit(train_input, train_target)
quadratic = LinearRegression().fit(train_poly, train_target)
knn = KNeighborsRegressor(n_neighbors=3).fit(train_input, train_target)
print('training range', train_input.min(), train_input.max())
for query in [50, 100]:
    distances, indexes = knn.kneighbors([[query]])
    print('KNN', query, 'neighbors', train_input[indexes[0], 0], 'weights', train_target[indexes[0]], 'prediction', knn.predict([[query]]))
print('linear parameters', linear.coef_, linear.intercept_)
print('polynomial parameters', quadratic.coef_, quadratic.intercept_)
manual = quadratic.coef_[0] * 40 ** 2 + quadratic.coef_[1] * 40 + quadratic.intercept_
print('40 manual and predict', manual, quadratic.predict([[1600, 40]])[0])
for x in [30, 40, 50, 60]:
    print('length and predictions', x, knn.predict([[x]])[0], linear.predict([[x]])[0], quadratic.predict([[x * x, x]])[0])
fig, axes = plt.subplots(1, 2, figsize=(11, 4), sharey=True)
for ax, model, data, title in [(axes[0], linear, test_input, 'Linear'), (axes[1], quadratic, test_poly, 'Polynomial')]:
    prediction = model.predict(data)
    residual = test_target - prediction
    print(title, 'train/test R2 and MAE', model.score(train_input if title == 'Linear' else train_poly, train_target), model.score(data, test_target), mean_absolute_error(test_target, prediction))
    worst = np.argsort(np.abs(residual))[-3:][::-1]
    for i in worst:
        print('worst: length, actual, predicted, residual', test_input[i, 0], test_target[i], prediction[i], residual[i])
    closest = np.argmin(test_input[:, 0])
    print('smallest fish', test_input[closest, 0], test_target[closest], prediction[closest], residual[closest])
    ax.scatter(test_input[:, 0], residual)
    ax.axhline(0, color='gray', linestyle='--')
    ax.set(title=title, xlabel='Length (cm)')
axes[0].set_ylabel('Actual - predicted (g)')
fig.tight_layout()
fig.savefig(out / '잔차-비교.png', dpi=140)
plt.close(fig)
