import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from 자료_불러오기 import fish
out = Path(__file__).resolve().parents[1] / 'assets'
out.mkdir(exist_ok=True)
fish_source = fish()
length = np.concatenate([fish_source['bream_length'], fish_source['smelt_length']])
weight = np.concatenate([fish_source['bream_weight'], fish_source['smelt_weight']])
fish_input = np.column_stack([length, weight])
fish_target = np.r_[np.ones(35), np.zeros(14)]
model = KNeighborsClassifier().fit(fish_input, fish_target)
print('shape', fish_input.shape, fish_target.shape)
print('train accuracy', model.score(fish_input, fish_target), 'new', model.predict([[30, 600]]))
print('k49', KNeighborsClassifier(n_neighbors=49).fit(fish_input, fish_target).score(fish_input, fish_target))
for k in range(5, 50):
    model.n_neighbors = k
    score = model.score(fish_input, fish_target)
    if score < 1:
        print('first error', k, score)
        break
# 내부 속성은 학습 관찰용이며 일반 프로그램에서는 공개 API를 사용
print('stored samples', model._fit_X.shape)
ordered = KNeighborsClassifier().fit(fish_input[:35], fish_target[:35])
print('ordered split', ordered.score(fish_input[35:], fish_target[35:]))
np.random.seed(42)
indexes = np.arange(len(fish_input))
np.random.shuffle(indexes)
train_indices, test_indices = (indexes[:35], indexes[35:])
model = KNeighborsClassifier().fit(fish_input[train_indices], fish_target[train_indices])
print('shuffled score', model.score(fish_input[test_indices], fish_target[test_indices]))
print('prediction', model.predict(fish_input[test_indices]))
print('target', fish_target[test_indices])
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
for ax, train, test, title in [(axes[0], np.arange(35), np.arange(35, 49), 'Ordered'), (axes[1], train_indices, test_indices, 'Shuffled')]:
    ax.scatter(fish_input[train, 0], fish_input[train, 1], label='Train')
    ax.scatter(fish_input[test, 0], fish_input[test, 1], marker='x', label='Test')
    ax.set(title=title, xlabel='Length (cm)', ylabel='Weight (g)')
    ax.legend()
fig.tight_layout()
fig.savefig(out / '데이터-분할-비교.png', dpi=140)
plt.close(fig)
for stratify in [None, fish_target]:
    train_input, test_input, train_target, test_target = train_test_split(fish_input, fish_target, stratify=stratify, random_state=42)
    print('test counts', 'random' if stratify is None else 'stratified', np.unique(test_target, return_counts=True))
