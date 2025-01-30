from typing import List, Dict, Any


def filter_vacancies(
    vacancies_list: List[Dict[str, Any]], filter_words: List[str]
) -> List[Dict[str, Any]]:
    """Функция фильтрует вакансии по ключевым словам"""
    filtered_vacancies: List[Dict[str, Any]] = []

    for vacancy in vacancies_list:
        for word in filter_words:
            name: str = vacancy.get("name", "")
            address: str = vacancy.get("address", "")

            if not isinstance(name, str):
                name = ""
            if not isinstance(address, str):
                address = ""

            if word.lower() in name.lower() or word.lower() in address.lower():
                filtered_vacancies.append(vacancy)
                break

    return filtered_vacancies
