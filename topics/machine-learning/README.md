# 머신러닝 기초

머신러닝의 기본 흐름부터 특성 공학과 규제까지 파일 번호 순서대로 정리

## 1. 머신러닝의 기본 흐름과 데이터 준비

| 번호 | 내용 |
| --- | --- |
| 00 | [전체 정리](01-ml-basics/00-전체-정리.md) |
| 01 | [인공지능과 머신러닝](01-ml-basics/01-인공지능과-머신러닝.md) |
| 02 | [생선 데이터와 최근접 이웃](01-ml-basics/02-생선-데이터와-최근접-이웃.md) |
| 03 | [훈련 세트와 테스트 세트](01-ml-basics/03-훈련-세트와-테스트-세트.md) |
| 04 | [넘파이와 데이터 분할](01-ml-basics/04-넘파이와-데이터-분할.md) |
| 05 | [특성의 스케일과 표준화](01-ml-basics/05-특성의-스케일과-표준화.md) |
| 06 | [생선 분류 예제](01-ml-basics/06-생선-분류-예제.md) |
| 07 | [표준화 예제](01-ml-basics/07-표준화-예제.md) |
| 08 | [인공지능과 생선데이터](01-ml-basics/08-인공지능과-생선데이터.md) |
| 09 | [최근접 이웃 분류](01-ml-basics/09-최근접-이웃-분류.md) |
| 10 | [훈련과 테스트 분리](01-ml-basics/10-훈련과-테스트-분리.md) |
| 11 | [특성 스케일과 표준화](01-ml-basics/11-특성-스케일과-표준화.md) |

## 2. 최근접 이웃 회귀

| 번호 | 내용 |
| --- | --- |
| 00 | [전체 정리](02-knn-regression/00-전체-정리.md) |
| 01 | [최근접 이웃 회귀](02-knn-regression/01-최근접-이웃-회귀.md) |
| 02 | [회귀 모델 평가 지표](02-knn-regression/02-회귀-모델-평가-지표.md) |
| 03 | [과대적합과 이웃 수](02-knn-regression/03-과대적합과-이웃-수.md) |
| 04 | [오차와 손실함수](02-knn-regression/04-오차와-손실함수.md) |
| 05 | [최근접 이웃 회귀 예제](02-knn-regression/05-최근접-이웃-회귀-예제.md) |
| 06 | [회귀와 최근접 이웃 예측](02-knn-regression/06-회귀와-최근접-이웃-예측.md) |
| 07 | [농어 데이터와 최근접 이웃 학습](02-knn-regression/07-농어-데이터와-최근접-이웃-학습.md) |
| 08 | [회귀 모델 평가](02-knn-regression/08-회귀-모델-평가.md) |
| 09 | [과대적합과 이웃 수](02-knn-regression/09-과대적합과-이웃-수.md) |

## 3. 선형 회귀

| 번호 | 내용 |
| --- | --- |
| 00 | [전체 정리](03-linear-regression/00-전체-정리.md) |
| 01 | [선형 회귀 기초](03-linear-regression/01-선형-회귀-기초.md) |
| 02 | [다항 회귀 기초](03-linear-regression/02-다항-회귀-기초.md) |
| 03 | [회귀 잔차 예제](03-linear-regression/03-회귀-잔차-예제.md) |
| 04 | [최근접 이웃 회귀의 한계](03-linear-regression/04-최근접-이웃-회귀의-한계.md) |
| 05 | [선형 회귀](03-linear-regression/05-선형-회귀.md) |
| 06 | [다항 회귀](03-linear-regression/06-다항-회귀.md) |
| 07 | [회귀모델과 잔차 비교](03-linear-regression/07-회귀모델과-잔차-비교.md) |

## 4. 특성 공학과 규제

| 번호 | 내용 |
| --- | --- |
| 00 | [전체 정리](04-feature-engineering-and-regularization/00-전체-정리.md) |
| 01 | [다항 특성 생성](04-feature-engineering-and-regularization/01-다항-특성-생성.md) |
| 02 | [릿지와 라쏘 기초](04-feature-engineering-and-regularization/02-릿지와-라쏘-기초.md) |
| 03 | [특성 공학과 규제 예제](04-feature-engineering-and-regularization/03-특성-공학과-규제-예제.md) |
| 04 | [다중회귀와 특성공학](04-feature-engineering-and-regularization/04-다중회귀와-특성공학.md) |
| 05 | [특성확장과 과대적합](04-feature-engineering-and-regularization/05-특성확장과-과대적합.md) |
| 06 | [규제와 표준화](04-feature-engineering-and-regularization/06-규제와-표준화.md) |
| 07 | [릿지와 라쏘](04-feature-engineering-and-regularization/07-릿지와-라쏘.md) |

## 그림 설명

| 내용 | 설명 |
| --- | --- |
| [그림 살펴보기](그림-살펴보기.md) | 학습 문서에 나온 그림과 해석 |

[전체 공부 기록](../../README.md)

## 예제 실행

저장소 루트에서 필요한 라이브러리를 설치한 뒤 예제 파일을 실행. 데이터는 온라인에서 불러오며, 실습 자료가 있는 경우 `ML_NOTEBOOK_DIR` 환경 변수에 해당 폴더를 지정할 수 있음.

```powershell
python -m pip install -r topics/machine-learning/examples/필요-라이브러리.txt
python topics/machine-learning/examples/01-생선-분류.py
```

| 파일 | 내용 |
| --- | --- |
| [01 생선 분류](examples/01-생선-분류.py) | 최근접 이웃을 이용한 생선 분류 |
| [02 표준화](examples/02-표준화.py) | 특성 스케일과 표준화 |
| [03 최근접 이웃 회귀](examples/03-최근접-이웃-회귀.py) | 농어 무게 예측과 평가 |
| [04 선형 회귀와 잔차](examples/04-선형회귀와-잔차.py) | 선형 및 다항 회귀와 잔차 비교 |
| [05 특성 공학과 규제](examples/05-특성공학과-규제.py) | 다항 특성, 릿지와 라쏘 |
| [06 그림 생성](examples/06-그림-생성.py) | 학습용 그래프 생성 |
| [자료 불러오기](examples/자료_불러오기.py) | 예제에서 사용하는 데이터 로딩 |
| [필요 라이브러리](examples/필요-라이브러리.txt) | 예제 실행에 필요한 패키지 목록 |
| [실행 결과](examples/results/) | 예제별 출력값과 경고 기록 |
