from abc import ABC, abstractmethod
from src.vacancy_class import Vacancy


class Parser(ABC):

    @abstractmethod
    def __init__(self, file_worker):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        """Метод загрузки вакансий по ключевому слову"""
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class JSONWorkerABC(ABC):
    @abstractmethod
    def add_vacancy(self: object, vacancies: Vacancy) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self: object, vacancies: Vacancy) -> None:
        pass
