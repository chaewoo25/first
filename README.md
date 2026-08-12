# 코디세이 1주차 과제
# 개발 환경 구축 및 Docker 웹 서버 실습

## 👤 작성자 정보
- **GitHub**: chaewoo25

---

## 1. 개발 및 실습 환경
- **OS**: Windows 11
- **가상화 환경**: WSL 2 (Ubuntu)
- **Container Runtime**: Docker Desktop 4.85.0
- **IDE**: Visual Studio Code

---

## 2. Nginx 웹 서버 컨테이너 실행

```bash
docker run -d -p 80:80 --name my-web-server nginx
```

---

## 3. Docker 주요 명령어 실행 결과

### ① `docker version`
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

### ② `docker info`
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

### ③ `docker images`
```text
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    21f8c0e3416b   2 weeks ago    187MB
```

### ④ `docker ps -a`
```text
CONTAINER ID   IMAGE   COMMAND                  CREATED          STATUS          PORTS                               NAMES
a24ddec10034   nginx   "/docker-entrypoint.s…"   12 minutes ago   Up 12 minutes   0.0.0.0:80->80/tcp, [::]:80->80/tcp my-web-server
```