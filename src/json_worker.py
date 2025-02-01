import json
import os
from typing import Any, Dict, List

from src.abstract_classes import JSONWorkerABC
from src.vacancy_class import Vacancy


class JSONWorker(JSONWorkerABC):
    def __init__(self, file_saver: str = "data/data.json") -> None:
        self.__file_saver: str = file_saver

        # Ensure the file exists and contains a valid JSON list
        if not os.path.exists(self.__file_saver):
            with open(self.__file_saver, "w", encoding="utf-8") as file:
                json.dump([], file)

    def add_vacancy(self, vacancies: Vacancy) -> None:
        """Добавляет вакансию в JSON файл."""
        json_file_vacancies: List[Dict[str, Any]] = self._load_vacancies_from_file()

        dict_vacancy: Dict[str, Any] = {
            "name": vacancies.name,
            "url": vacancies.url,
            "salary": vacancies.salary,
            "address": vacancies.address,
        }

        if dict_vacancy not in json_file_vacancies:
            json_file_vacancies.append(dict_vacancy)

        self._save_vacancies_to_file(json_file_vacancies)

    def delete_vacancy(self, vacancies: Vacancy) -> None:
        """Удаляет вакансию из JSON файла."""
        json_file_vacancies: List[Dict[str, Any]] = self._load_vacancies_from_file()

        dict_vacancy: Dict[str, Any] = {
            "name": vacancies.name,
            "url": vacancies.url,
            "salary": vacancies.salary,
            "address": vacancies.address,
        }

        if dict_vacancy in json_file_vacancies:
            json_file_vacancies.remove(dict_vacancy)

        self._save_vacancies_to_file(json_file_vacancies)

    def get_vacancies(self) -> List[Dict[str, Any]]:
        """Метод получения всех вакансий из JSON файла."""
        return self._load_vacancies_from_file()

    def _load_vacancies_from_file(self) -> List[Dict[str, Any]]:
        """Частный метод для загрузки вакансий из файла JSON."""
        try:
            with open(self.__file_saver, "r", encoding="utf-8") as file:
                json_file_vacancies: Any = json.load(file)
                if not isinstance(json_file_vacancies, list):
                    return []
                return json_file_vacancies
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save_vacancies_to_file(self, vacancies: List[Dict[str, Any]]) -> None:
        """Частный метод для сохранения вакансий в JSON файл."""
        with open(self.__file_saver, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)
