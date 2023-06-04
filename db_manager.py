import psycopg2

class DBManager:
    def __init__(self, passwd):
        '''Инициализатор принимает аргмументом пароль от бд'''
        self.passwd = passwd

    def command_sender(self, command):
        '''Отправляет запрос на постгрис'''
        # вот здесь кстати получилось сделать так, как в домашке хотел сделать, что бы менялась только ф-строка
        # c запросом
        with psycopg2.connect(database='vacancy_db', user='postgres', password=self.passwd) as conn:
            with conn.cursor() as cur:


                    cur.execute(command)
                    #conn.commit() не помню зачем , не хочу убирать, потом, может пригодится
                    return cur.fetchall()

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""
        output = self.command_sender('SELECT COUNT(vacancy_id), employer_name FROM infor GROUP BY employer_name')
        i = 0
        for line in output:
            i += 1
            number, name = line
            print(f'{i}) {name}, количество вакансий : {number}')
        #return output # вариант для возвращения списка с кортеджами
    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия
        вакансии и зарплаты и ссылки на вакансию."""
        output = self.command_sender('SELECT employer_name, _name, salary_from, salary_to, salary_currency, '
                                   'employer_alternate_url FROM infor')



        i = 0
        for line in output:
            employer_name, name, salary_from, salary_to, salary_currency, employer_alternate_url = line
            i += 1
            print(f'{i}) {employer_name}, должность: {name}, от {salary_from} до {salary_to} {salary_currency}\n'
                  f'{employer_alternate_url}\n')
            if i % 10 == 0:
                usr_ans = input('Enter - next page, b - back')
                if usr_ans.lower() == 'b':
                    break

                continue
    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""
        #return self.command_sender('')
        avg_salary = self.command_sender('SELECT AVG(salary_from) FROM infor')

        print(f'Средняя  зарплата: {round(avg_salary[0][0], 2 )}')
        #return avg_salary[0]

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""

        output = self.command_sender(f'SELECT * from infor WHERE salary_from > (select AVG(salary_from) '
                                   f'from infor)')
        self.double_function(output)
    def get_vacancies_with_keyword(self,key_word):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”."""
        output = self.command_sender(f"SELECT * FROM infor WHERE LOWER(_name) IN (SELECT LOWER('{key_word}'));")
        self.double_function(output)
    @staticmethod
    def double_function(output):
        '''одинаковый код для двух последних методов''' # можно наверно было все так написать, но там немного разные
                                                        # принты получаются
        i = 0
        for line in output:
            i += 1
            vacancy_id, name, area_name, address, employer_name, employer_alternate_url, salary_from, salary_to, \
                salary_currency = line
            print(f'{i}) {vacancy_id}, {name}, {area_name}, {address}, {employer_name}, \n'
                  f'{employer_alternate_url}, \n'
                  f'от {salary_from}, до {salary_to}, {salary_currency}')
            if i % 10 == 0:
                usr_ans = input('Enter - next page, b - back')
                if usr_ans.lower() == 'b':
                    break

                continue

#формат запроса
#while True:
#    copy1 = DBManager('')
#    print(copy1.get_vacancies_with_keyword(input()))
# по-хорошему цикл надо было тоже сделать отдельной функцией, но я не придумал как
