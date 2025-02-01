import pytest

from src.functions.func_filter_vacancies import filter_vacancies
from src.functions.func_get_top_vacancies import get_top_vacancies
from src.functions.func_get_vacancies_by_salary import get_vacancies_by_salary
from src.functions.func_print_vacancies import print_vacancies


@pytest.fixture
def sample_vacancies():
    """Фикстура с тестовыми вакансиями"""
    return [
        {
            "name": "Python Developer",
            "address": "Moscow",
            "salary": {"from": 120000, "to": 150000},
            "url": "https://example.com/python-dev",
        },
        {
            "name": "Data Scientist",
            "address": "Saint Petersburg",
            "salary": {"from": 100000, "to": 130000},
            "url": "https://example.com/data-scientist",
        },
        {
            "name": "Java Developer",
            "address": "Moscow",
            "salary": {"from": 90000, "to": 110000},
            "url": "https://example.com/java-dev",
        },
        {
            "name": "Frontend Developer",
            "address": "Remote",
            "salary": {"from": 80000, "to": 100000},
            "url": "https://example.com/frontend-dev",
        },
    ]


def test_filter_vacancies(sample_vacancies):
    """Проверяем фильтрацию вакансий по ключевым словам."""
    result = filter_vacancies(sample_vacancies, ["Python", "Remote"])
    assert len(result) == 2
    assert result[0]["name"] == "Python Developer"
    assert result[0]["url"] == "https://example.com/python-dev"
    assert result[1]["name"] == "Frontend Developer"
    assert result[1]["url"] == "https://example.com/frontend-dev"

    result_empty = filter_vacancies(sample_vacancies, ["Go", "Rust"])
    assert len(result_empty) == 0


def test_get_vacancies_by_salary(sample_vacancies):
    """Проверяем фильтрацию вакансий по зарплате."""
    result = get_vacancies_by_salary(sample_vacancies, "90000 - 140000")
    assert len(result) == 2
    assert result[0]["name"] == "Data Scientist"
    assert result[0]["url"] == "https://example.com/data-scientist"

    result_empty = get_vacancies_by_salary(sample_vacancies, "200000 - 300000")
    assert len(result_empty) == 0

    result_invalid_input = get_vacancies_by_salary(sample_vacancies, "abc - xyz")
    assert result_invalid_input == []


def test_get_top_vacancies(sample_vacancies):
    """Проверяем выбор топ-N вакансий."""
    result = get_top_vacancies(sample_vacancies, 2)
    assert len(result) == 2
    assert result[0]["name"] == "Python Developer"
    assert result[0]["url"] == "https://example.com/python-dev"
    assert result[1]["name"] == "Data Scientist"
    assert result[1]["url"] == "https://example.com/data-scientist"

    result_all = get_top_vacancies(sample_vacancies, 10)
    assert len(result_all) == len(sample_vacancies)


def test_print_vacancies(sample_vacancies, capsys):
    """Проверяем, что print_vacancies корректно выводит список, включая URL."""
    print_vacancies(sample_vacancies)
    captured = capsys.readouterr()
    assert "Python Developer" in captured.out
    assert "https://example.com/python-dev" in captured.out
    assert "Frontend Developer" in captured.out
    assert "https://example.com/frontend-dev" in captured.out
