import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from 자료_불러오기 import perch, perch_frame
out = Path(__file__).resolve().parents[1] / 'assets'
out.mkdir(exist_ok=True)
perch_frame_df = perch_frame()
print(perch_frame_df.head().to_string())
perch_input = perch_frame_df.to_numpy()
perch_weight = perch()['perch_weight']
print('full', perch_input.shape, perch_weight.shape)
train_input, test_input, train_target, test_target = train_test_split(perch_input, perch_weight, random_state=42)
print('split', train_input.shape, test_input.shape)
toy = PolynomialFeatures().fit([[2, 3]])
print('toy', toy.transform([[2, 3]]))
transform2 = PolynomialFeatures(degree=2, include_bias=False).fit(train_input)
train_poly_2 = transform2.transform(train_input)
test_poly_2 = transform2.transform(test_input)
transform5 = PolynomialFeatures(degree=5, include_bias=False).fit(train_input)
train_poly_5 = transform5.transform(train_input)
test_poly_5 = transform5.transform(test_input)
print('features', transform2.get_feature_names_out(['length', 'height', 'width']))
for train, test in [(train_poly_2, test_poly_2), (train_poly_5, test_poly_5)]:
    model = LinearRegression().fit(train, train_target)
    print('feature count, train R2, test R2', train.shape[1], model.score(train, train_target), model.score(test, test_target))
scaler = StandardScaler().fit(train_poly_5)
train = scaler.transform(train_poly_5)
test = scaler.transform(test_poly_5)
print('scaler mean and scale (first 3)', scaler.mean_[:3], scaler.scale_[:3])
print('scaled shape', train.shape, test.shape)
models = [('Unregulated', LinearRegression()), ('Ridge', Ridge(alpha=0.1)), ('Lasso', Lasso(alpha=10, max_iter=10000))]
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
for name, model in models:
    model.fit(train, train_target)
    print(name, 'train/test R2, L2 norm, zero coefficients', model.score(train, train_target), model.score(test, test_target), np.linalg.norm(model.coef_), int((model.coef_ == 0).sum()))
    if name != 'Unregulated':
        axes[0].plot(model.coef_, marker='o', markersize=3, label=name)
axes[0].axhline(0, color='gray', linestyle='--')
axes[0].set(xlabel='Feature index', ylabel='Coefficient')
axes[0].legend()
alphas = [0.001, 0.01, 0.1, 1, 10, 100]
for cls, name in [(Ridge, 'Ridge'), (Lasso, 'Lasso')]:
    tr_scores = []
    te_scores = []
    for alpha in alphas:
        model = cls(alpha=alpha, **{'max_iter': 10000} if cls == Lasso else {}).fit(train, train_target)
        tr_scores.append(model.score(train, train_target))
        te_scores.append(model.score(test, test_target))
        print(name, alpha, model.score(train, train_target), model.score(test, test_target), int((model.coef_ == 0).sum()))
    axes[1].semilogx(alphas, te_scores, 'o-', label=name + ' test')
    plt.figure()
    plt.semilogx(alphas, tr_scores, 'o-', label='Train')
    plt.semilogx(alphas, te_scores, 'o-', label='Test')
    plt.xlabel('alpha')
    plt.ylabel('R²')
    plt.legend()
    plt.tight_layout()
    plt.savefig(out / (('릿지-점수-변화.png' if name == 'Ridge' else '라쏘-점수-변화.png')), dpi=140)
    plt.close()
axes[1].set(xlabel='alpha', ylabel='Test R²')
axes[1].legend()
fig.tight_layout()
fig.savefig(out / '계수와-규제강도.png', dpi=140)
plt.close(fig)
x = np.linspace(-2, 2, 200)
plt.figure()
plt.plot(x, np.abs(x), label='L1: absolute value')
plt.plot(x, x * x, label='L2: square')
plt.xlabel('Coefficient')
plt.ylabel('Penalty at alpha=1')
plt.legend()
plt.tight_layout()
plt.savefig(out / '규제-벌점-형태.png', dpi=140)
plt.close()
for alpha in [0, 0.01, 0.1, 1]:
    print('A/B objective', alpha, 10 + alpha * 100, 15 + alpha * 9)
