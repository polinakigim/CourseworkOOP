from typing import Any, Dict, List

import requests

from src.abstract_classes import Parser


class HH(Parser):
    def __init__(self, file_worker: str = "data/data.json") -> None:
        """Конструктор обьекта запроса инфо через API сервис"""

        self.__url: str = "https://api.hh.ru/vacancies"
        self.__headers: Dict[str, str] = {"User-Agent": "HH-User-Agent"}
        self.__params: Dict[str, Any] = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies: List[Dict[str, Any]] = []
        super().__init__(file_worker)

    def connect_to_api(
        self, url: str, headers: Dict[str, str], params: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Метод подключения к API"""
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def load_vacancies(self, keyword: str) -> List[Dict[str, Any]]:
        """Метод загрузки данных вакансий из API сервиса"""

        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = requests.get(
                self.__url, headers=self.__headers, params=self.__params
            )
            vacancies: List[Dict[str, Any]] = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

        return self.__vacancies
