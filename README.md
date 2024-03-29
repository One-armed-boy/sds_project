# 서비스데이터사이언스 과목 프로젝트(22.04 ~ 22.06)
# <오늘 뭐 먹지> 어플의 Backend src

## 1. 목적
- 경희대학교 근처 음식점에 대해, 사용자(경희대 학생)의 리뷰 및 평점 기반 음식점 추천 시스템  

## 2. 언어 및 프레임워크
- Front: Dart (Flutter)
- Back: Python (Django Rest Framework)
- DB: Sqlite3

## 3. 배포
- Github에 연동 후 Heroku 무료 배포 서비스 이용

## 4. 구현
### 1) 회원 가입, 로그인 기능
- 기본 회원 가입 및 로그인 기능은 장고에서 기본적으로 제공하는 기능을 상속하여 구현. 프로젝트의 규모를 고려하여 사용자의 개인 정보를 최소로 받을 수 있도록 설계하여 이메일을 제외한 다른 개인정보를 수집하지 않음. 따라서 회원 가입, 로그인 시 필요한 정보는 이메일(아이디)과 비밀번호
- 사용자 인증에 JWT(JSON WEB TOKEN) 방식을 이용. 이는 rest_framework_simplejwt를 이용하여 구현. 로그인 시 access token과 refresh token을 사용자에게 발급. 사용자는 이를 Flutter 내 변수로 갖고 있다가, 인증이 필요한 요청 시 access token을 Authorization header에 Bearer 타입으로 담아 http 통신.
### 2) 사용자 등록 별점 기반 별점 예측 기능
- 서비스 사용자들이 기존에 남긴 음식점 별점들을 이용하여 유저 X 음식점 행렬을 구성하고, 이를 SVD를 통해 차원 축소하여 K개의 사용자 별점 분포에 대한 설명력을 갖는 가중치들을 획득.(Truncated SVD)
- 위에서 얻어낸 가중치를 이제 예측의 타겟이 되는 사용자에게 적용하여 사용자가 방문하지 않은 음식점에 대해 해당 사용자가 남길 것으로 예상되는 별점 예측.
