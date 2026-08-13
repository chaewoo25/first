# 🤖 Mini NPU Simulator: 패턴 매칭 & MAC 연산 시뮬레이터

> **코디세이 AI All-in-One 2기 3주차 과제**  
> **작성자**: 박채우  
> **GitHub Repository**: [chaewoo25/third](https://github.com/chaewoo25/third)

---

## 1. 프로젝트 개요 (Overview)

본 프로젝트는 외부 AI/선형대수 라이브러리(`NumPy`, `PyTorch` 등)를 일체 사용하지 않고, **순수 파이썬(Pure Python)** 기본 자료구조 및 제어문만으로 인공지능 NPU(Neural Processing Unit)의 핵심 연산인 **MAC (Multiply-Accumulate, 곱셈-누적)** 알고리즘을 직접 구현하고 성능을 프로파일링하는 시뮬레이터입니다.

### 🎯 핵심 과제 목표
1. **NPU 핵심 연산 직접 구현**: 2차원 리스트와 이중 반복문을 활용하여 $N \times N$ 크기의 패턴과 필터 간 MAC 연산 작성.
2. **라벨 정규화 (Normalization)**: 다양한 문자열 입력 형태(`cross`, `v`, `X`, `x` 등)를 내부 표준 라벨(`Cross`, `X`)로 통일.
3. **부동소수점 오차 대응**: 허용 오차 ($\epsilon = 10^{-6}$) 기반 비교 알고리즘을 통해 동점(`UNDECIDED`) 판정 처리.
4. **알고리즘 복잡도 측정**: 크기별($3 \times 3, 5 \times 5, 13 \times 13, 25 \times 25$) 연산 시간(ms) 및 연산 횟수($N^2$) 프로파일링 및 정량 분석.

---

## 2. 파일 구조 (Project Structure)

```text
ia-codyssey/
└── 3주차/
    ├── main.py        # 시뮬레이터 메인 실행 파일 (모드 1, 모드 2 구현)
    ├── data.json      # 크기별 필터 및 테스트 패턴 데이터셋
    └── README.md      # 과제 수행 및 결과 리포트 (본 문서)

```
🤖 Mini NPU Simulator (패턴 매칭 & MAC)
==========================================
1. 사용자 입력 (3x3)
2. data.json 분석 및 프로파일링
3. 종료
선택 (1~3): 2

   [모드 2] data.json 패턴 분석 및 프로파일링
==========================================

# [1] 패턴 분석 (라벨 정규화 및 테스트)
  -- size_5_1 -- | Cross: 9.0000 | X: 1.0000 | 판정: Cross | expected: Cross | PASS
  -- size_5_2 -- | Cross: 1.0000 | X: 9.0000 | 판정: X | expected: X | PASS
  -- size_13_1 -- | Cross: 11.2500 | X: 11.2500 | 판정: UNDECIDED | expected: X | FAIL

# [2] 크기별 성능 분석 (평균 10회 연산)
------------------------------------------
 크기      평균 시간(ms)     연산 횟수(N^2)
------------------------------------------
  3x3         0.0023 ms           9
  5x5         0.0039 ms          25
 13x13        0.0210 ms         169
 25x25        0.0524 ms         625
------------------------------------------

# [3] 결과 요약
  총 테스트 : 3개
  성공(PASS) : 2개
  실패(FAIL) : 1개

  [실패 케이스 상세 목록]
   - size_13_1: 판정(UNDECIDED) != expected(X) [동점 또는 오판]
   ```