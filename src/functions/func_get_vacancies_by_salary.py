from typing import List, Dict, Any


def get_vacancies_by_salary(
    filtered_vacancies: List[Dict[str, Any]], salary_range: str
) -> List[Dict[str, Any]]:
    """Функция сортирует вакансии по вилке зарплаты (от и до)"""
    filtered_salary_vacancies: List[Dict[str, Any]] = []
    from_to_salary: List[str] = salary_range.split()

    try:
        min_salary: int = int(from_to_salary[0])
        max_salary: int = int(from_to_salary[2])
    except (IndexError, ValueError):
        print("Некорректный ввод диапазона зарплат. Пример: '100000 - 150000'")
        return []

    for vacancy in filtered_vacancies:
        salary: Dict[str, Any] = vacancy.get("salary", {})
        salary_from = salary.get("from")
        salary_to = salary.get("to")

        if salary_from is not None and salary_to is not None:
            try:
                salary_from = int(salary_from)
                salary_to = int(salary_to)
            except ValueError:
                continue

            if salary_from >= min_salary and salary_to <= max_salary:
                filtered_salary_vacancies.append(vacancy)

    return sorted(
        filtered_salary_vacancies, key=lambda x: x["salary"].get("to", 0), reverse=True
    )
