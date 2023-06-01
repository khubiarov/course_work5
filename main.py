from get_and_save import GetAndSave
from db_manager import DBManager
copy1 = GetAndSave()
copy1.list_cycle()
copy2 = DBManager()

while True:
    input('Посмотрим?')
    print(copy2.get_companies_and_vacancies_count())