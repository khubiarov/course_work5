from get_and_save import GetAndSave
from db_manager import DBManager

if __name__ == "__main__":
    passwd = input('Введите пароль от Б/Д')

    copy_get_and_save = GetAndSave(passwd)
    copy_get_and_save.list_cycle()
    copy_db_manager = DBManager(passwd)
    while True:
        usr_inp = input('Что посмотрим')
        if usr_inp.isdigit():
            if int(usr_inp) == 1:
                print(copy_db_manager.get_companies_and_vacancies_count())
            elif int(usr_inp) == 2:
                print(copy_db_manager.get_all_vacancies())
            elif int(usr_inp) == 3:
                print(copy_db_manager.get_vacancies_with_higher_salary())
        if usr_inp.isalpha():
            if str(usr_inp).lower() == 'q':
                copy_db_manager.quit_from_app()

        else:
            print('Ошибка')