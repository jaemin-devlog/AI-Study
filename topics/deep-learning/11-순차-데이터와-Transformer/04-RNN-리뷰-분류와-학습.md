# RNN 리뷰 분류와 학습

> Day 5 이론 2, 5~6절 (13~20쪽)

## 리뷰 하나가 확률 하나가 되는 과정

| 단계 | 배치 64개의 형태 | 수행하는 일 |
| --- | --- | --- |
| 정수 ID | (64, 100) | 리뷰별 토큰 순서 저장 |
| Embedding | (64, 100, 16) | 각 ID를 벡터로 변환 |
| RNN 전체 출력 | (64, 100, 8) | 순서대로 은닉 상태 계산 |
| 마지막 층의 최종 상태 | (64, 8) | 리뷰별 표현 선택 |
| Linear | (64, 1) | 긍정 여부의 점수 계산 |
| Sigmoid | (64, 1) | 긍정 확률로 변환 |

```python
import torch
from torch import nn

class ReviewRNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.embedding = nn.Embedding(500, 16)
        self.rnn = nn.RNN(16, 8, batch_first=True)
        self.dense = nn.Linear(8, 1)

    def forward(self, ids):
        vectors = self.embedding(ids)
        _, hidden = self.rnn(vectors)
        return torch.sigmoid(self.dense(hidden[-1]))
```

`ids`는 정수형 텐서임. 마지막 은닉 상태는 아직 긍정 확률이 아니며, 분류층에서 하나의 점수로 바꾼 뒤 시그모이드를 적용함.

## 예측과 정답으로 가중치 수정

아래는 준비된 `train_loader`를 사용하는 학습 핵심 부분임. 데이터 다운로드와 배치 생성은 별도로 준비해야 함.

```python
model = ReviewRNN()
criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

model.train()
for ids, targets in train_loader:
    optimizer.zero_grad()
    probabilities = model(ids).squeeze(-1)
    loss = criterion(probabilities, targets.float())
    loss.backward()
    optimizer.step()
```

강의처럼 시그모이드 확률을 반환하면 BCELoss와 연결함. BCEWithLogitsLoss를 선택할 경우 모델의 마지막 시그모이드를 제거하고 로짓을 전달해야 함. 두 조합을 섞지 않음.

## 검증 결과 읽기

훈련 손실만 감소하고 검증 손실이 나빠지면 과대적합 가능성을 살펴봄. 검증 손실이 가장 낮은 상태를 저장하고, 모델 선택이 끝난 후 테스트 세트로 최종 평가함. 이 글의 코드는 구조 설명용이며 직접 실행한 정확도를 기록한 것은 아님.

평가 시 `model.eval()`과 `torch.no_grad()`를 사용함. 강의의 기준은 확률이 0.5보다 크면 긍정, 나머지는 부정임. 전체 정답 개수를 전체 리뷰 개수로 나누어 정확도를 계산함. 미니배치별 정확도의 단순 평균은 마지막 배치가 작으면 전체 정확도와 달라질 수 있음.

[이전](03-IMDB-전처리와-임베딩.md) | [다음](05-LSTM과-GRU.md) | [파트 목차](README.md)
