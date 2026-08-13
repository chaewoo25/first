# 코디세이 1주차 과제: 개발 환경 구축 및 Docker 웹 서버 실습 보고서

## 📌 1. 과제 개요 (Overview)
본 과제는 최신 컨테이너 가상화 기술인 Docker를 활용하여 개발 환경을 구축하고, Nginx 웹 서버 컨테이너 구동, 커스텀 이미지 빌드, 데이터 영속성 관리를 포함한 기본 실습을 목표로 합니다. WSL 2 기반 가상화 환경에서 Docker Engine 및 VSCode를 연동하고, 리눅스 기초 CLI 명령어와 핵심 Docker 명령어를 통해 컨테이너 생태계의 동작 메커니즘을 분석 및 기록하였습니다.

- **교육 과정**: 코디세이 AI All-in-One 2기
- **작성자**: 박채우
- **GitHub 계정**: chaewoo25
- **저장소 주소**: https://github.com/chaewoo25/first

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

# 1. 작업 디렉토리 생성 및 이동
mkdir -p ~/workspace/test_dir && cd ~/workspace/test_dir

# 2. 테스트 파일 생성
touch sample.txt

# 3. 파일 이동 및 이름 변경
mv sample.txt test_file.txt

# 4. 파일 및 디렉토리 삭제
cd .. && rm -rf test_dir

# 1. 파일 생성 및 기본 권한 확인
touch permission_test.sh
ls -l permission_test.sh
# 출력: -rw-r--r-- 1 user user 0 permission_test.sh

# 2. 실행 권한 부여 (755 설정)
chmod 755 permission_test.sh
ls -l permission_test.sh
# 출력: -rwxr-xr-x 1 user user 0 permission_test.sh

docker run -d -p 80:80 --name my-web-server nginx

Client:
 Version:           29.6.2
 API version:       1.55
 Go version:        go1.26.5
 Git commit:        dfc4efb
 Built:             Thu Jul 16 16:14:59 2026
 OS/Arch:           windows/amd64
 Context:           desktop-linux

Server: Docker Desktop 4.85.0 (235549)
 Engine:
  Version:          29.6.2
  API version:      1.55 (minimum version 1.40)
  Go version:       go1.26.5
  Git commit:       3d80467
  Built:            Thu Jul 16 16:12:20 2026
  OS/Arch:          linux/amd64

  docker run hello-world

  Client: Docker Engine - Community
 Version:    29.6.2
 Context:    desktop-linux
 Debug Mode: false

Server:
 Containers: 1
  Running: 1
  Paused: 0
  Stopped: 0
 Images: 1
 Server Version: 29.6.2
 Storage Driver: overlay2
 Operating System: Docker Desktop
 OSType: linux
 Architecture: x86_64
 CPUs: 16
 Total Memory: 15.54GiB
 Name: docker-desktop

 REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    21f8c0e3416b   2 weeks ago    187MB
hello-world  latest    d2c38467ad3d   3 months ago   13.3kB

CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                               NAMES
a24ddec10034   nginx     "/docker-entrypoint.s…"   12 minutes ago   Up 12 minutes   0.0.0.0:80->80/tcp, [::]:80->80/tcp my-web-server

# Base 이미지 설정
FROM nginx:alpine

# 커스텀 index.html 복사
COPY index.html /usr/share/nginx/html/index.html

# 80번 포트 노출
EXPOSE 80

# 1. 커스텀 이미지 빌드
docker build -t my-custom-nginx:1.0 .

# 2. 빌드된 커스텀 이미지 구동 (포트 8080 매핑)
docker run -d -p 8080:80 --name custom-web my-custom-nginx:1.0

# 1. 호스트 OS 및 컨테이너 간 볼륨 마운트 실행 (-v 옵션)
docker run -d -p 8081:80 -v ~/nginx_data:/usr/share/nginx/html --name vol-test nginx

# 2. 호스트 마운트 폴더에 테스트 파일 생성
echo "Volume Data Test" > ~/nginx_data/test.html

# 3. 컨테이너 강제 삭제
docker rm -f vol-test

# 4. 데이터 영속성 검증 (컨테이너 삭제 후에도 호스트 폴더 파일 보존 확인)
cat ~/nginx_data/test.html
# 출력 결과: Volume Data Test

# 1. 실행 중인 컨테이너 정지 및 삭제
docker stop my-web-server custom-web
docker rm my-web-server custom-web

# 2. 불필요한 이미지 삭제
docker rmi my-custom-nginx:1.0 hello-world

# 1. Git 사용자 환경 설정
git config --global user.name "chaewoo25"

# 2. 원격 저장소(first) 연결 및 푸시
git remote set-url origin [https://github.com/chaewoo25/first.git](https://github.com/chaewoo25/first.git)
git add .
git commit -m "docs: 1주차 과제 보고서 완료"
git push origin main
