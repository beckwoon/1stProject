1st Project - car_mgt program in autoplus


1. 장고 설치
$ pip install django==2.1
(pymysql 사용을 위해 2.1버전으로 다운로)

2. 프로젝스 시작(설정)
$ django-admin startproject config .

3. DB 설치
  <SQL lite 활용>
  $ python manage.py migrate


  - admin 사용자 추가 -
  $ python manage.py createsuperuser
  ID : admin
  PW : abcd1234


  <AWS에 DB 셋팅하여 활용>
  1) AWS RDB에 DB 생성 => [db name = predata]
  2) DB 모듈 추가
     $ pip install pymysql
  3) setting에 import pymysql & DB 설정 변경
  4) 데이터 베이스 재설정
     $ python manage.py migrate
  5) 관리자 계정 생성
     $ python manage.py createsuperuser
     ID : admin
     PW : abcd1234



4. Static 파일 서버 설정 <AWS S3>
  1) staic 파일 설정 모듈 설치
    $ pip install boto3  => AWS S3 접속 모듈
    $ pip install django-storages

  2) AWS S3(스토리지) 서버만들기 (autoplus-storage)
  3) IAM 사용자 추가 및 권한 설
    - 엑세스 유형 => 프로그래밍 방식 엑세스
    - 그룹생성 -> autoplus_gorup -> AmazonS3FullAccess 선택
    - 엑세스 키 다운도드

  4) setting 설정

  5) 파일스토르지 설정 [config/asset_storage.py]

5. Static 파일 모으기 실행
$ python manage.py collectstatic

---------------------
6. Account App 만들기 (app_name = Account)
  생략 (로그인, 로그아웃, 회원가입)
---------------------

7. App 만들기 (input)
$ python manage.py startapp input
=> setting 추가

8. input/models.py 설정 => 엑셀 저장하는 DB
9. DB 반영
$ python manage.py makemigrations input
$ python manage.py migrate input

10. Admin에 데이터 관리 등록

11. input/views.py 만들기

12. urls 연결
 1) config/urls.py
 2) input/urls.py

13. 관리자 페이지 만들기 [input/admin.py]

14. 템플릿 만들기
[input/templates/file_list.html]
[input/templates/upload.html]

15. 레이아웃 템플렛 만들기
[templates/layout.html]
===============================

16. App 만들기 (monitoring)
$ python manage.py startapp monitoring
=> setting 추가

17. monitoring/views.만들

18. urls 연결
 1) config/urls.py
 2) monitoring/urls.py

19. 템플릿 만들기
[monitoring/templates/ban_board.html]
=> 작성요청(*****)

20. 업로드 엑셀 끌어와서 데이터 베이스로 입력
 1) 반납 엑셀데이터 저장 테이블 => [monitoring/models.py]
   $ python manage.py migrations monitoring
   $ python manage.py mograte monitoring

 2) 엑셀 데이터를 불러와서 테이블에 저장 => [monitoring/views.py]

   $ pip install openpyxl
   $ pip install pandas
   $ pip install xlrd

 3) 반납 현황 로직 및 화면 구성 => [monitoring/views2.py]
   3-1) 대량반납 현황 게시판
       [monitoring/models.py] => 게시판 모델 추가

       $ python manage.py makemigrations monitoring
       $ python manage.py migrate monitoring
       admin 등록

       [monitoring/views2.py] => 리스트뷰, 추가뷰, 수정뷰, 삭제뷰 추가

       [monitoring/urls.py] => 추가

       [monitoring/templates/massboard_list.html]
       [monitoring/templates/massboard_create.html]
       [monitoring/templates/massboard_update.html]
       [monitoring/templates/massboard_confirm_delete.html]


   3-2) 차량상세 뷰 => [monitoring/templates/data_detail.html]
   3-3) 차량상세 수정 => [monitoring/templates/data_update.html]

 4) 검색 기능 구현
   4-1) url 설정
      path('data/', search_list, name='search')
   4-2) view 설정
   4-3) template 설정 [monitoring/templates/data_list.html]


21. 원상회복관리 [recovery]
 1) 앱 등록, URL 생성, admin 등록
 2) 모델 만들기 [recovery/models.py]
   python manage.py makemigrations recovery
   pathon manage.py migrate recovery
 3) 뷰, 템플릿 만들기
   3-1) 뷰 만들기 [recovery/views.py]
   3-2) 탬플릿 만들기 [recovery/templates/re_board.html]
 4) 원상회복 신규등록
   4-1) 템플릿 만들기 [recovery/templates/re_create.html]]
   4-2) 뷰 만들기
 5) 원상회복 관리 기능(삭제, 수정 등)
 6) 입금내역 관리

22. 반납관리 [remgt]
 1) 앱등록, URL 생성, admin 등록
 2) 뷰, 탬플릿 만들기

23. 메입화면 구성 [ban_board]



----- ver1 완료 - Git 업로드 ----

1) Initialized empty Git repository
  $ git init

2) 관리 목록 설정
  $ git add -A

3) commit
  $ git commit -m "이름"

4) 업로드 리포지터리 등록
  $ git remote add origin http://리포지토리주소

5) master로 Push
  $ git push -u origin master



----- AWS EC2 활용 -----

1) EC2 인스턴트 생성

2) Ubuntu Server 18.04 LTS (HVM), SSD Volume Type  선택

3) 보안그룹 구성
 => 이름 설명 추가
   이름 : 1stProject_autoplus
   규칙추가 => 새로운 유형 추가 => HTTP 유형 => 소스위치 무관 선택

4) 새 키 페어 생성 => 키 페어 다운로드

5) 인스턴트 접속 - 터미널로 접속 -

  5-1) 소유자만 키페어 파일을 읽을 수 잇는 권한을 부여
    $ chmod 400 ~/Downloads/1stProject-key.pem
  5-2) 키페어 위치 이동 [~/.ssh]
    $ mv ~/Downloads/1stProject-key.pem ~/.ssh/
  5-3) 인스턴트 접속 [ubuntu 접속]
    $ ssh -i ~/.ssh/1stProject-key.pem ubuntu@[퍼블릭DNS]

  5-4) 서버 환경 설정
    <페키지 정보 업데이트>
    $ sudo apt-get data_update
    <패키지 의존성 검사 및 업그레이드>
    $ sudo apt-get dist-upgrade

    <웹서버 프로그램 nginx 설치>
    (1) PPA 저장소 업데이트
      $ sudo apt-get update
    (2) nginx 설치
      $ sudo apt-get install nginx
    (3) 버전 확인
      $ nginx -v
    (4) 웹서버 동작 확인
      $ systemctl status nginx

    * 웹 창에서 퍼블릭DNS을 입력하여 서버 구동을 확인

    <장고 웹 어플리케이션 동작을 위한 전용 그룹과 계정을 설정>
    (1) 사용자 그룹생성 [그룹명 : djangogroup]
      $ sudo groupadd djangogroup
    (2) 유저 생성 [유저명 : django]
      $ sudo useradd -g djangogroup -b /home -m -s /bin/bash django
    (3) 소스코드 업로드 폴더 생성
      $ sudo mkdir -p /var/www/1stProject
    (4) 해당 폴더에 djang 유저와 djangogroup 그룹에 소유권을 설정
      $ sudo chown django:djangogroup /var/www/1stProject/
    (5) ubuntu유저를 djangogroup에 추가
      $ sudo usermod -a -G djangogroup ubuntu
    (6) 업로드 폴더 쓰기 권한을 그룹에 속한 모든 유저에게 부여
      $ sudo chmod g+w /var/www/1stProject

  5-5) 필요 패키지 설치
    $ sudo apt-get install build-essential libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info libssl-dev
    (weasyprint를 위한 패키지 다수)

    <python 3.7 업그레이드>
    $ python3 -V
    $ sudo apt-get install python3.7
    $ python3.7 -V
    $ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
    $ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
    $ sudo update-alternatives --config python3
    => type selection number: 2
    python3 -V

    $ sudo apt-get install python3.7-dev
    $ sudo apt-get install python3-pip
    $ sudo apt-get install python3-cffi
    $ sudo apt-get install python3.7-venv

6) 추가 수정 작업
  6-1) 인스톨 라이브러리 목록 추출 [PyCharm]
    $ pip freeze > requirements.txt
  6-2) settings.py 설정변경 [config/settings.py]
    DEBUG = False
    ALLOWED_HOSTS = ['.compute.amazonaws.com']

7) 파일질라 사용 [업로드]

  7-1) 사이트 관리자 -> 새 사이트
  7-2) 설정
    프로토콜 [SFTP - SSH File Transfer Protocol]
    호스트 => 퍼블릭 DNS
    로그온 유형 => '키파일'
    사용자 => 'ubuntu'
    키파일 위치 '/Users/beckwoon/.ssh/1stProject.pem'

  7-3) 업로드 [/var/www/1stProject]

8) 파이썬 가상환경 설정 [Ubuntu]
  8-1) 업로드 폴더 이동
    $ cd /var/www/1stProject
  8-2) 가상환경 폴더 'venv설정'
    $ sudo python3 -m venv venv
  8-3) 관리자 상태 변경
    $ sudo -s
  8-4) 가상환경 활성화
    $ source venv/bin/activate
  8-5) 필요한 인스톨 라이브러리를 일괄 설치
    $ pip install -r requirements.txt

  <uWSGI 환경설정>
  8-6) WSGI 사용을 위한 uwsgi 모듈 설치
    $ pip install uwsgi

  8-7) uwsgi 동작을 위한 필요한 폴더 생성
    $ sudo mkdir run logs ssl
  8-8) 권한 변경
    $ sudo chown django:www-data run
    $ sudo chown django:www-data logs
  8-9) uwsgi.ini 파일 만들고 편집 [var/www/1stProject/run/uwsgi.ini]

    $ vim /var/www/1stProject/run/uwsgi.ini

      [uwsgi]
      uid = django
      base = /var/www/1stProject
      home = %(base)/venv
      chdir = %(base)
      module = config.wsgi:application
      env = DJANGO_SETTINGS_MODULE=config.settings

      master = true
      processes = 5

      socket = %(base)/run/uwsgi.sock
      logto = %(base)/logs/uwsgi.log
      chown-socket = %(uid):www-data
      chmod-socket = 660
      vacuum = true

    $ vim /etc/systemd/system/uwsgi.service

      [Unit]
      Description=uWSGI Emperor service

      [Service]
      ExecStart=/var/www/1stProject/venv/bin/uwsgi --emperor /var/www/1stProject/run

      User = django
      Group = www-data

      Restart=on-failure
      KillSignal=SIGQUIT
      Type=notify
      NotifyAccess=all
      StandardError=syslog

      [Install]
      WantedBy=multi-user.target

  8-10) uwsgi 서비스 시작
    $ systemctl start uwsgi
  8-11) uwsgi 서비스를 시작 서비스로 등록
    $ systemctl enable uwsgi
  8-12) uwsgi 동작 상태 확인
    $ systemctl status uwsgi

  <nginx 설정>
  8-13) 기본 설정 파일을 복사해 1stProject 위한 설정 파일을 만듬 (cp = copy)
    $ cp /etc/nginx/sites-available/default /etc/nginx/sites-available/1stProject

  8-14) 설정 파일을 nginx가 서비스 중인 싸이트로 링크 (ln = link)
    $ ln -s /etc/nginx/sites-available/1stProject /etc/nginx/sites-enabled

  8-15) nginx.conf 파일 수정 [etc/nginx/nginx.conf]
    $ vim /etc/nginx/nginx.conf

    <수정>
    # server_names_hash_bucket_size 64;
    ==>
    server_names_hash_bucket_size 128;

  8-16) nginx 설정변경-uwsgi 동작 [etc/nginx/site-available/1stProject]
    $ vim /etc/nginx/sites-available/1stProject

    upstream django {
        server unix:/var/www/1stProject/run/uwsgi.sock;
    }
    server {
        listen 80;
        server_name ec2-13-209-21-172.ap-northeast-2.compute.amazonaws.com;
        charset utf-8;

        location / {
                include         /etc/nginx/uwsgi_params;
                uwsgi_pass      django;
        }
    }

  8-17) 살장깂 점검
    $ nginx -t

    nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
    nginx: configuration file /etc/nginx/nginx.conf test is successful

  8-18) 서버 재시작
    $ systemctl restart nginx
