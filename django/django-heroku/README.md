park-map
-----

みんなでつくる公園マップ(仮)

### Herokuの設定
* HerokuではPostgreSQLが利用可能(デフォルト？)
* hobby-devという無料のプランあり
* 10,000行、1GBという制限があり

#### Heroku公式
* [Language/SupportPython](https://devcenter.heroku.com/categories/python-support)
* [Django の使用(Working with Django)](https://devcenter.heroku.com/ja/categories/working-with-django)
* [Django と静的アセット(Django and Static Assets)](https://devcenter.heroku.com/ja/articles/django-assets)
* [Heroku の Python サポート(Specifying a Python version)](https://devcenter.heroku.com/articles/python-support#supported-runtimes)

#### Herokuへデプロイ
* [【Django】Herokuへデプロイしアプリを公開](https://chigusa-web.com/blog/django-heroku/)
* [【Heroku】PostgreSQLにローカルのクライアントから接続](https://chigusa-web.com/blog/heroku-postgresql/)

#### Django Girls
* [Django Girlsチュートリアルで Heroku へデプロイするときに躓いたこと -スタックに注意](https://qiita.com/yujimod/items/595a4ecba991b2e5ccd1)
* [Herokuにデプロイしよう（PythonAnywhereだけでなく）](https://tutorial-extensions.djangogirls.org/ja/heroku)

Herokuコマンド更新
```
$ heroku --version
$ heroku update
```
pipで追加インストールして「requirements.txt」を作成する
```
$ pip install django-heroku
$ pip install gunicorn
$ pip install whitenoise
$ pip freeze > requirements.txt
```
「Procfile」を作成する
```
<config.wsgi>はconfig/wsgi.pyを指定している
  echo "web: gunicorn config.wsgi --log-file -" > Procfile
```
Herokuにログイン
```
$ heroku login
```
[Heroku dashboard](https://dashboard.heroku.com/apps) にアプリを作成
```
$ heroku create
$ heroku create <name>
$ heroku create park-map
```

環境変数SECRET_KEYを設定
```
$ heroku config:set SECRET_KEY='django-hoge'
```

collectstatic が実行された環境に関する追加情報が必要な場合は、DEBUG_COLLECTSTATIC設定
```
$ heroku config:set DEBUG_COLLECTSTATIC=1
```

Herokuでビルド（Masterブランチで実行して、Herokuに転送）
```
$ git push heroku master
```

Herokuの環境をチェック
```
$ heroku run python manage.py check
```

Herokuのビルドエラーが発生した場合
```
collectstatic のビルドステップを無効化
$ heroku config:set DISABLE_COLLECTSTATIC=1

手動でcollectstatic を実行
$ heroku run python manage.py collectstatic --noinput

collectstatic のビルドステップを有効化
$ heroku config:set DISABLE_COLLECTSTATIC=0

staticfilesを表示
$ heroku run ls staticfiles
```

データベースをmigrate
```
$ heroku run python manage.py migrate
```

管理者ユーザ作成
```
$ heroku run python manage.py createsuperuser
```

アプリをブラウザーでアクセス
```
$ heroku open
https://xxxx.herokuapp.com/
https://xxxx.herokuapp.com/admin/
```

ログ表示
```
$ heroku logs --tail
```

Herokuのアプリを作り直したら登録先をremoteも消す
```
$ git remote -v
$ git remote rm heroku
```

##### PostGISの追加

[PostGISの追加](https://devcenter.heroku.com/ja/articles/heroku-postgres-extensions-postgis-full-text-search)

AddOnを追加
Heroku Postgres プラン(有償)
```
$ heroku addons:create heroku-postgresql:standard-0
```
Hobby プラン(無償)
```
$ heroku addons:create heroku-postgresql:hobby-dev
```

DATABASE_URLを取得
```
$ heroku config:get DATABASE_URL
postgres://aaaa:bbbb@cccc:5432/dddd
$ psql -h [host] -p [port] -U [user] -d [database]
$ psql -h cccc -p 5432 -U aaaa -d dddd
password -> bbbb
```

Extension追加
```
=> create extension postgis;
CREATE EXTENSION
=> SELECT postgis_version();
            postgis_version
---------------------------------------
 3.2 USE_GEOS=1 USE_PROJ=1 USE_STATS=1
(1 row)
=> \q
```
