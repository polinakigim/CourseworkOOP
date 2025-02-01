from abc import ABC, abstractmethod
from typing import Any, Dict, List

from src.vacancy_class import Vacancy


class Parser(ABC):

    @abstractmethod
    def __init__(self, file_worker: str) -> None:
        pass

    @abstractmethod
    def load_vacancies(self, keyword: str) -> List[Dict[str, Any]]:
        """Метод загрузки вакансий по ключевому слову"""
        pass

    @abstractmethod
    def connect_to_api(self, keyword: str) -> Dict[str, Any]:
        pass


class JSONWorkerABC(ABC):
    @abstractmethod
    def add_vacancy(self, vacancies: Vacancy) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancies: Vacancy) -> None:
        pass
