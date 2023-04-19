"""
Импорт данных в базу данных sqlite из csv файл

Пример использования:
    python manage.py import_csv_users

"""
import os
import sqlite3

import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'Import csv to sqlite3'

    def handle(self, *args, **options):
        name_app = 'users_'

        db_file = os.path.join(settings.BASE_DIR, 'db.sqlite3')
        path_to_csv = os.path.join(settings.STATICFILES_DIRS[0], 'data')
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        for root, dirs, files in os.walk(path_to_csv):
            for file_name in files:
                if file_name == 'user.csv':
                    table_name = name_app + file_name.split('.')[0]
                    df = pd.read_csv(f'{path_to_csv}/{file_name}')
                    query = 'SELECT count(*) FROM {} '.format(table_name)
                    c.execute(query)
                    data = c.fetchone()
                    if data[0]:
                        print(f'Таблица {file_name.split(".")[0]}'
                              'не пустая, содержит {data[0]} записей')
                    else:
                        print(f'Таблица {file_name.split(".")[0]}'
                              'пустая. Делаем импорт!')
                        df.to_sql(
                            table_name,
                            conn,
                            if_exists='append',
                            index=False
                        )
