### 초기 환경 설정
```bash
# 가상환경 설정 및 Django 설치
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install django djangorestframework django-cors-headers pydantic

# Django 프로젝트 생성
django-admin startproject backend
cd backend

# 게시판 애플리케이션 생성
python manage.py startapp board

# 모델 마이그레이션
python manage.py makemigrations
python manage.py migrate

# 관리자 계정 생성
python manage.py createsuperuser  # 관리자 계정 생성

# 서버 실행
python manage.py runserver
```

```bash
# Next.js 프로젝트 생성 (기본 설정값)
npx create-next-app frontend
cd frontend
npm install  # 기본 의존성 설치
npx shadcn@latest init

# ShadCN은 공식적으로 별도 설치가 필요할 수 있음. 프로젝트에 맞게 설정



```