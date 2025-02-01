from typing import Any, Dict, List, Union


class Vacancy:
    __list_vacancies: List[Dict[str, Any]] = []
    __slots__ = ("name", "url", "salary", "address")

    def __init__(
        self, name: str, url: str, salary: Dict[str, int], address: str
    ) -> None:
        """
        Класс для представления вакансии.
        """
        self.name: str = name
        self.url: str = url
        self.salary: Dict[str, int] = salary
        self.address: str = address

        dict_vacancy: Dict[str, Any] = {
            "name": self.name,
            "url": self.url,
            "salary": self.salary,
            "address": self.address,
        }
        self.__list_vacancies.append(dict_vacancy)

    @classmethod
    def all_list_vacancies(cls) -> List[Dict[str, Any]]:
        """Метод для получения всех вакансий."""
        return cls.__list_vacancies

    @classmethod
    def clear_list(cls) -> None:
        """Метод для очистки списка вакансий."""
        cls.__list_vacancies = []

    @staticmethod
    def __validate(salary: Union[None, str, Dict[str, int]]) -> Dict[str, int]:
        """Метод валидации зарплаты."""
        if salary is None:
            return {"from": 0, "to": 0}
        if isinstance(salary, str):
            try:
                from_salary, to_salary = map(int, salary.split(" - "))
                return {"from": from_salary, "to": to_salary}
            except ValueError:
                return {"from": 0, "to": 0}
        elif isinstance(salary, dict):
            from_salary: int = salary.get("from", 0)
            to_salary: int = salary.get("to", 0)
            return {"from": from_salary, "to": to_salary}
        return {"from": 0, "to": 0}

    @classmethod
    def cast_to_object_list(
        cls, list_vacancies: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Метод добавления вакансий из списка вакансий."""
        for vacancy_data in list_vacancies:
            salary: Dict[str, int] = cls.__validate(vacancy_data.get("salary"))

            address: str = vacancy_data.get("address", "Не указан")
            if isinstance(address, dict):
                address = address.get("address", "")

            cls(
                name=vacancy_data.get("name", "Не указан"),
                url=vacancy_data.get("url", "Не указан"),
                salary=salary,
                address=vacancy_data.get("address", "Не указан"),
            )
        return cls.__list_vacancies

    def __ge__(self, other: "Vacancy") -> bool:
        """Метод сравнения вакансий по максимальной зарплате."""
        self_salary_to: int = self.salary.get("to", 0)
        other_salary_to: int = other.salary.get("to", 0)
        return self_salary_to >= other_salary_to

    @classmethod
    def filtered_salary(
        cls, from_salary: int = 0, to_salary: int = float("inf")
    ) -> None:
        """Метод фильтрации вакансий по зарплате (от и до вилка)."""
        for vacancy in cls.__list_vacancies:
            salary_from: int = vacancy["salary"].get("from", 0)
            salary_to: int = vacancy["salary"].get("to", 0)
            if salary_from >= from_salary and salary_to <= to_salary:
                print(vacancy)
