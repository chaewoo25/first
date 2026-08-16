# 코디세이 1주차 과제: 개발 환경 구축 및 Docker 웹 서버 실습 보고서

## 📌 1. 과제 개요 (Overview)
본 과제는 최신 컨테이너 가상화 기술인 Docker를 활용하여 개발 환경을 구축하고, Nginx 웹 서버 컨테이너 구동, 커스텀 이미지 빌드, 데이터 영속성 관리를 포함한 기본 실습을 목표로 합니다. WSL 2 기반 가상화 환경에서 Docker Engine 및 VSCode를 연동하고, 리눅스 기초 CLI 명령어와 핵심 Docker 명령어를 통해 컨테이너 생태계의 동작 메커니즘을 분석 및 기록하였습니다.

- **교육 과정**: 코디세이 AI All-in-One 2기
- **작성자**: 박채우
- **GitHub 계정**: chaewoo25
- **저장소 주소**: [https://github.com/chaewoo25/first](https://github.com/chaewoo25/first)

---

## 💻 2. 개발 및 실습 환경 (Environment)

| 구분 | 환경 명세 |
| :--- | :--- |
| **Host OS** | Windows 11 Home |
| **Virtualization** | WSL 2 (Windows Subsystem for Linux) |
| **Container Engine** | Docker Desktop 4.85.0 |
| **IDE / Editor** | Visual Studio Code |
| **CLI Terminal** | PowerShell / Windows Terminal |
| **Version Control** | Git / GitHub |

---

## 📁 3. 리눅스 기본 CLI 명령어 및 파일 권한 실습

### 3.1 디렉토리 및 파일 생성/이동/삭제
```bash
# 1. 작업 디렉토리 생성 및 이동
mkdir -p ~/workspace/test_dir && cd ~/workspace/test_dir

# 2. 테스트 파일 생성
touch sample.txt

# 3. 파일 이동 및 이름 변경
mv sample.txt test_file.txt

# 4. 파일 및 디렉토리 삭제
cd .. && rm -rf test_dir

3.2 파일 권한 변경 (chmod) 검증
# 1. 파일 생성 및 기본 권한 확인
touch permission_test.sh
ls -l permission_test.sh
# 출력: -rw-r--r-- 1 user user 0 permission_test.sh

# 2. 실행 권한 부여 (755 설정)
chmod 755 permission_test.sh
ls -l permission_test.sh
# 출력: -rwxr-xr-x 1 user user 0 permission_test.sh

# 일반 파일 권한 변경 (644 설정)
chmod 644 sample.txt
ls -l sample.txt
# 출력: -rw-r--r-- 1 user user 0 sample.txt
```
🚀 4. Docker Engine 및 Hello-World 실행 검증
```bash
4.1 docker --version 출력
docker --version
# 출력: Docker version 29.6.2, build dfc4efb
4.2 docker run hello-world 정상 실행
docker run hello-world
```
🌐 5. Nginx 웹 서버 컨테이너 구동 및 포트 매핑
```bash
5.1 컨테이너 실행 명령어 (포트 매핑)
docker run -d -p 80:80 --name my-web-server nginx
```
🛠️ 6. Dockerfile 작성 및 커스텀 이미지 빌드
6.1 Dockerfile 작성
```bash
# Base 이미지 설정
FROM nginx:alpine

# 커스텀 index.html 복사
COPY index.html /usr/share/nginx/html/index.html

# 80번 포트 노출
EXPOSE 80
```
6.2 이미지 빌드 및 매핑 포트 접속
```bash
# 1. 커스텀 이미지 빌드
docker build -t my-custom-nginx:1.0 .

# 2. 빌드된 커스텀 이미지 구동 (포트 8080 매핑)
docker run -d -p 8080:80 --name custom-web my-custom-nginx:1.0
```
💾 7. Docker Volume을 활용한 데이터 영속성 유지 검증
```bash
# 1. 호스트 OS 및 컨테이너 간 볼륨 마운트 실행 (-v 옵션)
docker run -d -p 8081:80 -v ~/nginx_data:/usr/share/nginx/html --name vol-test nginx

# 2. 호스트 마운트 폴더에 테스트 파일 생성
echo "Volume Data Test" > ~/nginx_data/test.html

# 3. 컨테이너 강제 삭제
docker rm -f vol-test

# 4. 데이터 영속성 검증 (컨테이너 삭제 후에도 호스트 폴더 파일 보존 확인)
cat ~/nginx_data/test.html
# 출력 결과: Volume Data Test
```
🧹 8. 이미지 및 컨테이너 목록 확인 및 자원 정리
```bash
8.1 목록 확인 (ps -a, images)

# 실행 중 및 정지된 전체 컨테이너 목록 확인
docker ps -a

# 다운로드 및 빌드된 전체 이미지 목록 확인
docker images

8.2 자원 정리 (rm, rmi)

# 1. 컨테이너 정지 및 삭제
docker stop my-web-server custom-web
docker rm my-web-server custom-web

# 2. 미사용 이미지 삭제
docker rmi my-custom-nginx:1.0 hello-world
```
🐙 9. Git 설정 및 GitHub 연동
```bash
# 1. Git 사용자 환경 설정
git config --global user.name "chaewoo25"

# 2. 원격 저장소(first) 연결 및 최종 푸시
git remote set-url origin https://github.com/chaewoo25/first.git
git add .
git commit -m "docs: 1주차 과제 보고서 9가지 항목 완벽 정리"
git push origin main --force
```

---

## 💡 10. 동작 구조 설계 및 핵심 기술 원리 분석

### 10.1 동작 구조 설계
* **디렉토리 구조 구성 기준**: 소스 코드(`index.html`), 컨테이너 설정(`Dockerfile`), 설명 문서(`README.md`)를 역할별로 분리하여 유지보수성과 가독성을 높였습니다.
* **포트/볼륨 재현성 확보**: 컨테이너 실행에 필요한 포트 매핑(`-p 8080:80`)과 볼륨 바인딩(`-v ~/nginx_data:...`) 옵션을 문서에 명시하여 타 환경에서도 동일한 명령어로 실습을 재현할 수 있도록 정리했습니다.

### 10.2 핵심 기술 원리 적용

* **이미지 vs 컨테이너의 차이 (빌드/실행/변경)**
  * **빌드(Build)**: `Dockerfile`을 기반으로 애플리케이션 실행 환경 전체를 하나의 읽기 전용(Read-Only) 템플릿인 **이미지**로 생성합니다.
  * **실행(Run)**: 읽기 전용 이미지를 로드하고, 그 위에 읽기/쓰기가 가능한 레이어(Writable Layer)를 얹어 격리된 프로세스로 구동하는 상태가 **컨테이너**입니다.
  * **변경(Change)**: 컨테이너 내부에서 일어나는 데이터 수정 및 삭제는 컨테이너 레이어에만 남으며, 원본 이미지에는 전혀 영향을 주지 않습니다.

* **컨테이너 포트 격리 및 포트 매핑**
  * **접속 불가 이유**: 컨테이너는 격리된 자체 네트워크 네임스페이스와 프라이빗 IP를 가지므로 호스트 OS 외부에서 직접 접근할 수 없습니다.
  * **포트 매핑의 필요성**: 보안을 위해 내부 포트를 격리하되, 외부 통신이 필요한 포트만 선택적으로 호스트 포트와 연결(`-p 호스트포트:컨테이너포트`)하여 안전하게 서비스를 노출하기 위해 필요합니다.

* **절대 경로 vs 상대 경로 선택 기준**
  * **절대 경로**: 시스템 위치가 명확히 고정되어야 하는 Docker 볼륨 바인딩(`~/nginx_data` 또는 `/usr/share/nginx/html`) 및 시스템 환경변수 설정 시 사용합니다.
  * **상대 경로**: 프로젝트 내부 파일 참조, 소스 코드 이동 및 다른 환경에서의 실행 시 연동 경로가 깨지지 않아야 하는 상황에서 사용합니다.


<img width="1011" height="83" alt="화면 캡처 2026-08-05 164250" src="https://github.com/user-attachments/assets/ef0fb611-b79b-4f0e-b19e-c498bcccc751" />
<img width="1896" height="111" alt="화면 캡처 2026-08-05 164149" src="https://github.com/user-attachments/assets/f2328c6a-7a44-44df-b9d8-9df8e1c43486" />
<img width="1590" height="1199" alt="화면 캡처 2026-08-05 164000" src="https://github.com/user-attachments/assets/860ec124-f44e-43a0-bccd-ed3c9b2f5067" />
<img width="672" height="476" alt="화면 캡처 2026-08-05 163910" src="https://github.com/user-attachments/assets/80750fea-16dc-4cc5-84e9-16f0d88ac688" />
