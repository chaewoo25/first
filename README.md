# 🎯 코디세이 2주차 과제: 오버워치 CLI 퀴즈 애플리케이션 개발 보고서

본 과제는 파이썬(Python)과 JSON 데이터 구조를 활용하여 제작한 대화형 CLI(Command Line Interface) 퀴즈 프로그램입니다. 오버워치(Overwatch) 게임 관련 퀴즈 수록 및 사용자 상태 관리를 포함합니다.

- **교육 과정**: 코디세이 AI All in One 2기
- **작성자**: 박채우
- **GitHub 계정**: chaewoo25
- **저장소 주소**: https://github.com/chaewoo25/second

---

## 📌 1. 과제 개요 (Overview)

| 항목 | 상세 내용 |
| :--- | :--- |
| **과제명** | CLI 기반 오버워치 퀴즈 애플리케이션 구축 |
| **주요 목적** | - Python 구조적 프로그래밍 및 함수 기반 모듈화 구현<br>- JSON 포맷 활용 데이터 영속성 및 사용자 통계 관리<br>- 대화형 CLI 메뉴 구현 및 입력 예외 처리 |
| **핵심 스택** | Python 3.x, JSON File System, Git / GitHub |

---

## 🎮 2. 수록 퀴즈 내용 및 예시 (Quiz Content)

본 앱에 실제 수록된 오버워치 관련 퀴즈 문제 및 해설 예시입니다.

### ❓ [문제 1] 지원 영웅 스킬
- **질문**: 쓰러진 아군 1명을 전장에 즉시 복귀시키는 '부활' 스킬을 가진 지원(힐러) 영웅은?
- **보기**:
  1. 루시우
  2. 메르시
  3. 아나
  4. 키리코
- **정답**: `2번 (메르시)`
- **해설**: 메르시는 쓰러진 아군을 즉시 부활시키는 능력을 가지고 있습니다.

### ❓ [문제 2] 오버워치 2 전장 모드
- **질문**: 오버워치 2에서 도입된 모드로, 로봇을 조종해 상대 진영으로 밀고 나가는 전장 모드는?
- **보기**:
  1. 밀기(Push)
  2. 점령(Control)
  3. 호위(Escort)
  4. 플래시포인트(Flashpoint)
- **정답**: `1번 (밀기)`
- **해설**: '밀기' 모드는 중앙의 로봇을 상대 진영 쪽으로 멀리 미는 팀이 승리합니다.

### ❓ [문제 3] 세계관 및 조직
- **질문**: 탈론(Talon)은 오버워치 세계관 속 어떤 조직인가요?
- **정답**: `대표적인 범죄 테러 조직`
- **해설**: 탈론(Talon)은 오버워치 세계관 속 대표적인 범죄 테러 조직입니다.

---

## ⚙️ 3. 핵심 기능 및 로직 구조

### 3.1 프로그램 구조 및 흐름
```text
[quiz_app.py 실행]
       │
       ▼
[state.json 데이터 로드] ──(파일 미존재 시)──► [기본 데이터 초기화]
       │
       ▼
[메인 메뉴 출력 (반복문)]
 ├── 1. 퀴즈 풀기 (오버워치 퀴즈 풀이, 채점, 해설 출력, 누적 통계 반영)
 ├── 2. 퀴즈 추가 (지문, 4지선다 보기, 정답, 해설 입력받아 저장)
 ├── 3. 퀴즈 삭제 (목록 선택 삭제 및 JSON 파일 동기화)
 ├── 4. 퀴즈 목록 보기 (전체 문제 지문, 보기 및 정답 조회)
 └── 5. 종료 (최종 데이터 저장 후 안전하게 종료)
import json
import os

DATA_FILE = "state.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        default_data = {
            "quizzes": [
                {
                    "question": "쓰러진 아군 1명을 전장에 즉시 복귀시키는 '부활' 스킬을 가진 지원(힐러) 영웅은?",
                    "options": ["루시우", "메르시", "아나", "키리코"],
                    "answer": 2,
                    "explanation": "메르시는 쓰러진 아군을 즉시 부활시키는 능력을 가지고 있습니다."
                },
                {
                    "question": "오버워치 2에서 도입된 모드로, 로봇을 조종해 상대 진영으로 밀고 나가는 전장 모드는?",
                    "options": ["밀기(Push)", "점령(Control)", "호위(Escort)", "플래시포인트(Flashpoint)"],
                    "answer": 1,
                    "explanation": "'밀기' 모드는 중앙의 로봇을 상대 진영 쪽으로 멀리 미는 팀이 승리합니다."
                },
                {
                    "question": "탈론(Talon)은 오버워치 세계관 속 어떤 조직인가요?",
                    "options": ["범죄 테러 조직", "평화 유지군", "우주 탐사대", "의료 봉사단"],
                    "answer": 1,
                    "explanation": "탈론은 오버워치 세계관 속 대표적인 범죄 테러 조직입니다."
                }
            ],
            "user_stats": {
                "total_solved": 0,
                "correct_count": 0
            }
        }
        save_data(default_data)
        return default_data
    
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def play_quiz(data):
    quizzes = data.get("quizzes", [])
    if not quizzes:
        print("\\n[!] 수록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해 주세요.")
        return

    print("\\n=== 🎮 오버워치 퀴즈 시작 ===")
    for idx, q in enumerate(quizzes, 1):
        print(f"\\n[Q{idx}] {q['question']}")
        for opt_idx, opt in enumerate(q['options'], 1):
            print(f"  {opt_idx}. {opt}")
        
        try:
            user_ans = int(input("정답 입력 (숫자): "))
            data["user_stats"]["total_solved"] += 1
            if user_ans == q['answer']:
                print("⭕ 정답입니다!")
                data["user_stats"]["correct_count"] += 1
            else:
                print(f"❌ 틀렸습니다. (정답: {q['answer']}번)")
            print(f"💡 해설: {q['explanation']}")
        except ValueError:
            print("❌ 잘못된 입력입니다. 숫자로 입력해 주세요.")
    
    save_data(data)
    print(f"\\n📊 현재 통계: {data['user_stats']['correct_count']} / {data['user_stats']['total_solved']} 문제 정답")

def add_quiz(data):
    print("\\n=== ➕ 새 퀴즈 추가 ===")
    question = input("퀴즈 질문: ")
    options = []
    for i in range(1, 5):
        opt = input(f"보기 {i}: ")
        options.append(opt)
    
    try:
        answer = int(input("정답 번호 (1~4): "))
        explanation = input("정답 해설: ")
        
        new_q = {
            "question": question,
            "options": options,
            "answer": answer,
            "explanation": explanation
        }
        data["quizzes"].append(new_q)
        save_data(data)
        print("✅ 퀴즈가 성공적으로 추가되었습니다!")
    except ValueError:
        print("❌ 정답 번호는 숫자로 입력해 주세요.")

def delete_quiz(data):
    quizzes = data.get("quizzes", [])
    if not quizzes:
        print("\\n[!] 삭제할 퀴즈가 없습니다.")
        return

    print("\\n=== 🗑️ 퀴즈 삭제 ===")
    for idx, q in enumerate(quizzes, 1):
        print(f"{idx}. {q['question']}")
    
    try:
        del_idx = int(input("삭제할 퀴즈 번호 입력: ")) - 1
        if 0 <= del_idx < len(quizzes):
            removed = quizzes.pop(del_idx)
            save_data(data)
            print(f"✅ '{removed['question']}' 퀴즈가 삭제되었습니다.")
        else:
            print("❌ 올바른 번호를 선택해 주세요.")
    except ValueError:
        print("❌ 숫자를 입력해 주세요.")

def view_quizzes(data):
    quizzes = data.get("quizzes", [])
    print("\\n=== 📋 퀴즈 전체 목록 ===")
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return

    for idx, q in enumerate(quizzes, 1):
        print(f"\\n{idx}. {q['question']}")
        for opt_idx, opt in enumerate(q['options'], 1):
            print(f"   {opt_idx}) {opt}")
        print(f"   정답: {q['answer']}번 | 해설: {q['explanation']}")

def main():
    data = load_data()
    while True:
        print("\\n=============================")
        print(" 오버워치 CLI 퀴즈 애플리케이션")
        print("=============================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 삭제")
        print("4. 퀴즈 목록 보기")
        print("5. 종료")
        
        choice = input("메뉴 선택 (1-5): ")
        if choice == "1":
            play_quiz(data)
        elif choice == "2":
            add_quiz(data)
        elif choice == "3":
            delete_quiz(data)
        elif choice == "4":
            view_quizzes(data)
        elif choice == "5":
            print("\\n프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
            break
        else:
            print("\\n❌ 올바른 번호를 선택해 주세요 (1~5).")

if __name__ == "__main__":
    main()
    {
    "quizzes": [
        {
            "question": "쓰러진 아군 1명을 전장에 즉시 복귀시키는 '부활' 스킬을 가진 지원(힐러) 영웅은?",
            "options": [
                "루시우",
                "메르시",
                "아나",
                "키리코"
            ],
            "answer": 2,
            "explanation": "메르시는 쓰러진 아군을 즉시 부활시키는 능력을 가지고 있습니다."
        },
        {
            "question": "오버워치 2에서 도입된 모드로, 로봇을 조종해 상대 진영으로 밀고 나가는 전장 모드는?",
            "options": [
                "밀기(Push)",
                "점령(Control)",
                "호위(Escort)",
                "플래시포인트(Flashpoint)"
            ],
            "answer": 1,
            "explanation": "'밀기' 모드는 중앙의 로봇을 상대 진영 쪽으로 밀어내는 팀이 승리합니다."
        },
        {
            "question": "탈론(Talon)은 오버워치 세계관 속 어떤 조직인가요?",
            "options": [
                "범죄 테러 조직",
                "평화 유지군",
                "우주 탐사대",
                "의료 봉사단"
            ],
            "answer": 1,
            "explanation": "탈론은 오버워치 세계관 속 대표적인 범죄 테러 조직입니다."
        }
    ],
    "user_stats": {
        "total_solved": 0,
        "correct_count": 0
    }
}