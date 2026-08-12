# 🎯 코디세이 2주차 과제: 파이썬 기반 CLI 퀴즈 애플리케이션 개발 보고서

본 과제는 파이썬(Python)의 핵심 제어문, 함수, 예외 처리 및 JSON 기반 파일 입출력(File I/O)을 활용하여 대화형 CLI(Command Line Interface) 퀴즈 애플리케이션을 구축하는 것을 목표로 합니다. 데이터 영속성(Persistence)을 확보하고 상태 관리를 체계화한 개발 및 실습 보고서입니다.

- **교육 과정**: 코디세이 AI All in One 2기
- **작성자**: 박채우
- **GitHub 계정**: chaewoo25
- **저장소 주소**: https://github.com/chaewoo25/second

---

## 📌 1. 과제 개요 (Overview)

| 항목 | 상세 내용 |
| :--- | :--- |
| **과제명** | CLI 기반 나만의 퀴즈 애플리케이션 구축 |
| **주요 목적** | - Python 구조적 프로그래밍 및 함수 기반 모듈화 구현<br>- JSON 포맷 활용 데이터 영속성 및 사용자 통계 관리<br>- 예외 처리를 통한 사용자 입력 검증 및 안정성 확보 |
| **핵심 스택** | Python 3.x, JSON File System, Git / GitHub |

---

## 💻 2. 개발 및 실습 환경 (Environment)

| 구분 | 환경 명세 |
| :--- | :--- |
| **Host OS** | Windows 11 Home |
| **Language** | Python 3.12+ |
| **IDE / Editor** | Visual Studio Code |
| **CLI Terminal** | PowerShell / Windows Terminal |
| **Version Control** | Git / GitHub |
| **Data Format** | JSON (JavaScript Object Notation) |

---

## ⚙️ 3. 핵심 기능 및 로직 구조

### 3.1 프로그램 구조 및 흐름
```text
[quiz_app.py 실행]
       │
       ▼
[state.json 데이터 로드] ──(파일 미존재 시)──► [기본 구조 초기화]
       │
       ▼
[메인 메뉴 출력 (반복문)]
 ├── 1. 퀴즈 풀기 (채점, 해설 출력, 누적 통계 업데이트)
 ├── 2. 퀴즈 추가 (지문, 4지선다 보기, 정답, 해설 입력받아 저장)
 ├── 3. 퀴즈 삭제 (목록 선택 삭제 및 JSON 파일 동기화)
 ├── 4. 퀴즈 목록 보기 (전체 문제 및 정답 번호 조회)
 └── 5. 종료 (최종 데이터 저장 후 안전하게 종료)
 {
    "quizzes": [
        {
            "question": "문제 지문",
            "options": ["보기1", "보기2", "보기3", "보기4"],
            "answer": 1,
            "explanation": "문제 해설"
        }
    ],
    "user_stats": {
        "total_solved": 0,
        "correct_count": 0
    }
}