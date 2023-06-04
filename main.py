from get_and_save import GetAndSave
from db_manager import DBManager

if __name__ == "__main__":
    passwd = input('Введите пароль от Б/Д')
    #инициализируем классы,запускаем методы
    copy_get_and_save = GetAndSave(passwd)
    copy_get_and_save.list_cycle()
    copy_db_manager = DBManager(passwd)
    # здесь я хотел экземпяры как то засунуть в словарь, но не придумал как,поставил ифы

    while True:

        usr_inp = input('\nЧто посмотрим:\n1 - Список компаний и количество вакансий у каждой'
                        '\n2 - Список всех вакансий'
                        '\n3 - Средняя зарплата'
                        '\n4 - Список вакансий с зарплатой выше средней'
                        '\n5 - Поиск вакансий по ключевому слову'
                        '\n"q"-выйти')

        if usr_inp.isdigit():
            if int(usr_inp) == 1:
                copy_db_manager.get_companies_and_vacancies_count()
            elif int(usr_inp) == 2:
                copy_db_manager.get_all_vacancies()
            elif int(usr_inp) == 4:
                copy_db_manager.get_vacancies_with_higher_salary()
            elif int(usr_inp) == 3:
                print(copy_db_manager.get_avg_salary())
            elif int(usr_inp) == 5:
                copy_db_manager.get_vacancies_with_keyword(input('по-какому слову искать?'))
            else:
                print('Ошибка')
        if usr_inp.isalpha():
            if str(usr_inp).lower() == 'q':
                exit()

            else:
                print('Ошибка')