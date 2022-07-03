# 서비스데이터사이언스 과목 프로젝트(22.04 ~ 22.06)
# <오늘 뭐 먹지> 어플의 Backend src

## 1. 언어 및 프레임워크
- Front: Dart (Flutter)
- Back: Python (Django Rest Framework)
- DB: Sqlite3

## 2. 배포
- Github에 연동 후 Heroku 무료 배포 서비스 이용

## 3. 구현 목록
### 1) 회원 가입, 로그인 기능
- 기본 회원 가입 및 로그인 기능은 장고에서 기본적으로 제공하는 기능을 상속하여 구현. 프로젝트의 규모를 고려하여 사용자의 개인 정보를 최소로 받을 수 있도록 설계하여 이메일을 제외한 다른 개인정보를 수집하지 않음. 따라서 회원 가입, 로그인 시 필요한 정보는 이메일(아이디)과 비밀번호
- 사용자 인증에 JWT(JSON WEB TOKEN) 방식을 이용. 이는 rest_framework_simplejwt를 이용하여 구현. 로그인 시 access token과 refresh token을 사용자에게 발급. 사용자는 이를 Flutter 내 변수로 갖고 있다가, 인증이 필요한 요청 시 access token을 Authorization header에 Bearer 타입으로 담아 http 통신.
### 2) 나중에 이어쓰겠음.
