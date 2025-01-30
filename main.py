from src.vacancy_class import Vacancy
from src.hh_api import HH
from src.functions import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, print_vacancies
from src.json_worker import JSONWorker

def user_interaction():
    platforms = HH()

    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = platforms.load_vacancies(search_query)

    vacancies_add_list = Vacancy.cast_to_object_list(hh_vacancies)
    vacancies_list = Vacancy.all_list_vacancies()

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    #  Функция фильтрации вакансий по ключевым словам
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    #  Функция сортировки вакансий (вывод топ № вакансий)
    top_vacancies = get_top_vacancies(ranged_vacancies, top_n)

    #  Функция вывода вакансий в консоль
    print_vacancies(top_vacancies)

    # Пример работы контструктора класса с одной вакансией
    vacancy = Vacancy(
        "Python Developer",
        "<https://hh.ru/vacancy/123456>",
        "100 000-150 000 руб.",
        "Минск",
    )

    json_worker = JSONWorker()
    json_worker.add_vacancy(vacancy)
    json_worker.delete_vacancy(vacancy)

    for filtered_vacancy in [tuple(d.values()) for d in top_vacancies]:
        vacancy_obj = Vacancy(*filtered_vacancy)
        json_worker.add_vacancy(vacancy_obj)


if __name__ == "__main__":
    user_interaction()