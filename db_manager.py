import psycopg2

class DBManager:
    def __init__(self, passwd):
        self.passwd = passwd

    def command_sender(self, command):
        with psycopg2.connect(database='vacancy_db', user='postgres', password=self.passwd) as conn:
            with conn.cursor() as cur:


                    cur.execute(command)
                    #conn.commit()
                    return cur.fetchall()

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""
        return self.command_sender('SELECT COUNT(vacancy_id), employer_name FROM infor GROUP BY employer_name')

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия
        вакансии и зарплаты и ссылки на вакансию."""
        return self.command_sender('SELECT employer_name, _name, salary_from, salary_to, salary_currency, '
                                   'employer_alternate_url FROM infor')

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""
        #return self.command_sender('')
        avg_salary = self.command_sender('SELECT AVG(salary_from) FROM infor')
        return avg_salary[0]

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        avg_number = self.get_avg_salary()
        return self.command_sender(f'SELECT * from infor WHERE salary_from > (select AVG(salary_from) '
                                   f'from infor)')


    def get_vacancies_with_keyword(self,key_word):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”."""
        return self.command_sender(f"SELECT * FROM infor WHERE LOWER(_name) IN (SELECT LOWER('{key_word}'));")

    def quit_from_app(self):
        exit()


#while True:
#    copy1 = DBManager('Rikitikitavi13245')
#    print(copy1.get_vacancies_with_keyword(input()))