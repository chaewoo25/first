# 코디세이 1주차 과제: 개발 환경 구축 및 Docker 웹 서버 실습 보고서

## 📌 1. 과제 개요 (Overview)
본 과제는 최신 컨테이너 가상화 기술인 Docker를 활용하여 개발 환경을 구축하고, Nginx 웹 서버 컨테이너를 구동 및 제어하는 기본 실습을 목표로 합니다. WSL 2 기반 가상화 환경에서 Docker Engine 및 VSCode를 연동하고, 핵심 Docker 명령어를 통해 컨테이너 생태계의 동작 메커니즘을 분석 및 기록하였습니다.

- **교육 과정**: 코디세이 AI All-in-One 2기
- **작성자**:박채우
- **GitHub 계정**: chaewoo25
- **저장소 주소**: https://github.com/chaewoo25/ia-codyssey

---

## 💻 2. 개발 및 실습 환경 (Environment)

| 구분 | 환경 명세 
| :--- | :--- 
| **Host OS** | Windows 11 Home 
| **Virtualization** | WSL 2 (Windows Subsystem for Linux) 
| **Container Engine** | Docker Desktop 4.85.0 
| **IDE / Editor** | Visual Studio Code 
| **CLI Terminal** | PowerShell / Windows Terminal 
| **Version Control** | Git / GitHub
---

## 🚀 3. Nginx 웹 서버 컨테이너 실행 및 옵션 분석

### 3.1 컨테이너 실행 명령어
```bash
docker run -d -p 80:80 --name my-web-server nginx
```


---

## 🔍 4. Docker 주요 명령어 실행 결과 및 상세 분석

### ① `docker version` (클라이언트 및 서버 버전 확인)
Docker Client와 Daemon Server의 API 버전, 빌드 날짜, Go 언어 환경 및 아키텍처 정보를 출력합니다.

```text
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
  Experimental:     false
 containerd:
  Version:          v2.2.5
  GitCommit:        e53c7c1516c3b2bff98eb76f1f4117477e6f4e66
 runc:
  Version:          1.3.6
  GitCommit:        v1.3.6-0-g491b69ba
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

---

### ② `docker info` (시스템 전체 가상화 자원 정보 확인)
Docker 엔진이 사용할 수 있는 CPU, 메모리, 스토리지 드라이버(overlay2) 및 실행 중인 컨테이너 상태를 점검합니다.

```text
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
```

---

### ③ `docker images` (로컬 이미지 저장소 확인)
다운로드되어 local 레지스트리에 보관되어 있는 Docker 이미지 파일 목록과 용량을 확인합니다.

```text
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    21f8c0e3416b   2 weeks ago    187MB
```

---

### ④ `docker ps -a` (전체 컨테이너 상태 확인)
현재 구동 중인 컨테이너의 ID, 이미지, 실행 상태(`Up`), 포트 바인딩 상태를 검증합니다.

```text
CONTAINER ID   IMAGE   COMMAND                  CREATED          STATUS          PORTS                               NAMES
a24ddec10034   nginx   "/docker-entrypoint.s…"   12 minutes ago   Up 12 minutes   0.0.0.0:80->80/tcp, [::]:80->80/tcp my-web-server
```

---

## 🌐 5. 네트워크 검증 및 동작 원리

### 5.1 웹 브라우저 접속 테스트
* **접속 주소**: `http://localhost` 또는 `http://127.0.0.1`
* **접속 결과**: Nginx 기본 안내 페이지(**"Welcome to nginx!"**) 정상 수신 확인

### 5.2 네트워크 흐름 매커니즘
1. 사용자 브라우저에서 `localhost:80`으로 HTTP 요청 전송
2. Host OS(Windows 11)의 80번 포트에서 요청 수신
3. Docker Desktop의 가상 바인딩 포트에 의해 `my-web-server` 컨테이너의 80번 포트로 트래픽 전달
4. 컨테이너 내부에서 실행 중인 Nginx 프로세스가 `index.html` 문서 응답 반환

---