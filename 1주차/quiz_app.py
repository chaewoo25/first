import json
import os

FILE_NAME = 'state.json'

def load_data():
    """state.json 파일에서 데이터를 불러옵니다. 파일이 없으면 기본 구조를 반환합니다."""
    if not os.path.exists(FILE_NAME):
        return {"quizzes": [], "user_stats": {"total_solved": 0, "correct_count": 0}}
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {"quizzes": [], "user_stats": {"total_solved": 0, "correct_count": 0}}

def save_data(data):
    """데이터를 state.json 파일에 저장합니다."""
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def play_quiz(data):
    """1. 퀴즈 풀기 기능"""
    quizzes = data.get("quizzes", [])
    if not quizzes:
        print("\n[알림] 등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해주세요.")
        return

    print("\n=== 🎯 퀴즈 풀기 ===")
    score = 0
    for idx, q in enumerate(quizzes, 1):
        print(f"\n[문제 {idx}] {q['question']}")
        for opt_idx, option in enumerate(q['options'], 1):
            print(f"  {opt_idx}. {option}")
        
        while True:
            user_input = input("정답 번호를 입력하세요 (1~4): ").strip()
            if user_input.isdigit() and 1 <= int(user_input) <= len(q['options']):
                user_ans = int(user_input)
                break
            print("[오류] 1에서 4 사이의 정답 번호를 입력해주세요.")

        if user_ans == q['answer']:
            print("⭕ 정답입니다!")
            score += 1
        else:
            print(f"❌ 틀렸습니다. (정답: {q['answer']}번)")
        print(f"💡 해설: {q['explanation']}")

    data['user_stats']['total_solved'] += len(quizzes)
    data['user_stats']['correct_count'] += score
    print(f"\n[결과] 총 {len(quizzes)}문제 중 {score}문제를 맞혔습니다!")

def add_quiz(data):
    """2. 퀴즈 추가 기능"""
    print("\n=== ➕ 퀴즈 추가 ===")
    question = input("문제 지문을 입력하세요: ").strip()
    if not question:
        print("[오류] 지문은 빈 칸일 수 없습니다.")
        return

    options = []
    for i in range(1, 5):
        opt = input(f"보기 {i}을(를) 입력하세요: ").strip()
        options.append(opt)

    while True:
        ans_input = input("정답 번호를 입력하세요 (1~4): ").strip()
        if ans_input.isdigit() and 1 <= int(ans_input) <= 4:
            answer = int(ans_input)
            break
        print("[오류] 1에서 4 사이의 숫자를 입력해주세요.")

    explanation = input("해설을 입력하세요: ").strip()

    new_quiz = {
        "question": question,
        "options": options,
        "answer": answer,
        "explanation": explanation
    }
    data["quizzes"].append(new_quiz)
    save_data(data)
    print("\n[완료] 새로운 퀴즈가 성공적으로 추가되었습니다!")

def delete_quiz(data):
    """3. 퀴즈 삭제 기능"""
    quizzes = data.get("quizzes", [])
    if not quizzes:
        print("\n[알림] 삭제할 퀴즈가 없습니다.")
        return

    list_quizzes(data)
    while True:
        del_input = input("\n삭제할 퀴즈 번호를 입력하세요 (취소: 0): ").strip()
        if del_input.isdigit():
            del_num = int(del_input)
            if del_num == 0:
                print("삭제를 취소합니다.")
                return
            if 1 <= del_num <= len(quizzes):
                removed = quizzes.pop(del_num - 1)
                save_data(data)
                print(f"\n[완료] '{removed['question']}' 퀴즈가 삭제되었습니다.")
                return
        print("[오류] 올바른 퀴즈 번호를 입력해주세요.")

def list_quizzes(data):
    """4. 퀴즈 목록 보기 기능"""
    quizzes = data.get("quizzes", [])
    print("\n=== 📜 퀴즈 목록 ===")
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return

    for idx, q in enumerate(quizzes, 1):
        print(f"{idx}. {q['question']} (정답: {q['answer']}번)")

def main():
    """메인 메뉴 실행 함수"""
    data = load_data()
    while True:
        print("\n====================")
        print(" 🎮 나만의 퀴즈 앱")
        print("====================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 삭제")
        print("4. 퀴즈 목록 보기")
        print("5. 종료")
        
        choice = input("메뉴를 선택하세요 (1~5): ").strip()
        if choice == '1':
            play_quiz(data)
        elif choice == '2':
            add_quiz(data)
        elif choice == '3':
            delete_quiz(data)
        elif choice == '4':
            list_quizzes(data)
        elif choice == '5':
            save_data(data)
            print("\n데이터를 저장하고 프로그램을 종료합니다.")
            break
        else:
            print("[오류] 1에서 5 사이의 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()