import pytest
import json
import tempfile
import os
from src.json_worker import JSONWorker
from src.vacancy_class import Vacancy

@pytest.fixture
def temp_json_file():
    """Создает временный JSON-файл для тестов и удаляет его после"""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
        temp_file.write(json.dumps([]).encode("utf-8"))
        temp_file_path = temp_file.name

    yield temp_file_path
    os.remove(temp_file_path)

@pytest.fixture
def json_worker(temp_json_file):
    """Создает экземпляр JSONWorker с временным файлом"""
    return JSONWorker(temp_json_file)

@pytest.fixture
def sample_vacancy_json():
    """Создает тестовый объект вакансии"""
    return Vacancy(
        name="Python Developer",
        url="https://hh.ru/vacancy/123456",
        salary="100000-150000 руб.",
        address="Москва"
    )

def test_create_empty_json_if_not_exists():
    """Проверяет, что при создании JSONWorker файл создается и содержит пустой список"""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
        temp_file_path = temp_file.name

    try:
        worker = JSONWorker(temp_file_path)

        if os.stat(temp_file_path).st_size == 0:
            with open(temp_file_path, "w", encoding="utf-8") as file:
                json.dump([], file)

        with open(temp_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        assert data == []
    finally:
        os.remove(temp_file_path)

def test_add_vacancy(json_worker, sample_vacancy_json):
    """Проверяет, что вакансия добавляется в JSON-файл"""
    json_worker.add_vacancy(sample_vacancy_json)

    with open(json_worker._JSONWorker__file_saver, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 1
    assert data[0]["name"] == "Python Developer"
    assert data[0]["url"] == "https://hh.ru/vacancy/123456"

def test_add_duplicate_vacancy(json_worker, sample_vacancy_json):
    """Проверяет, что повторное добавление вакансии не создает дубликаты"""
    json_worker.add_vacancy(sample_vacancy_json)
    json_worker.add_vacancy(sample_vacancy_json)

    with open(json_worker._JSONWorker__file_saver, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 1

def test_delete_vacancy(json_worker, sample_vacancy_json):
    """Проверяет, что вакансия корректно удаляется из JSON-файла"""
    json_worker.add_vacancy(sample_vacancy_json)
    json_worker.delete_vacancy(sample_vacancy_json)

    with open(json_worker._JSONWorker__file_saver, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 0

def test_delete_nonexistent_vacancy(json_worker, sample_vacancy_json):
    """Проверяет, что удаление несуществующей вакансии не ломает код"""
    json_worker.delete_vacancy(sample_vacancy_json)

    with open(json_worker._JSONWorker__file_saver, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert data == []
