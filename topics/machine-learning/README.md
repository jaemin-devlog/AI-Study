# 머신러닝 기초

머신러닝의 기본 흐름부터 특성 공학과 규제까지 학습 순서대로 정리

## 1. 머신러닝의 기본 흐름과 데이터 준비

| 순서 | 내용 |
| --- | --- |
| 01 | [인공지능과 생선 데이터](01-ml-basics/08-인공지능과-생선데이터.md) |
| 02 | [최근접 이웃 분류와 이웃](01-ml-basics/09-최근접-이웃-분류.md) |
| 03 | [훈련 데이터와 테스트 데이터](01-ml-basics/10-훈련과-테스트-분리.md) |
| 04 | [특성 스케일과 표준화](01-ml-basics/11-특성-스케일과-표준화.md) |

## 2. 최근접 이웃 회귀

| 순서 | 내용 |
| --- | --- |
| 01 | [회귀와 최근접 이웃 예측](02-knn-regression/06-회귀와-최근접-이웃-예측.md) |
| 02 | [농어 데이터와 최근접 이웃 학습](02-knn-regression/07-농어-데이터와-최근접-이웃-학습.md) |
| 03 | [회귀 모델 평가](02-knn-regression/08-회귀-모델-평가.md) |
| 04 | [과대적합과 이웃 수](02-knn-regression/09-과대적합과-이웃-수.md) |

## 3. 선형 회귀

| 순서 | 내용 |
| --- | --- |
| 01 | [최근접 이웃 회귀의 한계](03-linear-regression/04-최근접-이웃-회귀의-한계.md) |
| 02 | [선형 회귀](03-linear-regression/05-선형-회귀.md) |
| 03 | [다항 회귀](03-linear-regression/06-다항-회귀.md) |
| 04 | [회귀 모델과 잔차 비교](03-linear-regression/07-회귀모델과-잔차-비교.md) |

## 4. 특성 공학과 규제

| 순서 | 내용 |
| --- | --- |
| 01 | [다중 회귀와 특성 공학](04-feature-engineering-and-regularization/04-다중회귀와-특성공학.md) |
| 02 | [특성 확장과 과대적합](04-feature-engineering-and-regularization/05-특성확장과-과대적합.md) |
| 03 | [규제와 표준화](04-feature-engineering-and-regularization/06-규제와-표준화.md) |
| 04 | [릿지와 라쏘 회귀](04-feature-engineering-and-regularization/07-릿지와-라쏘.md) |

[그림 살펴보기](그림-살펴보기.md)에서 각 그림의 의미 확인

[전체 공부 기록](../../README.md)

## 예제 실행

저장소 루트에서 필요한 라이브러리를 설치한 뒤 예제 파일을 실행. 데이터는 온라인에서 불러오며, 실습 자료가 있는 경우 `ML_NOTEBOOK_DIR` 환경 변수에 해당 폴더를 지정할 수 있음.

```powershell
python -m pip install -r topics/machine-learning/examples/필요-라이브러리.txt
python topics/machine-learning/examples/01-생선-분류.py
```
