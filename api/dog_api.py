from api.base_api import BaseAPI

class DogApi(BaseAPI):
    def get_all_breeds(self):
        return self.get("/breeds")

    def search_breed(self, breed_name):
        return self.get("/breeds/search", params={"q": breed_name})

    def get_with_wrong_key(self):
        return self.get("/breeds", headers={"x-api-key": "WRONG_KEY"})