import unittest
from unittest.mock import MagicMock
from crud import charts_crud
from fastapi.testclient import TestClient
from fastapi import FastAPI, HTTPException
from unittest.mock import MagicMock
from main import app



class MyTestCase(unittest.TestCase):

    def get_db(self):
        """
        Fake 데이터 베이스
        :return:
        """
        # Create a fake database object
        db = MagicMock()
        # Add some test data
        items = [{"id": 1, "name": "Item 1"}]
        db.query.return_value.filter.return_value.first.side_effect = items
        return db

    def test_charts_crud(self):
        """
        차트 정보 불러오는 API 테스트
        현재 데이터 베이스에 있는 데이터를 불러오는지 확인
        :return: 모든 Fish_type
        history에 fish_type이 없을시 0으로 반환
        """
        # db = self.get_db()
        client = TestClient(app)

        response = client.get("http://0.0.0.0:8000/api/charts")
        assert response.status_code == 200
        assert response.json() ==  {'고등어': 0, '넙치': 5, '노랑 가오리': 11, '볼락': 3, '적색퉁돔': 5}


if __name__ == '__main__':
    unittest.main()
