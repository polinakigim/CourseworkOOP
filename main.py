from src.vacancy_class import Vacancy
from src.hh_api import HH
from src.functions.func_filter_vacancies import filter_vacancies
from src.functions.func_get_vacancies_by_salary import get_vacancies_by_salary
from src.functions.func_get_top_vacancies import get_top_vacancies
from src.json_worker import JSONWorker


def format_vacancy(vacancy: dict) -> str:
    """Форматирует вакансию в человекочитаемый вид."""
    return (
        f" Название: {vacancy.get('name', 'Не указано')}\n"
        f" Ссылка: {vacancy.get('url', 'Не указано')}\n"
        f" Зарплата: {vacancy.get('salary', {}).get('from', 'Не указано')} - "
        f"{vacancy.get('salary', {}).get('to', 'Не указано')} руб.\n"
        f" Адрес: {vacancy.get('address', 'Не указан')}\n"
        "----------------------------------------"
    )


def print_vacancies(vacancies: list) -> None:
    """Выводит вакансии в удобочитаемом формате."""
    if not vacancies:
        print(" Вакансии не найдены.")
        return

    print("\nНайденные вакансии:")
    for vacancy in vacancies:
        print(format_vacancy(vacancy))


def user_interaction() -> None:
    """Функция взаимодействия с пользователем."""
    hh_api = HH()

    # Ввод поискового запроса
    search_query = input("Введите поисковый запрос: ").strip()
    if not search_query:
        print("Поисковый запрос не может быть пустым.")
        return

    hh_vacancies = hh_api.load_vacancies(search_query)
    if not hh_vacancies:
        print("По вашему запросу вакансий не найдено.")
        return

    Vacancy.cast_to_object_list(hh_vacancies)

    # Ввод количества вакансий в топе
    while True:
        try:
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            if top_n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Введите корректное число больше 0.")

    # Ввод ключевых слов для фильтрации
    filter_words = input(
        "Введите ключевые слова для фильтрации (через пробел): "
    ).split()

    # Ввод диапазона зарплат
    salary_range = input("Введите диапазон зарплат (Пример: 100000 - 150000): ").strip()

    # Фильтрация вакансий
    filtered_vacancies = filter_vacancies(Vacancy.all_list_vacancies(), filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    top_vacancies = get_top_vacancies(ranged_vacancies, top_n)

    # Вывод вакансий
    print_vacancies(top_vacancies)

    # Работа с JSON
    json_worker = JSONWorker()

    for vacancy in top_vacancies:
        vacancy_obj = Vacancy(
            name=vacancy["name"],
            url=vacancy["url"],
            salary=vacancy["salary"],
            address=vacancy["address"],
        )
        json_worker.add_vacancy(vacancy_obj)

    print("\nВакансии успешно сохранены в JSON-файл!")


if __name__ == "__main__":
    user_interaction()
