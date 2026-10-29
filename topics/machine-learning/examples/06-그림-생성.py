import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from 자료_불러오기 import perch, perch_frame
out = Path(__file__).resolve().parents[1] / 'assets'
out.mkdir(exist_ok=True)
perch_data = perch()
train_input, test_input, train_target, test_target = train_test_split(perch_data['perch_length'], perch_data['perch_weight'], random_state=42)
train_input = train_input.reshape(-1, 1)
grid = np.linspace(8, 45, 500).reshape(-1, 1)
fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharey=True)
for ax, k in zip(axes, [3, 5, 10]):
    model = KNeighborsRegressor(n_neighbors=k).fit(train_input, train_target)
    ax.scatter(train_input[:, 0], train_target, s=15)
    ax.plot(grid, model.predict(grid), color='darkorange')
    ax.set(title=f'k={k}', xlabel='Length (cm)')
axes[0].set_ylabel('Weight (g)')
fig.tight_layout()
fig.savefig(out / '이웃-수-비교.png', dpi=140)
plt.close(fig)
model = KNeighborsRegressor(n_neighbors=3).fit(train_input, train_target)
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, x in zip(axes, [50, 100]):
    _, ids = model.kneighbors([[x]])
    ax.scatter(train_input[:, 0], train_target, s=15, label='Training')
    ax.scatter(train_input[ids[0], 0], train_target[ids[0]], marker='D', label='Neighbors')
    ax.scatter(x, model.predict([[x]])[0], marker='^', label='Prediction')
    ax.set(xlabel='Length (cm)', ylabel='Weight (g)', title=f'Query {x} cm')
    ax.legend()
fig.tight_layout()
fig.savefig(out / '훈련범위-밖-이웃.png', dpi=140)
plt.close(fig)
model = LinearRegression().fit(train_input, train_target)
xx = np.linspace(0, 50, 100)
yy = model.coef_[0] * xx + model.intercept_
plt.figure()
plt.plot(xx, yy, label='Fitted line')
plt.scatter([0], [model.intercept_], label='Intercept')
x0 = 30
x1 = 40
y0 = model.predict([[x0]])[0]
y1 = model.predict([[x1]])[0]
plt.plot([x0, x1, x1], [y0, y0, y1], '--', label='Rise / run')
plt.xlabel('Length (cm)')
plt.ylabel('Predicted weight (g)')
plt.legend()
plt.tight_layout()
plt.savefig(out / '기울기와-절편.png', dpi=140)
plt.close()
full = perch_frame().to_numpy()
train_input, test_input, train_target, test_target = train_test_split(full, perch_data['perch_weight'], random_state=42)
scores = []
for degree in [2, 5]:
    transformer = PolynomialFeatures(degree=degree, include_bias=False).fit(train_input)
    train_poly = transformer.transform(train_input)
    test_poly = transformer.transform(test_input)
    model = LinearRegression().fit(train_poly, train_target)
    scores.append([model.score(train_poly, train_target), model.score(test_poly, test_target)])
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for i, title in enumerate(['Train R²', 'Test R²']):
    axes[i].bar(['Degree 2', 'Degree 5'], [s[i] for s in scores])
    axes[i].set_title(title)
fig.tight_layout()
fig.savefig(out / '특성차수별-점수.png', dpi=140)
plt.close(fig)
# 합성 데이터로 만든 개념 예시. 농어 실험 결과가 아님
rng = np.random.default_rng(42)
x = np.linspace(-1, 1, 25)
y = x * x + rng.normal(0, 0.12, len(x))
g = np.linspace(-1, 1, 300)
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
for ax, degree in zip(axes, [1, 4, 15]):
    coef = np.polynomial.polynomial.polyfit(x, y, degree)
    pred = np.polynomial.polynomial.polyval(g, coef)
    ax.scatter(x, y, s=15)
    ax.plot(g, pred)
    ax.set(title=f'Concept: degree {degree}', xlabel='Synthetic input', ylim=(-0.5, 1.5))
axes[0].set_ylabel('Synthetic target')
fig.tight_layout()
fig.savefig(out / '모델-복잡도.png', dpi=140)
plt.close(fig)
print('Generated five visual checks. Degree scores:', scores)
