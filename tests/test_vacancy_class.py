import pytest
from src.vacancy_class import Vacancy


@pytest.fixture
def sample_vacancies():
    """Фикстура для тестирования вакансий"""
    Vacancy.clear_list()  # Очищаем перед тестами, чтобы избежать влияния предыдущих тестов
    return [
        {"name": "Python Developer", "url": "https://example.com/python-dev", "salary": {"from": 120000, "to": 150000}, "address": "Moscow"},
        {"name": "Data Scientist", "url": "https://example.com/data-scientist", "salary": {"from": 100000, "to": 130000}, "address": "Saint Petersburg"},
        {"name": "Java Developer", "url": "https://example.com/java-dev", "salary": {"from": 90000, "to": 110000}, "address": "Moscow"},
    ]


def test_vacancy_constructor():
    """Проверяем создание экземпляра Vacancy"""
    Vacancy.clear_list()
    vacancy = Vacancy("Python Developer", "https://example.com/python-dev", {"from": 120000, "to": 150000}, "Moscow")

    assert vacancy.name == "Python Developer"
    assert vacancy.url == "https://example.com/python-dev"
    assert vacancy.salary == {"from": 120000, "to": 150000}
    assert vacancy.address == "Moscow"
    assert len(Vacancy.all_list_vacancies()) == 1


def test_all_list_vacancies(sample_vacancies):
    """Проверяем, что вакансии добавляются в список"""
    Vacancy.clear_list()
    for v in sample_vacancies:
        Vacancy(**v)

    all_vacancies = Vacancy.all_list_vacancies()
    assert len(all_vacancies) == 3
    assert all_vacancies[0]["name"] == "Python Developer"
    assert all_vacancies[1]["url"] == "https://example.com/data-scientist"


def test_clear_list(sample_vacancies):
    """Проверяем очистку списка вакансий"""
    Vacancy.clear_list()
    for v in sample_vacancies:
        Vacancy(**v)

    assert len(Vacancy.all_list_vacancies()) == 3
    Vacancy.clear_list()
    assert len(Vacancy.all_list_vacancies()) == 0


def test_validate_salary():
    """Проверяем статический метод __validate"""
    assert Vacancy._Vacancy__validate("120000 - 150000") == {"from": 120000, "to": 150000}
    assert Vacancy._Vacancy__validate(None) == {"from": 0, "to": 0}
    assert Vacancy._Vacancy__validate({"from": 100000, "to": 130000}) == {"from": 100000, "to": 130000}
    assert Vacancy._Vacancy__validate("invalid salary") == {"from": 0, "to": 0}


def test_cast_to_object_list(sample_vacancies):
    """Проверяем метод cast_to_object_list"""
    Vacancy.clear_list()
    Vacancy.cast_to_object_list(sample_vacancies)

    all_vacancies = Vacancy.all_list_vacancies()
    assert len(all_vacancies) == 3
    assert all_vacancies[0]["name"] == "Python Developer"
    assert all_vacancies[2]["url"] == "https://example.com/java-dev"


def test_ge_operator():
    """Проверяем оператор сравнения >= для вакансий"""
    Vacancy.clear_list()
    vacancy1 = Vacancy("Python Developer", "https://example.com/python-dev", {"from": 120000, "to": 150000}, "Moscow")
    vacancy2 = Vacancy("Data Scientist", "https://example.com/data-scientist", {"from": 100000, "to": 130000}, "Saint Petersburg")

    assert vacancy1 >= vacancy2
    assert not vacancy2 >= vacancy1


def test_filtered_salary(sample_vacancies, capsys):
    """Проверяем метод filtered_salary"""
    Vacancy.clear_list()
    Vacancy.cast_to_object_list(sample_vacancies)

    Vacancy.filtered_salary(90000, 140000)
    captured = capsys.readouterr()

    assert "Data Scientist" in captured.out
    assert "Java Developer" in captured.out
    assert "Python Developer" not in captured.out  # Не должен попасть в диапазон
