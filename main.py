from src.functions.func_filter_vacancies import filter_vacancies
from src.functions.func_get_top_vacancies import get_top_vacancies
from src.functions.func_get_vacancies_by_salary import get_vacancies_by_salary
from src.functions.func_print_vacancies import print_vacancies
from src.hh_api import HH
from src.json_worker import JSONWorker
from src.vacancy_class import Vacancy


def get_search_query() -> str:
    search_query = input("Введите поисковый запрос: ").strip()
    if not search_query:
        print("Поисковый запрос не может быть пустым.")
        exit()
    return search_query


def get_top_n() -> int:
    while True:
        try:
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            if top_n <= 0:
                raise ValueError
            return top_n
        except ValueError:
            print("Введите корректное число больше 0.")


def get_filter_words() -> list:
    return input("Введите ключевые слова для фильтрации (через пробел): ").split()


def get_salary_range() -> str:
    return input("Введите диапазон зарплат (Пример: 100000 - 150000): ").strip()


def save_vacancies_to_json(vacancies: list) -> None:
    json_worker = JSONWorker()
    for vacancy in vacancies:
        json_worker.add_vacancy(Vacancy(**vacancy))
    print("\nВакансии успешно сохранены в JSON-файл!")


def user_interaction() -> None:
    hh_api = HH()
    search_query = get_search_query()
    hh_vacancies = hh_api.load_vacancies(search_query)

    if not hh_vacancies:
        print("По вашему запросу вакансий не найдено.")
        return

    Vacancy.cast_to_object_list(hh_vacancies)
    top_n = get_top_n()
    filter_words = get_filter_words()
    salary_range = get_salary_range()

    filtered_vacancies = filter_vacancies(Vacancy.all_list_vacancies(), filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    top_vacancies = get_top_vacancies(ranged_vacancies, top_n)

    print_vacancies(top_vacancies)
    save_vacancies_to_json(top_vacancies)


if __name__ == "__main__":
    user_interaction()
