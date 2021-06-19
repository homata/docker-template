Django
----

### 参考
* [docker-composeを利用した逆ジオコーディングAPIを作った際の記録](https://qiita.com/nc30mtd/items/d7baa8f45b7b1ee9d25c)
* [docker-composeを利用した逆ジオコーディングAPIを作った際の記録](https://qiita.com/nc30mtd/items/d7baa8f45b7b1ee9d25c)
* [DockerでDjangoの開発環境を再構築！！！！](https://qiita.com/nokonoko_1203/items/e345f899ac9ac700d6a8)

### 作業メモ

```
mkdir -p backend/containers/django
cd backend/containers/django
```

```
$ pipenv --python 3.8 install
$ pipenv shell
$ pipenv graph
$ pipenv install
```


```
django-admin startproject config .
python manage.py runserver localhost:8000
```


```
vi backend/containers/django/config/settings.py
vi backend/containers/django/.env
vi backend/containers/django/Dockerfile
```

ビルド
```
docker build . -t pipenv_sample
dockerにログイン
docker run -it pipenv_sample
python -V
pip list
Ctrl+Dでログアウト
```

postgresコンテナとの接続用shellスクリプト
```
vi backend/containers/django/entrypoint.sh
```

```
vi backend/containers/docker-compose.yml
```


```
docker-compose up -d --build
docker-compose down
一旦コンテナを停止・イメージを削除
docker-compose down -v

localhost:8000
```


コンテナには以下のコマンドでログイン  
docker exec -it <サービス名> bash

```
docker exec -it django bash
または
docker exec -it postgres bash

psql -U <YOUR_DB_USER> -d <YOUR_DB_NAME>
```


```
docker exec -it postgres bash
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
c$ docker-compose down -v
```


```
$ mkdir nginx
$ cd nginx/
$ touch Dockerfile
$ vi backend/containers/nginx/nginx.conf
```
