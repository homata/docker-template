redis
-----

* [Redisの紹介](https://www.sraoss.co.jp/tech-blog/redis/redis-introduction/)
* [Redisのデータ永続化](https://www.sraoss.co.jp/tech-blog/redis/redis-persistdata/)
* [システム開発で得たRedis利用ノウハウ](https://future-architect.github.io/articles/20190821/)

* [【入門】Redis](https://qiita.com/wind-up-bird/items/f2d41d08e86789322c71)
* [Redisの特徴と活用方法について ](https://www.slideshare.net/yujiotani16/redis-76504393)
* [Redis入門 : 概要と特徴について](https://weblabo.oscasierra.net/redis-beginning/)

### Django Redis

* [Djangoで非同期処理を実装する方法（Celery、Redis）Macローカル編](https://dot-blog.jp/news/django-async-celery-redis-mac/)

    $ pip install celery
    $ pip install django-celery-results
    $ pip install redis
    $ pip install django-redis
    $ pip install django-celery-beat


### docker-compose

* [docker-composeでredisを起動して接続する](https://katsu-tech.hatenablog.com/entry/2017/10/11/233024)

# -d をつけるとバックグラウンドで起動
$ docker-compose up -d

# 終了
$ docker-compose down

# 起動していることを確認
$ docker-compose ps

# コマンドから接続
redis-cli
127.0.0.1:6379> 

# bash
docker exec -it d6b7ea3a59e7 bash


redis-celery
---

* [Python で分散タスクキュー (RQ 編)](https://qiita.com/hoto17296/items/39597f6e26c0186a6e1b)
* [【Python】非同期タスクの実行環境+モニタリング環境を作る](https://qiita.com/xecus/items/9722b287cc6aee4083ae)
* [【Celery】Celery タスクの追加とflower編](http://dnond.hatenablog.com/entry/2013/07/31/221130)
* [【Celery】Celery 要件と環境編](http://dnond.hatenablog.com/entry/2013/07/31/211121)

* ブローカー（broker）仲介
    - 仲買人。仲介業者。 
* エージェント（agent) 代理
    - 当事者に代わって物事を処理したり，意思表示をしたりする者。代理人。代行人。代理店。代理業者。 
    - コンピューターのユーザーが連続した操作をしなくても，自律的に情報収集や状況判断を行い，適切な処理動作を実行する機能。また，そのソフト-ウエア。 
* プロデューサー (Producer)
    - 映画・演劇・放送などで，制作責任者。作品の企画から完成までの一切を統轄する。 

エージェントとは、代理人や代理店等の事である。一方ブローカーとは、物の売り買いを仲介する仲立人の事である。

Celery -> キューシステム
redis -> インメモリデータベース -> BROKERというキューを保持する入れ物
flower -> キューの為のGUI環境

$ apt-get install redis-server
$ pip install celery
$ pip install flower
$ pip install redis

$ pip freezes
    celery==4.3.0
    django-celery-beat==1.5.0
    django-celery-results==1.1.2

    django-redis==4.10.0
    redis==3.3.11

    flower==0.9.3

$ sudo service redis-server start
$ ps aux | grep redis
    redis    15839  0.0  0.0  38852  3252 ?        Ssl  03:43   0:00 /usr/bin/redis-server 127.0.0.1:6379
    ubuntu   16694  0.0  0.0  12940  1000 pts/0    S+   03:46   0:00 grep --color=auto redis


main.py

    import tasks

    print('<first task>')

    # ここでタスク起動　(runタスク)
    worker = tasks.run.delay()
    # 終わらぬなら終わるまで待とうホトトギス
    while not worker.ready():
        pass
    #　返り値をだす
    print(worker.result)

    print('<second task>')
    
    # ここでタスク起動　(calcタスク)
    worker = tasks.calc.delay(100, 200)
    # 終わらぬなら終わるまで待とうホトトギス
    while not worker.ready():
        pass

    #　返り値をだす
    print(worker.result)

tasks.py

    import time
    from celery.decorators import task

    @task
    def run():
        time.sleep(10)
        print('処理　おわた')
        return 'おわったよ'


    @task
    def calc(a, b):
        return a+b

celeryconfig.py

    BROKER_URL = 'redis://localhost/0'
    CELERYD_CONCURRENCY = 1
    CELERY_RESULT_BACKEND = 'redis'
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_RESULT_BACKEND = "redis"
    CELERYD_LOG_FILE = "./celeryd.log"
    CELERYD_LOG_LEVEL = "INFO"
    CELERY_IMPORTS = ("tasks", )



$ celery flower --broker=redis://localhost:6379/0 --port=5555