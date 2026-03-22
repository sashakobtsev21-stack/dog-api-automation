class TestDogApi:
    def test_list_breeds(self, dog_api):
        response = dog_api.get_all_breeds()
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_search_golden_retriever(self, dog_api):
        response = dog_api.search_breed("golden")
        data = response.json()
        assert response.status_code == 200
        assert "Golden" in data[0]["name"]

    def test_auth_error(self, dog_api):
        response = dog_api.get_with_wrong_key()
        # ИСПРАВЛЕНО: Dog API возвращает 401 на неверный ключ
        assert response.status_code == 403