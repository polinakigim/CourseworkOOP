from src.abstract_classes import Parser
import requests


class HH(Parser):
    def __init__(self, file_worker: str = "data/data.json"):
        """Конструктор обьекта запроса инфо через API сервис"""

        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = (
            []
        )  # конечный список, в который складываются вакансии list[dict]
        super().__init__(file_worker)

    def connect_to_api(self, url, headers, params):
        """Метод подключения к API"""
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def load_vacancies(self, keyword: str):
        """Метод загрузки данных вакансий из API сервиса"""

        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = requests.get(
                self.__url, headers=self.__headers, params=self.__params
            )
            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

        return self.__vacancies
