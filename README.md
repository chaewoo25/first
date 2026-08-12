# 코디세이 1주차 과제
# 개발 환경 구축 및 Docker 웹 서버 실습

## 1. 개발 환경
- OS: Windows 11
- Container Runtime: Docker Desktop (WSL 2)
- IDE: Visual Studio Code

## 2. Nginx 웹 서버 컨테이너 실행
```bash
docker run -d -p 80:80 --name my-web-server nginx