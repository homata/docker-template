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
* [ぼく「Djangoのリモートデバッグも出来ないエディターなんて…」VSCode「それ、できるで。」~docker-compose編~](https://qiita.com/nokonoko_1203/items/33a05c86f359027afb33)

"""
Remote-Containers: Add Development Container configuration Files...
From 'docker-compose.yml
デバックしたいサービスを選択(今回はDjango)
.devcontainerディレクトリと、その中にdevcontainer.json及びdocker-compose.ymlが出来る
Remote-Containers: Open Folder in Containers...
.devcontainerが存在するディレクトリ（今回の例ではcontainers）を選択
Remote-Containers: Attach to Running Containers...
Docker Debug ins Container
"""

##### 保留
* [DockerでPythonの開発環境を作成してみる　その1](https://ittech-nsnl.hatenablog.com/entry/2019/11/12/233136)
    * [DockerでPythonの開発環境を作成してみる　その2](https://ittech-nsnl.hatenablog.com/entry/2019/11/20/233219)
* [docker-composeで作成したDjango環境をVS Codeでリモートデバッグする](https://qiita.com/makiuchiatisols/items/ddc6cf8fb16968ac8bf3)




##### 注意
* デバック用にdocker-compose-debug.ymlを起動する
    - 通常のdocker-compose.ymlで終了させておく (コンテナを立ち上げている場合は一旦停止させてる)
    - デバッグ用のコンテナを立ちあげるので、元々のymlファイルが同じものを使っていると名前が競合する

### docker-compose

bash シェル
```
$ docker-compose exec django bash
```

マイグレーション
```
$ docker-compose run django python3 manage.py makemigrations
$ docker-compose run django python3 manage.py migrate
```
管理者作成
```
$ docker-compose run django python3 manage.py createsuperuser
```


### docker-memo

```
docker-compose logs -f
docker-compose logs -f django
```




Docker+Django
----

* [Pipenvを使ったPython開発まとめ](https://qiita.com/y-tsutsu/items/54c10e0b2c6b565c887a)

```
$ pipenv --python 3.8 install
$ pipenv shell
$ pipenv install
```

```
$ django-admin startproject config .
$ python manage.py runserver localhost:8000
```

```
$ docker-compose build --no-cache
$ docker-compose up -d --build
$ docker-compose down -v
$ psql -U app -d app
$ docker-compose down -v

### docker-compose

bash シェル
```
$ docker-compose exec django bash
```

マイグレーション
```
$ docker-compose run django python3 manage.py makemigrations
$ docker-compose run django python3 manage.py migrate
```
管理者作成
```
$ docker-compose run django python3 manage.py createsuperuser
```

### docker-memo
```
docker-compose logs -f
docker-compose logs -f django
```

pipenv install --dev autopep8 flake8

pipenv shell
pipenv install geopandas
pipenv install GeoAlchemy2
pipenv install workdays
pipenv install python-decouple
pipenv install jupyterlab


バージョン確認してインストール
---
$ gdal-config --version
3.0.4
$ export CPLUS_INCLUDE_PATH=/usr/include/gdal
$ export C_INCLUDE_PATH=/usr/include/gdal
$ pipenv run pip3 install GDAL==3.0.4
$ pipenv run pip3 install Rtree

(app) #  pipenv run pip3 install Rtree
Requirement already satisfied: Rtree in ./.venv/lib/python3.8/site-packages (0.9.7)
(app) # pipenv run pip3 install GDAL==3.0.4
Requirement already satisfied: GDAL==3.0.4 in ./.venv/lib/python3.8/site-packages (3.0.4)
