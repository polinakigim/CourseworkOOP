from unittest.mock import Mock, patch

import pytest

from src.hh_api import HH


@pytest.fixture
def hh_parser():
    """Фикстура для создания экземпляра HH"""
    return HH()


def test_load_vacancies(hh_parser):
    """Тест загрузки вакансий с API hh.ru"""

    mock_response = {
        "items": [
            {"id": "1", "name": "Python Developer"},
            {"id": "2", "name": "Data Scientist"},
        ]
    }

    with patch("requests.get") as mock_get:
        mock_get.return_value = Mock(json=lambda: mock_response)

        keyword = "Python"
        vacancies = hh_parser.load_vacancies(keyword)

        assert mock_get.call_count == 20

        assert len(vacancies) == 40
        assert vacancies[0]["name"] == "Python Developer"
        assert vacancies[1]["name"] == "Data Scientist"

        mock_get.assert_called_with(
            "https://api.hh.ru/vacancies",
            headers={"User-Agent": "HH-User-Agent"},
            params={"text": keyword, "page": 20, "per_page": 100},
        )
