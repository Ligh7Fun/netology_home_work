# import psycopg2
import psycopg2.extensions
import os
from dotenv import load_dotenv
import datetime
from prettytable import from_db_cursor


class Logger:

    def __init__(self, filename: str = 'logs.log') -> None:
        self.filename = filename

    def add(self, type_log: str, message: str) -> None:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[
                    :-3]
        log_message = f'[{timestamp}][{type_log}] {message}'
        print(f'[{timestamp}][{type_log}] {message}')
        with open(self.filename, 'a') as file:
            file.write(log_message + '\n')


log = Logger()

load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')


def create_db(connection: psycopg2.extensions.connection) -> None:
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE
        );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS phones (
                id SERIAL PRIMARY KEY,
                phone_number VARCHAR(20) NOT NULL UNIQUE,
                user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE
        );
        """)
        connection.commit()
        log.add('INFO', 'create_db: OK')


def add_client(connection: psycopg2.extensions.connection,
               first_name: str,
               last_name: str,
               email: str,
               phone_number: str = None) -> None:
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                INSERT INTO users (first_name, last_name, email)
                VALUES (%s, %s, %s) RETURNING id;
            """, (first_name, last_name, email))
            connection.commit()
            user_id_ = cursor.fetchone()[0]

            if phone_number:
                add_phone(connection, user_id_, phone_number)

            log.add('INFO', f'add_client {first_name} {last_name} {email}: OK')
            find_client(connection=connection, user_id=user_id_)
        except Exception as e:
            log.add('ERROR', f'add_client: {e}')


def get_user_id(connection: psycopg2.extensions.connection,
                email: str) -> int | None:
    """
    Получаем user_id по email адресу пользователя
    """
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                SELECT id FROM users WHERE email=%s;
            """, (email,))
            connection.commit()
            log.add('INFO', f'get_user_id: OK')
            return int(cursor.fetchone()[0]) if cursor.rowcount else None
        except Exception as e:
            log.add('ERROR', f'get_user_id: {e}')


def add_phone(connection: psycopg2.extensions.connection,
              user_id: str,
              phone_number: str) -> None:
    with connection.cursor() as cursor:
        try:
            user_id = int(user_id)
            cursor.execute("""
                INSERT INTO phones (phone_number, user_id)
                VALUES (%s, %s);
            """, (phone_number, user_id))
            connection.commit()
            log.add('INFO', f'add_phone {phone_number}: OK')
        except Exception as e:
            log.add('ERROR', f'add_phone: {e}')


def show_clients_all(connection: psycopg2.extensions.connection) -> None:
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                SELECT 
                    u.id,
                    MAX(u.first_name) "first name",
                    MAX(u.last_name) "last name",
                    u.email,
                    STRING_AGG(p.phone_number, '\n ') "phone numbers"
                FROM users u
                LEFT JOIN phones p ON u.id = p.user_id
                GROUP BY u.id, u.email
                ORDER BY u.id;
            """)
            connection.commit()
            show_table = from_db_cursor(cursor)
            print(show_table)
            log.add('INFO', f'show_clients_all: OK')
        except Exception as e:
            log.add('ERROR', f'show_clients_all: {e}')


def find_client(connection: psycopg2.extensions.connection,
                user_id: str = None,
                first_name: str = None,
                last_name: str = None,
                email: str = None,
                phone_number: str = None
                ) -> None:

    with connection.cursor() as cursor:
        try:
            base_query = """
                            SELECT 
                                u.id,
                                MAX(u.first_name) "first name",
                                MAX(u.last_name) "last name",
                                u.email,
                                STRING_AGG(p.phone_number, '\n ') "phone numbers"
                            FROM users u
                            LEFT JOIN phones p ON u.id = p.user_id
                            """

            query_params = []

            if user_id:
                user_id = int(user_id)
                base_query += " WHERE u.id = %s"
                query_params.append(user_id)
            elif first_name:
                base_query += " WHERE u.first_name = %s"
                query_params.append(first_name)
            elif last_name:
                base_query += " WHERE u.last_name = %s"
                query_params.append(last_name)
            elif email:
                base_query += " WHERE u.email = %s"
                query_params.append(email)
            elif phone_number:
                base_query += " WHERE p.phone_number = %s"
                query_params.append(phone_number)

            base_query += """
                            GROUP BY u.id, u.email
                            ORDER BY u.id;
                        """

            cursor.execute(base_query, query_params)
            connection.commit()
            show_table = from_db_cursor(cursor)
            print(show_table)
            log.add('INFO', f'find_client: OK')
        except Exception as e:
            log.add('ERROR', f'find_client: {e}')


def change_client(connection: psycopg2.extensions.connection,
                  user_id: str):
    pass


def delete_phone(connection: psycopg2.extensions.connection,
                 phone_number: str = None):
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                DELETE FROM phones WHERE phone_number=%s;
            """, (phone_number,))
            connection.commit()
            log.add('INFO', f'delete_phone {phone_number}: OK')
        except Exception as e:
            log.add('ERROR', f'delete_phone: {e}')


def delete_client(connection: psycopg2.extensions.connection,
                  user_id: str) -> None:
    with connection.cursor() as cursor:
        try:
            user_id = int(user_id)
            cursor.execute("""
                DELETE FROM users WHERE id=%s;
            """, (user_id,))
            connection.commit()
            log.add('INFO', f'delete_client: OK')
        except Exception as e:
            log.add('ERROR', f'delete_client: {e}')


def main_menu():
    menu_items = ['Show all user',
                  'Add User',
                  'Add phone for existing User',
                  'Edit User data',
                  'Delete phone number',
                  'Delete an existing User',
                  'Find a client']
    for index, item in enumerate(menu_items, start=1):
        print(f'{index} - {item}')


def press_enter():
    input('Press Enter for continue...')


with psycopg2.connect(database=DB_NAME,
                      user=DB_USER,
                      password=DB_PASSWORD,
                      host=DB_HOST,
                      port=DB_PORT) as conn:
    with conn.cursor() as cur:
        create_db(conn)
        menu = -1
        try:
            while menu != 0:
                main_menu()
                print('Press "0" for exit.')
                try:
                    menu = int(input('Enter menu position: ').strip())
                except ValueError:
                    print("Incorrect input! Please enter numbers only.")
                if menu == 1:
                    show_clients_all(connection=conn)
                    press_enter()
                elif menu == 2:
                    add_client(connection=conn,
                               first_name=input('Enter first name: '),
                               last_name=input('Enter last name: '),
                               email=input('Enter email: '),
                               phone_number=input(
                                   'Enter phone number(optional): ')
                               )
                    press_enter()
                elif menu == 3:
                    add_phone(connection=conn,
                              user_id=input('Enter User ID: '),
                              phone_number=input('Enter phone number: '))
                    press_enter()
                elif menu == 4:

                    press_enter()
                elif menu == 5:
                    delete_phone(connection=conn,
                                 phone_number=input('Enter phone number: '))
                    press_enter()
                elif menu == 6:
                    show_clients_all(connection=conn)
                    delete_client(connection=conn,
                                  user_id=input('Enter User ID: '))
                    press_enter()
                elif menu == 7:
                    find_client(connection=conn,
                                user_id=input('Enter User ID: '),
                                first_name=input('Enter first name: '),
                                last_name=input('Enter last name: '),
                                email=input('Enter email: '),
                                phone_number=input(
                                    'Enter phone number(optional): ')
                                )
                    press_enter()

        except Exception as e:
            log.add('ERROR', f'main menu: {e}')

conn.close()
