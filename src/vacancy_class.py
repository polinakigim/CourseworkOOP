class Vacancy:
    __list_vacancies: list = []
    __slots__ = ("name", "url", "salary", "address")

    def __init__(self, name, url, salary, address):
        """

        :type salary: object
        """
        self.name = name
        self.url = url
        self.salary = salary
        self.address = address

        dict_vacancy = {
            "name": self.name,
            "url": self.url,
            "salary": self.salary,
            "address": self.address
        }
        self.__list_vacancies.append(dict_vacancy)

    @classmethod
    def all_list_vacancies(cls):
        """Метод для получения всех вакансий"""
        return cls.__list_vacancies

    @classmethod
    def clear_list(cls):
        cls.__list_vacancies = []

    @staticmethod
    def __validate(salary):
        if salary is None:
            return {"from": 0, "to": 0}
        if isinstance(salary, str):
            try:
                from_salary, to_salary = map(int, salary.split(" - "))
                return {"from": from_salary, "to": to_salary}
            except ValueError:
                return {"from": 0, "to": 0}
        elif isinstance(salary, dict):
            from_salary = salary.get('from', 0)
            to_salary = salary.get('to', 0)
            return {"from": from_salary, "to": to_salary}
        else:
            return {"from": 0, "to": 0}

    @classmethod
    def cast_to_object_list(cls, list_vacancies):
        """Метод добавления вакансий из списка вакансий"""
        for vacancy_data in list_vacancies:

            salary = cls.__validate(vacancy_data.get("salary"))

            address = vacancy_data.get("address", "Не указан")
            if isinstance(address, dict):
                address = address.get("city", "")

            cls(
                name=vacancy_data.get("name", "Не указан"),
                url=vacancy_data.get("url", "Не указан"),
                salary=salary,
                address=vacancy_data.get("address", "Не указан"),
            )
        return cls.__list_vacancies

    def __ge__(self, other):
        self_salary_to = self.salary.get("to", 0)
        other_salary_to = other.__salary.get("to", 0)
        return self_salary_to >= other_salary_to

    @classmethod
    def filtered_salary(cls, from_salary: int = 0, to_salary: int = float("inf")):
        """Метод фильтрации вакансий по зарплате (от и до вилка)"""
        for vacancies in cls.__list_vacancies:
            if vacancies["salary"].get("from", 0) >= from_salary and vacancies["salary"]["to"] <= to_salary:
                print(vacancies)


if __name__ == "__main__":
    Vacancy.clear_list()
vacancy_data_list = [
    {
        "name": "Frontend Developer",
        "url": "https://hh.ru/vacancy/111222",
        "salary": "80000 - 120000",
        "address": "Saint Petersburg"
    },
    {
        "name": "Data Scientist",
        "url": "https://hh.ru/vacancy/333444",
        "salary": "120000 - 180000",
        "address": "Novosibirsk"
    },
    {
        "name": "QA Engineer",
        "url": "https://hh.ru/vacancy/555666",
        "salary": "60000 - 90000",
        "address": "Vladivostok"
    },
    {
        "name": "Project Manager",
        "url": "https://hh.ru/vacancy/777888",
        "salary": "110000 - 160000",
        "address": "Moscow"
    },
    {
        "name": "DevOps Engineer",
        "url": "https://hh.ru/vacancy/999000",
        "salary": "130000 - 190000",
        "address": "Yekaterinburg"
    }
]

Vacancy.cast_to_object_list(vacancy_data_list)
Vacancy.filtered_salary(0, 140000)
print(Vacancy.all_list_vacancies())
