import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error
from 자료_불러오기 import perch
out = Path(__file__).resolve().parents[1] / 'assets'
out.mkdir(exist_ok=True)
perch_data = perch()
train_input, test_input, train_target, test_target = train_test_split(perch_data['perch_length'], perch_data['perch_weight'], random_state=42)
print('before reshape', train_input.shape, test_input.shape)
train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)
print('after reshape', train_input.shape, test_input.shape)
model = KNeighborsRegressor().fit(train_input, train_target)
for length in [30, 35]:
    distances, indexes = model.kneighbors([[length]])
    neighbor_weights = train_target[indexes[0]]
    print('query', length, 'shapes', distances.shape, indexes.shape)
    print('neighbor lengths', train_input[indexes[0], 0], 'distance', distances[0], 'weight', neighbor_weights)
    print('manual', neighbor_weights.mean(), 'predict', model.predict([[length]])[0])
print('k train_r2 test_r2 mae')
for k in [1, 3, 5, 10, 20, 42]:
    model = KNeighborsRegressor(n_neighbors=k).fit(train_input, train_target)
    print(k, round(model.score(train_input, train_target), 4), round(model.score(test_input, test_target), 4), round(mean_absolute_error(test_target, model.predict(test_input)), 2))
# 같은 길이의 샘플이 여럿이면 k=1이어도 자기 자신이 선택된다는 보장은 없음
for length in np.unique(train_input):
    targets = train_target[train_input[:, 0] == length]
    if len(targets) > 1:
        print('duplicate length', length, 'weights', targets)
plt.scatter(perch_data['perch_length'], perch_data['perch_weight'])
plt.xlabel('Length (cm)')
plt.ylabel('Weight (g)')
plt.tight_layout()
plt.savefig(out / '농어-분포.png', dpi=140)
plt.close()
