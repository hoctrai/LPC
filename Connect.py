from itertools import count

import psycopg2
from django.db import transaction, DatabaseError
from configparser import ConfigParser


def config(filename, section):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


class DB_connection:
    params = ''
    conn = ''
    cur = ''

    def __init__(self):
        print()
        self.display()

    def connect(self):
        """connnet to postgresql database server"""
        conn = None
        try:
            # read connection parameters
            self.params = config('DB.ini', 'postgresql')

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**self.params)

            # create a cursor
            self.cur = self.conn.cursor()

            # execute a statement
            print('PostgreSQL database version:')
            self.cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = self.cur.fetchone()
            print(db_version)

            # close the communication with the PostgreSQL
            # cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        except DatabaseError:
            transaction.rollback()
        # finally:
        #     if conn is not None:
        #         conn.close()
        #         print('Database connection closed.')

    def close_memory(self):
        self.cur.close()
        if self.conn is not None:
            self.conn.close()

    def insert_lpc_list(self, lpc_list):
        """ insert multiple vendors into the vendors table  """
        sql = "INSERT INTO lpc(Province, Date, Type, is_print, value) VALUES(%s)"
        # conn = None
        try:
            self.cur.executemany(sql, lpc_list)
            # commit the changes to the database
            self.conn.commit()
            # close communication with the database
            # cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        # finally:
        #     if conn is not None:
        #         conn.close()

    def insert_lpc(self, Province, Date, Type, is_print, value):
        """ insert a new vendor into the vendors table """
        sql = """INSERT INTO lpc(province, date, type, is_print, value)
                 VALUES(%s,%s,%s,%s,%s) RETURNING id;"""
        # conn = None
        id = None
        try:

            # execute the INSERT statement
            self.cur.execute(sql, [Province, Date, Type, is_print, value, ])
            # get the generated id back
            id = self.cur.fetchone()[0]
            # commit the changes to the database
            self.conn.commit()
            # close communication with the database
            # cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        # finally:
        #     self.close_memory()

        return id

    def is_none_exist_lpc(self, province, date, type, value):
        """

        :type type: object
        """
        # count = int (0)
        sql = """   SELECT *
                    FROM lpc 
                    WHERE 
                        lpc.province = %s AND 
                        lpc.date = %s AND 
                        lpc.type = %s AND 
                        lpc.value = %s """
        self.cur.execute(sql, [province, date, type, value])
        if self.cur.rowcount == 0:
            return True
        elif self.cur.rowcount == 1:
            print("Data have been gotten in %s", str(date))
            return False
        elif self.cur.rowcount > 1:
            print("there are dulicate in database ")
            return False
        return True

    def get_cur(self):
        return self.cur

    def display(self):
        self.connect()
#
# run = DB_connection()
# run.display()
