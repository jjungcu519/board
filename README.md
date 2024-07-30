# 반복 작업 관리

## include

- 앱마다 (기능마다) url을 따로 관리할 수 있도록 함
    - 앱폴더 내에 urls.py 생성
    - 기존 urls.py에 import include

## 템플릿 경로 지정
- settings.py 내 TEMPLATES에 DIRS를 BASE_DIR/'templates' 로 설정

## {% url '앱이름:이름' %}
- path 함수를 찾기 위해 urls.py에 app_name을 지정

## post와 csrf 토큰
- post -> 데이터를 같이 담아서 보내기 위한 메서드
- csrf 토큰 -> 직인, 양식

- RESTFUL 코드 작성
![](https://gmlwjd9405.github.io/images/network/rest.png)