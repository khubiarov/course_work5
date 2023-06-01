import requests, json, psycopg2, csv


class GetAndSave:
    def __init__(self):
        #self.name = input('Введите...')
        self.company_url = ''

    def read_list(self):

        with open("company_list.txt", 'rt', encoding='utf-8') as file:
            company_list = []
            content = csv.reader(file, delimiter="\n")

            for line in content:
                print(line[0])
                company_list.append(line[0])
            return company_list
    def get_vacancy(self):
        """Получает """
        req = requests.get(f'{str(self.company_url)}')
        data = req.content.decode()  # спер из одного мануала

        req.close()

        json.dumps(data)
        data = json.loads(data)
        return data

    def save(self):
        """Сохраняет запрошенные данные от апи в бд"""
        data = self.get_vacancy()
        count = 1
        with psycopg2.connect(database='vacancy_db', user='postgres', password='Rikitikitavi13245') as conn:
            with conn.cursor() as cur:
                for row in data['items']:

                    if row.get('address') is None:
                        row['address'] = {}
                        row['address']['city'] = None
                    print(row)

                    cur.execute(
                        f'INSERT INTO infor(vacancy_id, _name, area_name, address, vac_number) VALUES (%s, %s, %s, %s, %s, %s)',
                        (row['id'], row["name"], row["area"]['name'], row["address"]['city'], count, row['employer']['name']))
                    count += 1
                    conn.commit()

                    #cur.execute("SELECT * FROM infor ")

                    #conn.commit
                    #print(cur.fetchall())

    def list_cycle(self):
        company_list = self.read_list()
        for item in company_list:
            self.company_url = str(item)
            self.save()


