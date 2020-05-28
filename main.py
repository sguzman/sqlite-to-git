import atexit
import datetime
import sqlite3
import sys
import typing


def main() -> None:
    table_name: str = sys.argv[1]
    sql_str: str = f'SELECT * FROM {table_name}'

    conn: sqlite3.Connection = sqlite3.connect('db.sqlite')
    atexit.register(lambda: conn.close())

    c: sqlite3.Cursor = conn.cursor()
    for row in c.execute(sql_str):
        time_opt: typing.Optional[datetime.datetime] = None
        try:
            time: datetime.datetime = datetime.datetime.strptime(row[1], '%Y-%m-%dT%H:%M:%S')
            time_opt = time
        except Exception as e:
            time: datetime.datetime = datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
            time_opt = time

        time: datetime.datetime = time_opt
        msg: str = row[2]

        print(time, msg)


if __name__ == '__main__':
    main()
