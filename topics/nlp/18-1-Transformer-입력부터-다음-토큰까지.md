# Day 4. Transformer 입력부터 다음 토큰까지

`나는 커피를 마신다`를 `I drink coffee`로 번역한다고 하자. 그림 왼쪽의 인코더는 원문을 한 번 읽는다. 오른쪽의 디코더는 `I`까지 썼을 때 원문의 어느 위치를 얼마나 참조할지 계산한 뒤, 다음 토큰을 고른다.

![Transformer 인코더-디코더 구조도. 원문과 번역의 두 경로가 Cross-Attention에서 만나고, 선택한 토큰이 디코더 입력으로 돌아간다.](assets/Transformer-Encoder-Decoder.png)

[구조도 확대 보기 (SVG)](assets/Transformer-Encoder-Decoder.svg)

## 1. 원문을 토큰별 입력 벡터로 바꾼다

`나는 커피를 마신다` → `[나는, 커피를, 마신다]` → 토큰 ID 세 개 → 위치 정보가 담긴 벡터 세 개

<details>
<summary>Tokenizer, Token Embedding, Positional Encoding이 각각 하는 일</summary>

<strong>토큰화(Tokenization).</strong> 토크나이저(Tokenizer)가 문장을 토큰으로 나눈다. 여기서는 계산을 따라가기 쉽게 원문을 세 토큰으로 나눴다고 가정한다. 실제 분할 단위는 토크나이저의 어휘집과 분할 규칙에 따라 달라진다.

<strong>토큰 임베딩(Token Embedding).</strong> 각 토큰에는 어휘집의 정수 번호인 Token ID가 있다. 그림의 Source Token IDs가 이 번호들이다. 임베딩 층은 각 ID를 행 번호로 사용해 학습 가능한 표에서 벡터 하나를 꺼낸다. 벡터의 길이가 모델 차원 `d_model`이다.

<strong>위치 인코딩(Positional Encoding).</strong> 같은 토큰 ID는 어디에 놓여도 같은 임베딩을 가져온다. 원래 Transformer는 임베딩에 `√d_model`을 곱하고, 그 위치에 해당하는 벡터를 더한다. 그림의 ⊕가 이 덧셈이다.

위치 벡터는 임베딩과 차원이 같다. 원 논문에서는 서로 다른 주파수의 사인과 코사인으로 이 벡터를 만든다. 덕분에 같은 토큰이 첫 번째와 세 번째에 놓여도 인코더에 들어가는 벡터는 달라진다.

</details>

## 2. 인코더가 원문의 앞뒤 문맥을 모은다

`마신다` 위치는 `나는`, `커피를`, `마신다` 세 위치를 모두 참조할 수 있다. 이때 각 위치의 정보를 얼마나 가져올지 계산하는 연산이 인코더의 <strong>Multi-Head Self-Attention</strong>이다.

<details>
<summary>Query, Key, Value에서 어텐션 헤드의 출력까지</summary>

<strong>Query, Key, Value를 만든다.</strong> 한 헤드(Attention Head) 안에서 같은 층 입력에 서로 다른 세 선형 변환을 적용한다. 그 결과가 Query(`Q`), Key(`K`), Value(`V`)다. 세 벡터 모두 같은 입력 시퀀스에서 만들기 때문에 Self-Attention이라고 부른다.

`마신다`의 Query는 세 위치의 Key와 하나씩 내적해 점수 세 개를 얻는다. Key는 점수를 계산할 때 쓰고, Value는 실제로 모아 올 정보를 담는다. 원문의 앞뒤 유효 위치가 모두 참조 범위에 들어가므로 이 그림에는 Bidirectional Self-Attention이라고 표시했다.

<strong>점수를 가중치로 바꾼다.</strong> 그림 왼쪽 아래의 Scaled Dot-Product Attention은 헤드 하나에서 다음 순서로 계산한다.

1. `QKᵀ`로 각 Query와 각 Key 사이의 내적을 구한다. 원문 세 위치끼리 비교하면 점수 행렬은 3행 3열이다.
2. 점수를 헤드의 Key 차원 `d_k`의 제곱근으로 나눈다. 차원이 커질 때 내적의 크기가 지나치게 커지는 것을 줄인다.
3. 가릴 위치가 있으면 해당 점수를 마스킹한 뒤, 각 행의 Key 위치를 따라 Softmax를 적용한다. 한 Query에 배정된 가중치의 합은 1이다.
4. 각 가중치를 해당 위치의 Value에 곱해 더한다. 이 가중합이 그 헤드에서 얻은 한 위치의 출력이다.

<strong>여러 헤드를 합친다.</strong> 헤드마다 투영 가중치가 달라서 같은 문장에서도 서로 다른 가중치를 계산할 수 있다. Multi-Head Attention은 헤드별 출력을 특성 축으로 이어 붙이고(Concat), 선형 변환(Output Projection)을 거쳐 모델 차원으로 돌려놓는다.

</details>

## 3. 인코더 블록을 쌓아 위치별 원문 표현을 만든다

Self-Attention이 위치 사이에서 정보를 모으면, <strong>Position-wise Feed-Forward Network(FFN)</strong>가 각 위치의 벡터를 변환한다. 여섯 번째 블록을 지나도 원문 세 위치에 벡터가 하나씩 남는다.

<details>
<summary>FFN, Add &amp; Norm, × 6을 그림 순서로 읽기</summary>

인코더 블록 하나의 계산 순서는 다음과 같다.

1. Multi-Head Self-Attention
2. Add &amp; Norm
3. Position-wise Feed-Forward Network
4. Add &amp; Norm

<strong>Add &amp; Norm.</strong> 그림에서 연산을 우회하는 화살표는 잔차 연결(Residual Connection)이다. 블록 안의 하위 층(Sublayer)이 입력 `x`로 출력 `F(x)`를 만들면, 두 벡터를 더해 `x + F(x)`를 만든다. 이어서 Layer Normalization(LayerNorm)이 각 위치의 특성 축을 따라 정규화한다. 이 순서를 Post-Layer Normalization(Post-LN)이라고 한다. 원 논문은 학습 시 하위 층 출력에 Dropout을 적용한 뒤 잔차를 더한다.

<strong>FFN.</strong> 첫 선형 층이 벡터의 차원을 늘리고, ReLU 활성화 함수를 거친 다음, 두 번째 선형 층이 모델 차원으로 되돌린다. 같은 블록 안에서는 세 위치에 같은 가중치를 적용한다. 이 단계에서는 각 위치의 벡터를 독립적으로 계산한다.

<strong>Encoder Output.</strong> 그림의 `× 6`은 원래 Transformer가 구조가 같은 블록 여섯 개를 서로 다른 가중치로 쌓았다는 뜻이다. 한 블록의 출력은 다음 블록의 입력이 된다. 마지막 출력은 `원문 토큰 수 × 모델 차원`, 이 예에서는 `3 × d_model`이다. 디코더의 각 블록이 이 출력을 참조한다.

</details>

## 4. 학습할 때는 정답 번역을 한 칸 옮긴다

디코더가 `I`를 입력받은 위치에서 맞혀야 할 정답은 `drink`다. 정답 토큰열을 오른쪽으로 한 칸 옮기는 <strong>Shift Right</strong>가 이 입력과 정답의 짝을 만든다.

<details>
<summary>디코더 입력과 예측할 정답을 위치별로 맞춰 보기</summary>

| 위치 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| 디코더 입력 | `<BOS>` | `I` | `drink` | `coffee` |
| 예측할 정답 | `I` | `drink` | `coffee` | `<EOS>` |

`<BOS>`는 시작 토큰(Beginning of Sequence), `<EOS>`는 종료 토큰(End of Sequence)이다. 정답 토큰열 끝에 `<EOS>`를 붙인다. 디코더 입력을 만들 때는 마지막 `<EOS>`를 빼고 맨 앞에 `<BOS>`를 넣어 두 줄의 길이를 맞춘다.

그림 위쪽의 Target Token IDs는 정답 번역의 토큰 번호이고, Decoder Input IDs는 한 칸 옮긴 뒤의 번호다. 디코더도 이 ID를 Token Embedding으로 바꾸고 Positional Encoding을 더한다.

학습에서는 앞 위치의 실제 정답 토큰을 다음 위치의 입력으로 제공한다. 이를 Teacher Forcing이라고 한다. 정답 전체가 한 배치에 들어 있으므로, 디코더가 미래 위치를 보지 못하게 하는 연산도 필요하다.

</details>

## 5. 디코더가 현재 위치까지의 번역을 읽는다

디코더 블록의 첫 연산은 <strong>Masked Multi-Head Self-Attention</strong>이다. 표의 두 번째 위치에서는 `<BOS>`와 `I`만 참조해 `drink`를 예측한다.

<details>
<summary>Causal Mask가 가리는 위치와 학습을 병렬로 계산할 수 있는 이유</summary>

Query, Key, Value는 모두 해당 디코더 층의 입력에서 만든다. 인코더와 달리 각 Query에는 현재 위치와 그보다 앞선 Key만 보인다. 이렇게 참조 범위를 제한하는 방식을 Causal Self-Attention이라고 한다.

Causal Mask는 Softmax를 적용하기 전에 미래 위치의 점수를 음의 무한대로 처리한다. 두 번째 위치에서 보면 세 번째 입력 `drink`와 네 번째 입력 `coffee`의 어텐션 가중치가 0이 된다.

각 행이 참조할 수 있는 범위는 마스크로 이미 정해져 있다. 그래서 학습할 때는 네 위치의 예측을 한 번의 순전파에서 계산한다. 길이가 다른 문장을 한 배치로 묶을 때 채워 넣은 패딩 위치는 별도의 Padding Mask로 참조 대상에서 제외할 수 있다.

이 연산 뒤에도 Add &amp; Norm이 온다. 그 출력이 다음 Cross-Attention의 Query를 만드는 입력이다.

</details>

## 6. Cross-Attention에서 원문과 번역이 만난다

<strong>Multi-Head Cross-Attention(Encoder-Decoder Attention)</strong>에서 Query는 디코더 쪽에서 오고, Key와 Value는 인코더 쪽에서 온다. 디코더는 이 연산에서 현재 번역 위치에 필요한 원문 정보를 가져온다.

<details>
<summary>디코더의 I가 원문 세 위치를 참조하는 과정</summary>

`<BOS> / I`까지 입력한 시점을 보자. 디코더의 두 위치는 각각 직전 Add &amp; Norm의 출력으로 Query를 만든다. 각 헤드는 최종 Encoder Output에 별도의 선형 변환을 적용해 원문 세 위치의 Key와 Value를 만든다.

헤드 하나의 점수 행렬은 <strong>2행 3열</strong>이다. 행은 디코더의 두 위치, 열은 원문의 세 위치에 대응한다. 두 번째 행에는 `I`의 Query를 `나는`, `커피를`, `마신다` 각 위치의 Key와 비교한 점수가 들어간다.

두 번째 행에 Softmax를 적용하면 원문 세 위치에 대한 가중치가 나온다. 예를 들어 한 헤드의 가중치가 `[0.1, 0.2, 0.7]`이라면, 이 헤드의 출력은 `0.1 × V(나는) + 0.2 × V(커피를) + 0.7 × V(마신다)`다. 실제 가중치는 학습한 매개변수와 입력 문맥에 따라 달라진다.

이제 디코더는 원문 정보를 반영한 결과에 Add &amp; Norm을 적용하고, 위치별 FFN과 마지막 Add &amp; Norm을 거친다. 디코더도 이런 블록을 여섯 개 쌓는다. 각 블록은 같은 최종 Encoder Output에서 자기 가중치로 Key와 Value를 만든다.

| 어텐션 | Query를 만드는 입력 | Key와 Value를 만드는 입력 | 한 Query가 참조하는 범위 |
| --- | --- | --- | --- |
| 인코더 Self-Attention | 해당 인코더 층 입력 | 같은 입력 | 원문의 모든 유효 위치 |
| 디코더 Causal Self-Attention | 해당 디코더 층 입력 | 같은 입력 | 현재까지의 번역 위치 |
| 디코더 Cross-Attention | 디코더의 첫 Add &amp; Norm 출력 | 최종 Encoder Output | 원문의 모든 유효 위치 |

</details>

## 7. 다음 토큰을 고르고 디코더 입력에 붙인다

마지막 디코더 블록은 위치마다 벡터 하나를 내놓는다. <strong>Vocabulary Projection</strong>이 이 벡터를 어휘별 점수로 바꾸면, 추론에서는 마지막 위치의 점수를 사용해 다음 토큰을 고른다.

<details>
<summary>Logits와 Softmax부터 종료 토큰까지 따라가기</summary>

<strong>어휘별 점수와 확률.</strong> Vocabulary Projection은 모델 차원의 벡터를 목표 어휘집 크기로 선형 변환한다. 결과 벡터의 각 성분은 후보 토큰 하나의 로짓(Logit), 즉 확률로 바꾸기 전의 점수다. 여기에 Softmax를 적용하면 다음 토큰의 확률 분포를 얻는다.

어텐션 안에서 Softmax를 적용한 축은 참조할 <strong>위치</strong>였다. 여기서는 출력할 <strong>어휘</strong>를 따라 확률의 합이 1이 된다. 학습에서는 각 위치의 예측을 4단계 표의 정답과 비교해 손실을 계산한다.

<strong>토큰 선택(Token Selection).</strong> 추론에서는 시작 토큰만 주어진다. 예를 들어 Greedy Decoding을 사용하면 매 단계에서 확률이 가장 높은 토큰 하나를 고른다. 아래 표는 그런 방식으로 번역이 완성되는 한 가지 예다.

| 생성 단계 | 지금까지의 디코더 입력 | 마지막 위치에서 고른 토큰 |
| --- | --- | --- |
| 1 | `<BOS>` | `I` |
| 2 | `<BOS> / I` | `drink` |
| 3 | `<BOS> / I / drink` | `coffee` |
| 4 | `<BOS> / I / drink / coffee` | `<EOS>` |

선택한 토큰을 다음 디코더 입력 끝에 붙이는 과정이 그림 오른쪽의 되돌아가는 화살표다. 이전에 생성한 토큰을 조건으로 다음 토큰을 생성하는 방식을 Autoregressive Decoding이라고 한다. 번역하는 동안 원문은 같으므로 인코더 출력은 재사용한다. `<EOS>`를 고르면 생성이 끝난다.

</details>

원 논문의 Figure 1과 §3에는 블록 구성과 어텐션 계산이 나온다. 디코더의 마지막 위치에서 토큰을 선택하는 구현은 Harvard NLP의 `greedy_decode`에서 볼 수 있다. [Attention Is All You Need](https://arxiv.org/abs/1706.03762) / [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/#greedy-decoding)

## 용어 정리

<details>
<summary>입력과 블록 구성</summary>

| 용어 | 뜻 |
| --- | --- |
| Tokenizer / Token ID | 토크나이저는 문장을 토큰으로 나눈다. 토큰 ID는 어휘집에서 각 토큰에 부여한 정수 번호다. |
| Token Embedding | 토큰 ID로 조회하는 학습 가능한 벡터. |
| Positional Encoding | 순서 정보를 담기 위해 토큰 임베딩에 더하는 위치 벡터. |
| Position-wise Feed-Forward Network (FFN) | 각 위치에 같은 가중치로 적용하는 신경망. 원래 구조는 선형 변환, ReLU, 선형 변환 순서다. |
| Residual Connection / Layer Normalization | 잔차 연결은 하위 층 입력을 그 출력에 더한다. LayerNorm은 각 위치에서 특성 축을 따라 값을 정규화한다. |
| Add &amp; Norm / Post-LN | 원래 Transformer에서 잔차 덧셈 후 LayerNorm을 적용하는 순서. |
| Encoder Output | 원문의 각 위치에 대응하는 최종 인코더 벡터들의 시퀀스. |

</details>

<details>
<summary>어텐션의 구성 요소와 참조 범위</summary>

| 용어 | 뜻 |
| --- | --- |
| Query (Q) | 현재 위치에서 다른 위치를 얼마나 참조할지 계산할 때 Key와 비교하는 벡터. |
| Key (K) | 각 참조 위치에서 Query와의 점수를 계산하는 데 쓰는 벡터. |
| Value (V) | 각 참조 위치에서 해당 어텐션 가중치만큼 출력에 더하는 벡터. |
| Scaled Dot-Product Attention | Query와 Key의 내적을 스케일링하고, Softmax로 구한 가중치로 Value를 합치는 연산. |
| Multi-Head Attention / Concat / Output Projection | 여러 헤드에서 어텐션을 계산한 뒤, 출력을 이어 붙여 선형 변환하는 연산. |
| Bidirectional Self-Attention | 같은 시퀀스에서 현재 위치의 앞과 뒤를 모두 참조할 수 있는 Self-Attention. |
| Causal Self-Attention / Causal Mask | 현재와 이전 위치만 참조하는 Self-Attention과, 미래 위치를 가려 이를 구현하는 마스크. |
| Padding Mask | 길이를 맞추기 위해 채운 패딩 위치를 참조 대상에서 제외하는 마스크. |
| Cross-Attention / Encoder-Decoder Attention | 여기서는 디코더 표현에서 Query를, 최종 인코더 출력에서 Key와 Value를 만드는 어텐션. |

</details>

<details>
<summary>학습과 토큰 생성</summary>

| 용어 | 뜻 |
| --- | --- |
| Shift Right | 정답 토큰열을 오른쪽으로 한 칸 옮기고 첫 칸에 시작 토큰을 넣어 학습용 디코더 입력을 만드는 연산. |
| Teacher Forcing | 학습할 때 실제 정답의 이전 토큰들을 디코더 입력으로 제공하는 방법. |
| Vocabulary Projection / Logits | 마지막 디코더 벡터를 어휘별 점수로 바꾸는 선형 변환과, 그 결과로 얻는 점수들. |
| Softmax | 점수를 합이 1인 분포로 바꾸는 함수. 출력 층에서는 각 후보 토큰의 확률을 얻는다. |
| Token Selection / Greedy Decoding | 다음 토큰을 고르는 절차. Greedy Decoding은 매 단계에서 가장 높은 점수의 토큰을 고른다. |
| Autoregressive Decoding | 이전에 생성한 토큰들을 조건으로 다음 토큰을 하나씩 생성하는 방식. |
| `<BOS>` / `<EOS>` | 디코더의 생성 시작과 종료를 나타내는 특수 토큰. |

</details>

[이전 글: Transformer 블록과 인코더-디코더 구조](18-Transformer-블록과-인코더-디코더.md) | [학습 목차](README.md) | [다음 글: BERT의 문맥 표현과 사전학습](19-BERT의-문맥-표현과-사전학습.md)
