from typing import Any, Dict, List


def filter_vacancies(
    vacancies_list: List[Dict[str, Any]], filter_words: List[str]
) -> List[Dict[str, Any]]:
    """Функция фильтрует вакансии по ключевым словам"""
    filtered_vacancies: List[Dict[str, Any]] = []

    for vacancy in vacancies_list:
        name = str(vacancy.get("name", ""))
        address = str(vacancy.get("address", ""))

        for word in filter_words:
            if word.lower() in name.lower() or word.lower() in address.lower():
                filtered_vacancies.append(vacancy)
                break

    return filtered_vacancies
