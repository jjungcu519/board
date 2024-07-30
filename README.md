# 반복 작업 관리

## include

- 앱마다 (기능마다) url을 따로 관리할 수 있도록 함
    - 앱폴더 내에 urls.py 생성
    - 기존 urls.py에 import include

## 템플릿 경로 지정
- settings.py 내 TEMPLATES에 DIRS를 BASE_DIR/'templates' 로 설정