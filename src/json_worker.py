from src.abstract_classes import JSONWorkerABC
from src.vacancy_class import Vacancy
import json
import os


class JSONWorker(JSONWorkerABC):

    def __init__(self, file_saver: str = "data/data.json"):
        self.__file_saver = file_saver

        # Ensure the file exists and contains a valid JSON list
        if not os.path.exists(self.__file_saver):
            with open(self.__file_saver, "w", encoding="utf-8") as file:
                json.dump([], file)

    def add_vacancy(self, vacancies: Vacancy):
        """Добавляет вакансию в JSON файл."""
        with open(self.__file_saver, "r", encoding="utf-8") as file:
            try:
                json_file_vacancies = json.load(file)
                if not isinstance(json_file_vacancies, list):
                    json_file_vacancies = []
            except json.JSONDecodeError:
                json_file_vacancies = []

        dict_vacancy = {
            "name": vacancies.name,
            "url": vacancies.url,
            "salary": vacancies.salary,
            "address": vacancies.address,
        }

        if dict_vacancy not in json_file_vacancies:
            json_file_vacancies.append(dict_vacancy)

        with open(self.__file_saver, "w", encoding="utf-8") as file:
            json.dump(json_file_vacancies, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancies: Vacancy):
        """Удаляет вакансию из JSON файла."""
        with open(self.__file_saver, "r", encoding="utf-8") as file:
            try:
                json_file_vacancies = json.load(file)
                if not isinstance(json_file_vacancies, list):
                    json_file_vacancies = []
            except json.JSONDecodeError:
                json_file_vacancies = []

        dict_vacancy = {
            "name": vacancies.name,
            "url": vacancies.url,
            "salary": vacancies.salary,
            "address": vacancies.address,
        }

        if dict_vacancy in json_file_vacancies:
            json_file_vacancies.remove(dict_vacancy)

        with open(self.__file_saver, "w", encoding="utf-8") as file:
            json.dump(json_file_vacancies, file, ensure_ascii=False, indent=4)
