"""
Работа с базой данных
"""

import pandas
from pandas import DataFrame

# main dataframe
data = DataFrame()
path_players, path_plays = "", ""


def load_dataframe(db_players_path, db_plays_path):
    """
    Загрузка базы в датафрейм из таблиц
    """

    global data, path_players, path_plays
    path_players, path_plays = db_players_path, db_plays_path
    data = pandas.merge(pandas.read_csv(path_players), pandas.read_csv(path_plays))


def _save_dataframe():
    """
    Сохранение базы из датафрейма в таблицы
    """

    data.iloc[:, 0:4].to_csv(path_players, index=False)
    data.iloc[:, [1, 4, 5]].to_csv(path_plays,  index=False)


def insert_record(record):
    """
    Добавление новой записи
    """

    global data
    data = data.append(record, ignore_index=True)
    _save_dataframe()


def delete_record(index):
    """
    Удаление записи
    """

    global data
    data = data.drop(index).reset_index(drop=True)
    _save_dataframe()


def get_records():
    """
    Получение всех записей в виде листа
    """

    return [el[1:] for el in data.itertuples()]


def update_record(index, record_list):
    """
    Обновление записи
    """

    data.iloc[index] = record_list
    _save_dataframe()


# testing db
if __name__ == '__main__':
    load_dataframe("data/players.csv", "data/plays.csv")
    print(data)


