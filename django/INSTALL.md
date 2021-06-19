Django
----

### 参考
* [docker-composeを利用した逆ジオコーディングAPIを作った際の記録](https://qiita.com/nc30mtd/items/d7baa8f45b7b1ee9d25c)
* [docker-composeを利用した逆ジオコーディングAPIを作った際の記録](https://qiita.com/nc30mtd/items/d7baa8f45b7b1ee9d25c)
* [DockerでDjangoの開発環境を再構築！！！！](https://qiita.com/nokonoko_1203/items/e345f899ac9ac700d6a8)
    * [DockerでDjangoの開発環境を構築！（Docker-compose/Django/postgreSQL/nginx）](https://qiita.com/nokonoko_1203/items/242367a83c313a5e46bf)
* [Docker入門（第六回）〜Docker Compose〜](https://knowledge.sakura.ad.jp/16862/)

### Memo

```
$ mkdir -p backend/containers/django
$ cd backend/containers/django
```

pipenv directory
```
$ export PIPENV_VENV_IN_PROJECT=true
```

```
$ pipenv --python 3.8 install
$ pipenv shell
$ pipenv graph
$ pipenv install
$ pipenv sync
$ pip list
```

Django
```
$ django-admin startproject config .
$ python manage.py runserver localhost:8000
```

```
$ vi backend/containers/django/config/settings.py
$ vi backend/containers/django/.env
$ vi backend/containers/django/Dockerfile
```

build
```
$ docker-compose build
$ docker-compose build --no-cache
$ docker-compose ps
```

build
```
$ docker build . -t pipenv_sample
```

docker login
```
$ docker run -it pipenv_sample
$ python -V
$ pip list
Ctrl+Dでログアウト
```

postgresコンテナとの接続用shellスクリプト
```
$ vi backend/containers/django/entrypoint.sh
```

```
$ vi backend/containers/docker-compose.yml
```

Docker起動＆構築
```
$ docker-compose up -d --build
```

一旦コンテナを停止・イメージを削除
```
$ docker-compose down -v
http://localhost:8000
```

コンテナには以下のコマンドでログイン
```
docker exec -it <サービス名> bash
```

```
$ docker exec -it django bash
 または
$ docker exec -it postgres bash

$ psql -U <YOUR_DB_USER> -d <YOUR_DB_NAME>
```

migrate
```
$ docker-compose exec django bash
$ python3 manage.py migrate
```

```
$ docker exec -it postgres bash

# psql -U app -d app
psql (11.2 (Debian 11.2-1.pgdg90+1))
"help" でヘルプを表示します。

app=# SELECT postgis_version();
            postgis_version
---------------------------------------
 2.5 USE_GEOS=1 USE_PROJ=1 USE_STATS=1
(1 行)

app=#
```

```
$ docker-compose down -v
```

```
$ mkdir nginx
$ cd nginx/
$ touch Dockerfile
$ vi backend/containers/nginx/nginx.conf
``

### Debug

#### PyCharm
* [【Django】PyCharmでDjangoのコンテナ(Docker)開発環境をサクっと構築する](https://qiita.com/thim/items/82678e1cd59c925846b4)

#### VSCode
* [DockerでPythonの開発環境を作成してみる　その1](https://ittech-nsnl.hatenablog.com/entry/2019/11/12/233136)
* [DockerでPythonの開発環境を作成してみる　その2](https://ittech-nsnl.hatenablog.com/entry/2019/11/20/233219)

