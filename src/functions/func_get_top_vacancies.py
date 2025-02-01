from typing import Any, Dict, List


def get_top_vacancies(
    filtered_vacancies: List[Dict[str, Any]], top_n: int
) -> List[Dict[str, Any]]:
    """Функция вывода топ вакансий по выбору пользователя"""
    return filtered_vacancies[:top_n]
