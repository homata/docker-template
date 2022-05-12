PostGIS
----

* [dockerでPostGISを入れたPostgreSQL環境構築](https://qiita.com/A-Kira/items/3339e902e7a8fca8fdf6)


起動(デーモン)
```
$ docker-compose up -d
$ docker ps -a
```

終了
```
$ docker-compose down
```

初期化
```
$ ./init-db.sh
```

シェル接続
```
$ docker-compose exec db bash
```
