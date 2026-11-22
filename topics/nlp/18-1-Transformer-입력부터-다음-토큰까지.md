# Day 4. Transformer 입력부터 다음 토큰까지

> `나는 / 커피를 / 마신다`를 번역할 때, 디코더는 `I` 다음에 올 `drink`를 어떻게 고를까? 아래 그림에서 원문은 왼쪽 인코더로, 지금까지의 번역은 오른쪽 디코더로 들어간다. 두 흐름은 디코더의 Cross-Attention에서 만난다.

![Transformer Encoder–Decoder 구조도. 원문의 인코더 출력이 디코더에 Key와 Value로 전달되고, 선택된 다음 토큰이 디코더 입력에 추가된다.](assets/Transformer-Encoder-Decoder.png)

[구조도 확대 보기 (SVG)](assets/Transformer-Encoder-Decoder.svg)

## 1. 원문을 읽어 위치별 벡터 만들기

**Tokenizer**가 원문을 토큰으로 나누고 어휘집의 ID로 바꾼다. 예를 들어 `나는 / 커피를 / 마신다`를 세 토큰으로 나눴다고 하자. **Token Embedding**은 각 ID에 해당하는 벡터를 가져오고, 그림의 ⊕에서 같은 차원의 **Positional Encoding**을 더한다. 원래 Transformer는 위치마다 다른 사인·코사인 값을 사용한다. 이렇게 하면 같은 토큰이라도 어느 위치에 놓였는지 구분할 수 있다.

인코더의 **Multi-Head Self-Attention**은 같은 입력에서 Query, Key, Value를 만든다. 각 위치는 원문의 앞뒤 토큰을 모두 참조할 수 있다(**Bidirectional Self-Attention**). 따라서 `마신다` 위치의 출력에도 `나는`과 `커피를`의 정보가 반영될 수 있다.

그다음 **Position-wise Feed-Forward Network(FFN)**가 각 위치에 같은 `Linear → ReLU → Linear` 변환을 적용한다. 어텐션은 위치 사이에서 정보를 모으고, FFN은 그렇게 얻은 벡터의 특징을 위치별로 변환한다. 두 연산 뒤의 **Add & Norm**에서는 각 연산의 입력을 그 출력에 더한 뒤 LayerNorm을 적용한다. 그림의 우회 화살표가 이 잔차 연결이다.

그림의 **× 6**은 원래 Transformer에서 서로 다른 가중치를 가진 인코더 블록 여섯 개를 쌓았다는 뜻이다. 원문이 세 토큰이면 마지막 **Encoder Output**에도 세 위치의 벡터가 남는다. 디코더의 각 층은 이 출력을 사용한다.

## 2. 디코더 입력을 한 칸 옮기는 이유

그림 오른쪽 위의 **Shift Right**는 학습할 때 정답 번역을 디코더 입력으로 만드는 과정이다. 시작 토큰 `<BOS>`를 맨 앞에 두면, 각 위치의 정답은 현재 입력 바로 다음에 올 토큰이 된다.

| 위치 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| 디코더 입력 | `<BOS>` | `I` | `drink` | `coffee` |
| 예측할 정답 | `I` | `drink` | `coffee` | `<EOS>` |

디코더도 임베딩에 위치 정보를 더한다. 첫 번째 어텐션인 **Causal Self-Attention**은 **Causal Mask**로 각 위치보다 뒤에 있는 Key를 가린다. 표의 두 번째 위치는 `<BOS> / I`만 참조해서 `drink`를 예측해야 한다. 학습 배치에 정답 문장 전체가 들어 있어도 세 번째 위치의 `drink`를 미리 볼 수 없다. 덕분에 학습 시에는 네 위치의 예측과 손실을 한 번의 순전파에서 계산할 수 있다.

## 3. Cross-Attention에서 원문과 번역 연결하기

**Cross-Attention(Encoder-Decoder Attention)**에서 Query는 바로 앞의 디코더 Add & Norm 출력에서 만든다. Key와 Value는 최종 Encoder Output에서 만든다. 그림에서 디코더 안으로 내려오는 **Q**와 왼쪽에서 들어오는 **K, V**가 이 차이를 나타낸다.

예를 들어 `I`까지 생성했을 때, `I` 위치의 Query는 원문 세 위치의 Key와 각각 비교된다. 각 점수에서 얻은 가중치로 원문 세 위치의 Value를 더한다. 원문에서 어떤 정보를 얼마나 가져올지는 학습된 가중치와 현재 문맥에 따라 달라진다. **원문 세 토큰과 디코더 입력 두 토큰**이라면 헤드 하나의 점수 행렬은 **2 × 3**이다. 행 하나가 디코더 한 위치, 열 하나가 원문 한 위치에 대응한다.

| 어텐션 | Query의 출처 | Key·Value의 출처 | 한 위치가 참조할 수 있는 범위 |
| --- | --- | --- | --- |
| 인코더의 Bidirectional Self-Attention | 인코더의 해당 층 입력 | 같은 입력 | 원문의 모든 유효 위치 |
| 디코더의 Causal Self-Attention | 디코더의 해당 층 입력 | 같은 입력 | 디코더 입력의 현재 위치까지 |
| 디코더의 Cross-Attention | 디코더의 Causal Self-Attention과 Add & Norm을 거친 표현 | 최종 인코더 출력 | 원문의 모든 유효 위치 |

그림 왼쪽 아래는 세 어텐션이 공유하는 **Scaled Dot-Product Attention** 계산이다. 헤드마다 Query와 Key의 내적을 Key 차원의 제곱근으로 나눠 점수 크기를 조절한다. 필요한 마스크를 적용한 뒤, 각 Query에 대해 Key 위치를 따라 Softmax를 계산하고 그 비율로 Value를 더한다. **Multi-Head Attention**은 이렇게 얻은 헤드별 출력을 이어 붙이고(**Concat**), 선형 변환(**Output Projection**)으로 모델 차원에 맞춘다.

## 4. 다음 토큰을 선택하고 다시 입력하기

디코더의 각 블록은 **Causal Self-Attention → Cross-Attention → FFN** 순서로 계산하고, 각 단계에 Add & Norm을 적용한다. 여섯 번째 블록을 거친 뒤 **Vocabulary Projection**이 각 위치의 벡터를 어휘집 크기의 로짓으로 바꾼다. 여기서의 **Softmax**는 다음 토큰 후보에 확률을 배분한다. 앞서 어텐션 내부에서 Softmax를 적용한 축은 참조할 **위치**였고, 여기서 적용하는 축은 출력할 **어휘**다.

추론은 `<BOS>`로 시작한다. 첫 단계에서 `I`를 선택하면 다음 입력은 `<BOS> / I`다. 이때 마지막 위치의 분포에서 `drink`를 고르면 입력이 `<BOS> / I / drink`로 늘어난다. 이것이 그림 오른쪽의 되돌아가는 화살표다. 번역하는 동안 같은 원문의 인코더 출력은 재사용한다. 종료 토큰 `<EOS>`를 선택하면 생성을 마친다.

**원 논문**의 Figure 1은 블록 사이의 연결을, §3.2는 세 어텐션에서 Query, Key, Value가 어디에서 오는지를 보여 준다. [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

[이전 글: Transformer 블록과 인코더-디코더 구조](18-Transformer-블록과-인코더-디코더.md) | [학습 목차](README.md) | [다음 글: BERT의 문맥 표현과 사전학습](19-BERT의-문맥-표현과-사전학습.md)
