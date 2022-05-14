#!/usr/bin/python
# -*- coding: utf-8 -*-

# from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

import os
import json


"""
See Also
--------
ドキュメント
* pytest
    - https://docs.pytest.org/en/latest/
* pytest-django
    - https://pytest-django.readthedocs.io/en/latest/index.html

* Django Restframework のテストコードを作成する
    - https://qiita.com/shinno21/items/a42eea9b6ce959e106c0
    - https://github.com/shinno21/drf_sample

Notes
----------
テスト実行
```
$ python manage.py test
```
"""

def get_test_pathname(filename):
    """ get test data directory """
    basedir = os.path.dirname(os.path.abspath(__file__))
    datadir = os.path.join(basedir, "test_data")
    return os.path.join(datadir, filename)


class PostTests(APITestCase):
    """ Post のテスト """

    def setUp(self):
        """"各テストメソッド毎の前処理
        各テストに共通で必要な前準備を記述する
        """
        pass

    def tearDown(self):
        """各テストメソッド毎の後処理
        テストで使ったデータは毎回クリアされるので、テスト後のデータ削除はこちらに記述する必要はない
        """
        pass

    def test_post_reasult_200(self):
        """ post test normal end """
        # URL
        url = reverse('traffic_flows:traffic_flow_api', kwargs={})

        # jsonテストデータ
        pathname = get_test_pathname('json_style_pretty.json')
        json_data = json.load(open(pathname, 'r'))
        
        # POST
        response = self.client.post(url, json.dumps(json_data), content_type="application/json")
    
        # リターンステータスチェック
        assert response.status_code == status.HTTP_200_OK
