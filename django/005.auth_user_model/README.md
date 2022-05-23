Dockerでデバック
===

* [ゼロから学ぶ Python](https://rinatz.github.io/python-book/)
    * [rinatz/python-book](https://github.com/rinatz/python-book/tree/master/docs)
    * [MkDocs](https://www.mkdocs.org/)
    * [MkDocsによるドキュメント作成](https://zenn.dev/mebiusbox/articles/81d977a72cee01)

### PyCharmでDjango
* [【Django】PyCharmでDjangoのコンテナ(Docker)開発環境をサクっと構築する](https://qiita.com/thim/items/82678e1cd59c925846b4)

### vsCodeでDjango
* [DockerでPython+Django環境を構築し、vsCodeでリモートデバッグ（Windows10） ](http://www.tmckn.com/wp/docker-python-django-vscode-windows10/)


dockerコマンド
---

ビルド + 実行
```
$ docker-compose up -d --build
```

停止
```
$ docker-compose down -v
```

全部消す
```
$ docker-compose down --rmi all --volumes
```

startproject
```
$ docker-compose run django django-admin.py startproject プロジェクト名 .
```

アプリ作成
```
$ docker-compose run django python3 manage.py startapp アプリ名
$ docker-compose exec django python3 manage.py startapp アプリ名
```

マイグレーション、マイグレイト
```
$ docker-compose run --rm django python3 manage.py makemigrations
$ docker-compose exec django python3 manage.py migrate --noinput
```

collectstatic
```
$ docker-compose exec django python3 manage.py collectstatic --no-input --clear
```

クリエイトユーザー
```
$ docker-compose exec django python3 manage.py createsuperuser
```

古いネットワークを取り除く
```
$ docker system prune -a
```

ターミナル(bash)に入る
```
$ docker exec -it django /bin/bash
$ docker-compose exec django bash
```

個別停止
```
$ docker stop django
```
