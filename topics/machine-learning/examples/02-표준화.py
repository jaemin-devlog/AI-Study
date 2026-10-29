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
fish_input = np.column_stack([np.r_[fish_source['bream_length'], fish_source['smelt_length']], np.r_[fish_source['bream_weight'], fish_source['smelt_weight']]])
fish_target = np.r_[np.ones(35), np.zeros(14)]
train_input, test_input, train_target, test_target = train_test_split(fish_input, fish_target, stratify=fish_target, random_state=42)
mean = train_input.mean(axis=0)
std = train_input.std(axis=0)
train_scaled = (train_input - mean) / std
new_fish = np.array([[25, 150]])
fig, axes = plt.subplots(1, 3, figsize=(13, 4))
for ax, data, query, title in [(axes[0], train_input, new_fish, 'Raw'), (axes[1], train_input, new_fish, 'Only axis limits changed'), (axes[2], train_scaled, (new_fish - mean) / std, 'Standardized')]:
    model = KNeighborsClassifier().fit(data, train_target)
    distances, indexes = model.kneighbors(query)
    print(title, 'prediction', model.predict(query), 'neighbors', train_target[indexes], 'distance', np.round(distances, 2))
    print('neighbor input', data[indexes[0]])
    ax.scatter(data[:, 0], data[:, 1], s=16, label='Train')
    ax.scatter(data[indexes[0], 0], data[indexes[0], 1], marker='D', facecolors='none', edgecolors='red', label='Neighbors')
    ax.scatter(query[:, 0], query[:, 1], marker='^', c='black', label='New')
    ax.set_title(title)
    ax.legend(fontsize=7)
axes[0].set(xlabel='Length (cm)', ylabel='Weight (g)')
axes[1].set(xlim=(0, 1000), xlabel='Length (cm)')
axes[2].set(xlabel='Length z score', ylabel='Weight z score')
fig.tight_layout()
fig.savefig(out / '표준화와-이웃.png', dpi=140)
plt.close(fig)
print('mean', mean, 'std', std, 'new z', (new_fish - mean) / std)
print('raw and scaled test accuracy', KNeighborsClassifier().fit(train_input, train_target).score(test_input, test_target), KNeighborsClassifier().fit(train_scaled, train_target).score((test_input - mean) / std, test_target))
