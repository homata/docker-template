DockerでDjango環境を作成
----
* 001.base: 基本のベース
* 002.debug: デバック(runserver)で起動
* 003.prod: 本番と開発モードを準備
* 004.postgis: PostGISの環境

### 参考
* [DockerでDjangoローカル開発環境を爆速構築](https://michinoku-se.org/docker-django/)
* [【Python+Django4】VS Code+Dockerで簡単構築【リモート開発】【Win/Mac】](https://chigusa-web.com/blog/django-vscode-docker/)


### @nokonoko_1203(MIERUNE)
* [DockerでDjangoの開発環境を再構築！！！！](https://qiita.com/nokonoko_1203/items/e345f899ac9ac700d6a8)
* [市区町村名・緯度経度から平面直角座標系の系番号を取得するツールを作成した！](https://qiita.com/nokonoko_1203/items/f8925081665cab3f36f0)
* [モダンな技術で手軽に地図アプリを始めてみよう！！！（Next.js/TypeScript/Tailwind CSS/maplibre GL JS/Deck.gl）](https://qiita.com/nokonoko_1203/items/161a29d33d265a39016b)
* [ぼく「Djangoのリモートデバッグも出来ないエディターなんて…」VSCode「それ、できるで。」~docker-compose編~](https://qiita.com/nokonoko_1203/items/33a05c86f359027afb33)


### 実行コマンド

プロジェクト作成
```
mkdir `project名`
cd `project名`
django-admin startproject config .
```

プロジェクト作成（Docker経由)
```
$ docker-compose run web django-admin startproject config .
$ docker-compose run django django-admin startproject config .
```

コンテナの停止: -vオプションはボリュームの削除を表します
```
$ docker-compose down -v
```

コンテナの起動 & ビルド
```
$ docker-compose up -d --build
```

マイグレーション
```
<!-- $ docker-compose exec <service_name> python manage.py migrate --noinput -->
$  docker-compose exec django python manage.py migrate --noinput
```

psql接続
```
$ docker-compose exec postgres psql --username=django_db_user --dbname=django_db
```

コンテナの起動 & ビルド: ファイル指定
```
<!-- -fオプションでdocker-compose.prod.ymlを指定 -->
$ docker-compose -f docker-compose.prod.yml up -d --build
```

マイグレーション: ファイル指定
```
<!-- entrypoint.prod.shではmigrateをしていないので手動で実行 -->
$ docker-compose -f docker-compose.prod.yml exec django python manage.py migrate --noinput
```

起動サービス確認
```
$ docker ps$ docker-compose -f docker-compose.prod.yml ps --service 
```

bash起動
```
$ docker-compose exec django /bin/bash
$ docker-compose -f docker-compose.prod.yml exec django /bin/bash

$ docker exec -it コンテナ名 /bin/bash
```

ビルド -> migrate  -> collectstatic (ファイル指定)
```
$ docker-compose -f docker-compose.prod.yml down -v
$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml exec djnago python manage.py migrate --noinput
$ docker-compose -f docker-compose.prod.yml exec django python manage.py collectstatic --no-input --clear
```

ビルド -> migrate -> collectstatic (python3の場合)
```
$ docker-compose down -v
$ docker-compose up -d --build
$ docker-compose exec django python3 manage.py migrate --noinput
$ docker-compose exec django python3 manage.py collectstatic --no-input --clear
```
