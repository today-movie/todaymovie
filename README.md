# 한림대학교 캡스톤디자인 '오늘 뭐 볼래?'
---
<img src=README/readme_main.png>
20210830~20211204

## 구현목적 : 크롤링을 통한 키워드 영화추천 시스템
- 사용자가 원하는 단어(ex 로맨스)를 입력하여 그에 맞는 영화를 추천해주는 시스템
- 왓챠피디아, 네이버영화 등 영화 리뷰 핵심 단어를 추출
- 추출한 데이터를 기반으로 입력값과의 코사인 유사도를 측정하여 추천
- 입력된 단어와 유사한 단어를 word2Vec을 사용하여 출력
- 추천된 영화를 기반으로 또 다른 유사한 영화를 제공

## 데이터 수집
1. 왓챠피디아 리뷰
2. 네이버영화 리뷰

## 구현내용 요약
1. 로그인 및 마이페이지 기능.
2. 사용자가 원하는 장르를 클릭하여 영화 및 TV 프로그램을 검색할 수 있다.
3. 게시판에 사용자들이 리뷰를 작성할 수 있다.
4. 

## 시연동영상
- 데이터 시각화<br>
<img width="50%" src="https://user-images.githubusercontent.com/66001046/144744851-18d7ec3d-8fd5-486a-bd02-3fab45771ba4.gif">
<img width="50%" src="https://user-images.githubusercontent.com/66001046/144744853-03115b7c-6862-449a-9927-f50145448879.gif">

- 웹사이트<br>
<img width="50%" src="https://user-images.githubusercontent.com/66001046/144420434-35c34b70-32e0-47dd-92ef-6fdf8b500ec3.gif"><img width="50%" src="https://user-images.githubusercontent.com/66001046/144420442-6b5d51df-088f-4191-bbdc-3bf0789c6cf9.gif">
<img width="50%" src="https://user-images.githubusercontent.com/66001046/144426056-38a1ec61-fa75-4e15-99fb-5be922652198.gif"><img width="50%" src="https://user-images.githubusercontent.com/66001046/144426072-cb044516-463a-4f84-97b7-318a1da973e2.gif">
