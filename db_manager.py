import psycopg2
class DBManager:
    def __init__(self):
        pass

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""

        with psycopg2.connect(database='vacancy_db', user='postgres', password=input('DB_Password')) as conn:
            with conn.cursor() as cur:


                    cur.execute('SELECT COUNT(vacancy_id), employer_name FROM infor GROUP BY employer_name')
                    #conn.commit()
                    return cur.fetchall()

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия
        вакансии и зарплаты и ссылки на вакансию."""
        pass

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""

        pass

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        pass

    def get_vacancies_with_keyword(self):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”."""
