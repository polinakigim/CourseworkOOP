from src.vacancy_class import Vacancy
from src.json_worker import JSONWorker


def filter_vacancies(vacancies_list: list, filter_words: list):
    """Функция фильтрует вакансии по ключевым словам"""
    filtered_vacancies = []

    for vacancy in vacancies_list:
        for word in filter_words:
            name = vacancy.get("name", "")
            address = vacancy.get("address", "")

            if not isinstance(name, str):
                name = ""
            if not isinstance(address, str):
                address = ""

            if word.lower() in name.lower() or word.lower() in address.lower():
                filtered_vacancies.append(vacancy)
                break

    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Функция сортирует вакансии по вилке зарплаты (от и до)"""
    filtered_salary_vacancies = []
    from_to_salary = salary_range.split()

    try:
        min_salary = int(from_to_salary[0])
        max_salary = int(from_to_salary[2])
    except (IndexError, ValueError):
        print("Некорректный ввод диапазона зарплат. Пример: '100000 - 150000'")
        return []

    for vacancy in filtered_vacancies:
        salary = vacancy.get("salary", {})
        salary_from = salary.get("from")
        salary_to = salary.get("to")

        if salary_from is not None and salary_to is not None:
            try:
                salary_from = int(salary_from)
                salary_to = int(salary_to)
            except ValueError:
                continue

            if salary_from >= min_salary and salary_to <= max_salary:
                filtered_salary_vacancies.append(vacancy)
        else:
            continue

    return sorted(
        filtered_salary_vacancies,
        key=lambda x: x["salary"].get("to", 0),
        reverse=True
    )


def get_top_vacancies(filtered_vacancies, top_n):
    """Функция вывода топ вакансий по выбору пользователя"""
    filtered_vacancies = filtered_vacancies[0: top_n]
    return filtered_vacancies


def print_vacancies(vacancies):
    """Функция вывода отфильтрованных вакансий в консоль"""
    return print(vacancies)

