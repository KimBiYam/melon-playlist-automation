https://oboki.net/workspace/python/selenium%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-melon-playlist-%EC%B6%94%EA%B0%80-%EC%9E%90%EB%8F%99%ED%99%94/

해당 포스트 코드 기반으로 현재 날짜(2022-04-17) 기준으로 돌아가게끔 수정한 레포  
플레이리스트 텍스트 파일을 파싱하여서 멜론 플레이리스트에 추가 자동화

### 준비 사항 
- 사용하는 크롬 버전에 맞는 chromedriver - [다운로드](https://chromedriver.chromium.org/downloads)
  - 프로젝트 디렉토리에 추가
- 플레이리스트 텍스트 파일(`playlist.txt`)
  - 프로젝트 디렉토리에 추가
  - 텍스트 한 줄 마다 artist - title 의 형태여야 함
- selenium 설치
```bash
$ pip3 install selenium
```

### 실행
```bash
$ python3 main.py
```

### 참고 사항
플레이리스트 추가 실패 시 해당 곡 검색명은 error.log 파일에 기록됩니다