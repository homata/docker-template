Dockerでデバック
===

* [ゼロから学ぶ Python](https://rinatz.github.io/python-book/)
    * [rinatz/python-book](https://github.com/rinatz/python-book/tree/master/docs)
    * [MkDocs](https://www.mkdocs.org/)
    * [MkDocsによるドキュメント作成](https://zenn.dev/mebiusbox/articles/81d977a72cee01)

### PyCharmでDjango
* [【Django】PyCharmでDjangoのコンテナ(Docker)開発環境をサクっと構築する]()

### vsCodeでDjango
* [DockerでPython+Django環境を構築し、vsCodeでリモートデバッグ（Windows10） ](http://www.tmckn.com/wp/docker-python-django-vscode-windows10/)

ビルド -> migrate -> collectstatic (python3の場合)
```
$ docker-compose down -v
$ docker-compose up -d --build
$ docker-compose exec django python3 manage.py migrate --noinput
$ docker-compose exec django python3 manage.py collectstatic --no-input --clear

$ docker-compose exec django python3 manage.py createsuperuser

```
