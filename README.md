# 코디세이 1주차 과제
# 개발 환경 구축 및 Docker 웹 서버 실습

## 1. 개발 환경
- OS: Windows 11
- Container Runtime: Docker Desktop (WSL 2)
- IDE: Visual Studio Code

## 2. Nginx 웹 서버 컨테이너 실행
```bash
docker run -d -p 80:80 --name my-web-server nginx

```
PS C:\Users\posso\OneDrive\바탕 화면\코디세이> docker version
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