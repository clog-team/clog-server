### [SW 중심대학 공동해커톤] Movie-it

![image](https://user-images.githubusercontent.com/55101567/107108115-03433600-6879-11eb-8118-022498348fc1.png)

# Movie-it

__Let's movie it!__ 
__같이 영화보자!__ 


코로나로 인해 모든게 비대면으로 전환되면서
자연스럽게 사람들과의 소통도 줄어들었습니다.


반대로, 온라인 활동이 늘고 컨텐츠 소비가 늘어났죠
소통의 단절로 우울증, 외로움을 느끼는 사람들이 늘어나고 있습니다.


따라서
__우리가 본 컨텐츠를 바탕으로 소통할 거리를 늘려보자!__
라는 목표로 만들었습니다.


__<친구들과 영화에 관한 얘기를 나눌수 있는 앱, 무빗>__


내가 본 영화 평점을 매겨 기록할 수 있습니다.  
또한, 친구들이 이 영화를 봤을 때 몇 점을 줄 지 예측해 볼 수 있습니다!


__당신은 친구를 얼마나 잘 알고 있나요?__


__과연 당신과 친구는 "영혼의 단짝"일까요?__


__친구들이 본 영화는 나에게 추천되니, 더 이상 넷플릭스병은 그만🙅‍♀️__


__이 시국에도 함께 영화보기👌__


__오늘 밤은 친구들과 함께 영화토론, 어떠세요?😀__

## Running the server locally
1. Clone this repository.
```terminal
$ git clone https://github.com/movie-it/movieit-server.git
```
2. Add `credentials.json`.

:bulb: for team members, check out the team slack channel.
```json
{
  "SECRET_KEY": "PROJECT_SECRET_KEY",
  "MOVIE_API_KEY": "MOVIE_API_KEY",
  "MOVIE_DETAIL_API_KEY": "MOVIE_DETAIL_API_KEY",
  "NAVER_CLIENT_ID": "NAVER_CLIENT_ID",
  "NAVER_CLIENT_SECRET": "NAVER_CLIENT_SECRET"
}
```
3. Create and activate the virtual environment.
```terminal
$ pip install pipenv
$ pipenv shell
```
4. Install the requirements.
```terminal
$ pip install -r requirements.txt
```
5. Create the database.
```terminal
$ python manage.py migrate
```
6. Run the development server.
```terminal
$ python manage.py runserver
```

The project will be available at **localhost:8000/**
