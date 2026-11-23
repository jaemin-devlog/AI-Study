# Day 6. NLP 기초부터 LLM까지

> 텍스트를 수치로 표현하는 방법에서 시작해, 순서와 문맥을 처리하는 모델이 어떤 정보를 학습하는지 정리한다. 고객 문의 한 문장에 분류, 검색, 생성이 각각 어떤 결과를 내는지도 비교한다.

## 1. 토큰 ID에서 문서와 단어의 벡터로

<strong>토큰화(Tokenization)</strong>는 텍스트를 문자, 단어, 서브워드 등의 단위로 나눈다. 토큰 ID는 어휘집 안에서 토큰을 구별하는 번호다. 원핫 인코딩(One-Hot Encoding)은 해당 ID의 성분만 1인 벡터를 만든다. 서브워드 토큰화는 드문 단어를 어휘집에 있는 작은 조각으로 나눠 처리한다. [텍스트 전처리와 토큰화](02-텍스트-전처리와-토큰화.md) / [서브워드 토큰화](09-서브워드-토큰화와-가변-길이-입력.md)

| 방법 | 사용하는 정보 | 결과 |
| --- | --- | --- |
| Bag of Words (BoW) | 문서 안의 단어별 출현 횟수 | 단어 빈도를 담은 문서 벡터 |
| TF-IDF | 문서 내 빈도와 문서 집합에서의 희소성 | 단어별 가중치를 담은 문서 벡터 |
| N-gram 언어모델 | 앞선 짧은 토큰 조합의 출현 빈도 | 주어진 문맥의 다음 토큰 확률 |
| Word2Vec | 중심 단어와 주변 단어가 함께 등장하는 패턴 | 학습된 단어 벡터 |

기본 BoW와 TF-IDF는 단어 순서를 생략하므로 같은 단어 구성을 가진 문장에서 관계의 차이를 나타내기 어렵다. N-gram 언어모델은 토큰 순서를 쓰지만, 학습 데이터에 드물게 등장하는 조합의 확률은 추정하기 어렵다. [BoW와 TF-IDF](03-BoW와-TF-IDF-텍스트-분류.md) / [N-gram 언어모델](04-언어모델과-N-gram.md)

Word2Vec의 <strong>CBOW(Continuous Bag of Words)</strong>는 주변 단어로 중심 단어를 예측한다. <strong>Skip-gram</strong>은 중심 단어로 주변 단어를 예측한다. 두 방식 모두 예측 과정에서 임베딩 벡터를 갱신한다. 학습 뒤에는 임베딩 조회(Embedding Lookup)로 단어 벡터를 꺼내 코사인 유사도로 방향을 비교할 수 있다. [Word2Vec의 학습 원리](07-Word2Vec의-학습-원리.md)

Word2Vec은 같은 토큰에 고정 벡터를 사용한다. ‘배’가 과일인지 선박인지는 주변 문장에 따라 달라지므로, 문장 속 각 위치의 의미를 다루려면 문맥에 따라 바뀌는 표현이 필요하다. [단어 임베딩과 벡터 유사도](08-단어-임베딩과-벡터-유사도.md)

## 2. 단어를 읽은 순서와 상태를 다음 단계에 전달하기

<strong>순환 신경망(Recurrent Neural Network, RNN)</strong>은 현재 입력과 이전 은닉 상태로 새 은닉 상태를 만든다. 이전 계산이 끝나야 다음 시점을 진행할 수 있다. 시간 역전파(Backpropagation Through Time, BPTT)에서는 여러 시점에 걸쳐 기울기가 소실되거나 폭발할 수 있다. [RNN 언어모델의 학습](12-RNN-언어모델의-학습.md)

<strong>LSTM(Long Short-Term Memory)</strong>은 셀 상태(Cell State)에 정보를 두고 입력, 망각, 출력 게이트로 저장과 전달을 조절한다. <strong>GRU(Gated Recurrent Unit)</strong>는 별도의 셀 상태 없이 갱신 게이트와 리셋 게이트로 은닉 상태를 조절한다. 두 모델은 이전 상태를 다음 시점에 전달하면서, 오래 필요한 정보를 유지할 경로를 제공한다. [LSTM과 GRU의 작동 원리](13-LSTM과-GRU의-작동-원리.md)

초기 <strong>Seq2Seq(Sequence-to-Sequence)</strong>에서는 인코더의 최종 상태가 입력 문장의 정보를 디코더에 전달했다. 긴 원문을 고정 크기 상태에 모으면 세부 정보가 손실될 수 있다. 어텐션을 추가하면 디코더가 출력 위치마다 인코더의 각 위치에 점수를 매기고, Softmax 가중치로 입력 위치의 표현을 합칠 수 있다. [Seq2Seq의 인코더와 디코더](14-Seq2Seq의-인코더와-디코더.md) / [어텐션의 작동 원리](14-1-어텐션의-작동-원리.md)

## 3. Transformer에서 토큰 간 관계를 직접 계산하기

<strong>Self-Attention</strong>에서는 같은 입력 시퀀스에서 Query, Key, Value를 만든다. Query와 Key의 내적을 Key 차원의 제곱근으로 나눠 점수를 구한다. 필요한 마스크를 적용하고 Key 위치를 따라 Softmax를 계산한 뒤, 그 가중치로 Value를 합한다. Multi-Head Attention은 이 계산을 여러 헤드에서 수행해 결과를 결합한다. [Self-Attention과 QKV 생성](15-Self-Attention과-QKV-생성.md) / [스케일 내적 어텐션과 마스크](16-스케일-내적-어텐션과-마스크.md)

Transformer는 위치 정보를 반영한 입력을 사용한다. 어텐션이 토큰 사이에서 문맥을 모으면, 위치별 FFN이 각 토큰의 벡터를 변환한다. 잔차 연결과 층 정규화가 하위 층을 연결한다. 한 층의 모든 입력 위치가 주어졌을 때, RNN의 시점 간 상태 전달 없이 위치별 연산을 병렬로 계산할 수 있다. [멀티헤드 어텐션과 위치 정보](17-멀티헤드-어텐션과-위치-정보.md)

| Transformer 구조 | 문맥을 읽는 방식 | 대표적인 활용 |
| --- | --- | --- |
| Encoder-only | Bidirectional Self-Attention으로 입력의 앞뒤 유효 위치를 참조 | 토큰과 문장의 문맥 표현 |
| Decoder-only | Causal Self-Attention으로 현재와 이전 유효 위치를 참조 | 다음 토큰 예측과 생성 |
| Encoder-Decoder | 인코더가 소스를 처리하고, 디코더가 Causal Self-Attention과 Cross-Attention을 사용 | 번역과 같은 입력-출력 시퀀스 변환 |

## 4. BERT와 GPT의 사전학습 목표 비교하기

<strong>BERT(Bidirectional Encoder Representations from Transformers)</strong>의 대표 목표인 마스크 언어 모델링(Masked Language Modeling, MLM)은 선택한 입력 위치의 원래 토큰을 예측한다. ‘나는 `[MASK]` 마신다’에서 가운데 위치는 ‘나는’과 ‘마신다’를 모두 참조한다. 사전학습한 표현을 분류에 활용할 때는 `[CLS]` 위치의 벡터에서 분류 헤드가 클래스별 점수를 만든다. 원래 BERT는 다음 문장 예측(Next Sentence Prediction, NSP)도 함께 사용했다. [BERT의 문맥 표현과 사전학습](19-BERT의-문맥-표현과-사전학습.md) / [BERT 원 논문](https://arxiv.org/abs/1810.04805)

<strong>GPT(Generative Pre-trained Transformer)</strong>는 ‘나는 물을’까지 읽고 그 다음 토큰인 ‘마신다’를 예측하도록 학습한다. 학습에서는 원문의 다음 토큰을 정답으로 사용해 교차 엔트로피 손실을 계산한다. 생성에서는 모델이 고른 토큰을 다음 입력에 넣고 예측을 반복한다. 어떤 후보를 고를지는 Greedy Decoding이나 Sampling 같은 디코딩 규칙이 결정한다. [GPT의 구조와 다음 토큰 예측 학습](23-GPT의-구조와-다음-토큰-예측-학습.md) / [GPT의 텍스트 생성 원리와 생성 제어](24-GPT의-텍스트-생성-원리와-생성-제어.md)

## 5. ‘배송이 늦어요’를 세 가지 과제로 처리하기

| 과제 | 처리 방법 | 출력 예시 |
| --- | --- | --- |
| 문의 유형 분류 | TF-IDF 벡터와 분류 모델, 또는 BERT와 분류 헤드 | ‘배송 지연’이라는 클래스 |
| 유사 FAQ 검색 | 문의와 FAQ를 Sentence-BERT로 임베딩한 뒤 코사인 유사도로 순위 계산 | ‘배송이 지연되면 어떻게 해야 하나요?’라는 기존 문서 |
| 고객 응답 생성 | GPT 계열 모델이 문의와 제공된 문맥을 바탕으로 다음 토큰을 반복 생성 | ‘배송이 지연되어 불편을 드렸습니다. 주문 정보를 확인해 배송 상태를 안내해 드리겠습니다.’라는 새 응답 |

세 과제는 한 서비스에서도 연결할 수 있다. 분류 모델이 문의 유형을 고르면, 검색 단계가 관련 FAQ를 찾고, 생성 모델이 검색 결과를 응답에 반영한다. 실제 주문의 배송 상태를 안내하려면 해당 주문의 조회 데이터도 필요하다. [BERT 텍스트 분류와 미세조정](20-BERT-텍스트-분류와-미세조정.md) / [문장 임베딩과 의미 기반 검색](21-문장-임베딩과-의미-기반-검색.md)

모델을 고를 때는 먼저 필요한 출력이 클래스인지, 기존 문서인지, 새 텍스트인지 정한다. 같은 과제를 해결하는 후보끼리는 평가 성능과 함께 라벨 데이터의 양, 지연 시간, GPU 메모리, 운영 비용을 비교한다.

## 6. 사전학습한 LLM을 서비스에 연결하기

- <strong>지도 미세조정(Supervised Fine-Tuning, SFT)</strong>은 입력과 목표 응답 쌍으로 사전학습한 모델을 추가 학습한다.
- <strong>인간 피드백 기반 강화학습(Reinforcement Learning from Human Feedback, RLHF)</strong>은 사람의 평가를 보상 신호로 사용해 응답 정책을 조정한다. <strong>직접 선호 최적화(Direct Preference Optimization, DPO)</strong>는 선호 응답과 비선호 응답의 쌍으로 모델을 직접 최적화한다.
- <strong>저랭크 적응(Low-Rank Adaptation, LoRA)</strong>은 기존 가중치를 고정한 상태에서 저랭크로 표현한 가중치 변화분을 학습한다. <strong>양자화(Quantization)</strong>는 값을 더 낮은 정밀도로 표현하고, <strong>지식 증류(Knowledge Distillation)</strong>는 교사 모델의 출력을 이용해 학생 모델을 학습한다.
- <strong>검색 증강 생성(Retrieval-Augmented Generation, RAG)</strong>은 검색한 외부 자료를 생성에 사용할 문맥으로 전달한다. <strong>에이전트(Agent)</strong>는 목적에 맞는 도구 호출과 결과 확인을 반복할 수 있도록 구성한 시스템이다.

## 용어 정리

| 용어 | 뜻 |
| --- | --- |
| 정적 임베딩(Static Embedding) | 같은 토큰에 동일한 벡터를 조회하는 표현 |
| 문맥 기반 표현(Contextual Representation) | 주변 입력을 반영해 위치별로 계산한 토큰 벡터 |
| Seq2Seq | 입력 시퀀스를 처리해 출력 시퀀스를 만드는 모델 구조 |
| Self-Attention / Cross-Attention | 같은 시퀀스에서 Q, K, V를 만드는 어텐션과, 한 시퀀스의 Query로 다른 시퀀스의 Key와 Value를 참조하는 어텐션 |
| MLM / Next Token Prediction | 선택된 위치의 원래 토큰 예측과, 현재 문맥 바로 다음 토큰 예측 |
| 문장 임베딩(Sentence Embedding) | 문장 전체를 유사도 비교에 쓸 고정 차원 벡터로 나타낸 표현 |
| LLM(Large Language Model) | 대규모 텍스트와 많은 파라미터를 사용해 학습한 언어모델 |
| 사전학습(Pretraining) / 미세조정(Fine-Tuning) | 범용 표현이나 예측 능력을 먼저 학습하는 과정과, 그 가중치를 특정 목표에 맞게 추가 학습하는 과정 |

[이전 글: GPT의 텍스트 생성 원리와 생성 제어](24-GPT의-텍스트-생성-원리와-생성-제어.md) | [학습 목차로 이동](README.md)
