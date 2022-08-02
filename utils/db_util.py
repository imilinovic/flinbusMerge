from typing import Optional, Type, TypeVar

import psycopg2

import settings

T = TypeVar("T")


class DBUtil:
    _db_handler: Optional['_DBHandler'] = None

    class _DBHandler:
        def __init__(self):
            self.pg = psycopg2.connect(
                host=settings.POSTGRES_HOST,
                database=settings.POSTGRES_DB,
                user=settings.POSTGRES_USER,
                password=settings.POSTGRES_PASSWORD,
            )

    def __init__(self):
        if not DBUtil._db_handler:
            DBUtil._db_handler = DBUtil._DBHandler()

    def filter(self, cls: Type[T], **filter_opts) -> list[T]:
        table = cls.__name__.lower()

        if filter_opts:
            equality_checks = [f"{key} = '{value}'" for key, value in filter_opts.items()]
            where_section = " AND ".join(equality_checks)

            query = f"SELECT * FROM {table} WHERE {where_section};"
        else:
            query = f"SELECT * FROM {table};"

        results: list[T] = []

        with DBUtil._db_handler.pg.cursor() as cursor:
            cursor.execute(query)

            for row in cursor:
                results.append(cls(**{key: value for key, value in zip(cls.get_field_names(), row)}))

        return results

    def insert(self, value: T) -> None:
        table = value.__class__.__name__.lower()

        values = []

        for field_value in value.dict().values():
            if str(field_value).lower() != "default":
                values.append(f"'{field_value}'")
            else:
                values.append("DEFAULT")

        values = ", ".join(values)

        query = f"INSERT INTO {table} VALUES ({values});"

        with DBUtil._db_handler.pg.cursor() as cursor:
            cursor.execute(query)
            DBUtil._db_handler.pg.commit()

    def update(self, value: T, **filter_opts) -> None:
        table = value.__class__.__name__.lower()

        values = ", ".join([f"{field_key} = '{field_value}'" for field_key, field_value in value.dict().items()])

        if filter_opts:
            equality_checks = [f"{key} = '{value}'" for key, value in filter_opts.items()]
            where_section = " AND ".join(equality_checks)
        else:
            primary_key = value.primary_key()
            where_section = f"{primary_key} = '{getattr(value, primary_key)}'"

        query = f"UPDATE {table} SET {values} WHERE {where_section};"

        with DBUtil._db_handler.pg.cursor() as cursor:
            cursor.execute(query)
            DBUtil._db_handler.pg.commit()

    def delete(self, value: T) -> None:
        table = value.__class__.__name__.lower()

        where_section = " AND ".join(
            [f"{field_key} = '{field_value}'" for field_key, field_value in value.dict().items()]
        )

        query = f"DELETE FROM {table} WHERE {where_section};"

        with DBUtil._db_handler.pg.cursor() as cursor:
            cursor.execute(query)
            DBUtil._db_handler.pg.commit()

    def rollback(self) -> None:
        DBUtil._db_handler.pg.rollback()
