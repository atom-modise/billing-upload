import mysql.connector
from mysql.connector import Error
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_DATABASE = os.getenv('DB_DATABASE')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')


def connect():
    is_connected = False
    try:
        connection = mysql.connector.connect(host=DB_HOST,
                                             database=DB_DATABASE,
                                             user=DB_USERNAME,
                                             password=DB_PASSWORD)
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            is_connected = True

        return is_connected

    except Error as e:
        print("Error while connecting to MySQL", e)


def insert(data_list):

        try:
            connection = mysql.connector.connect(host=DB_HOST,
                                                 database=DB_DATABASE,
                                                 user=DB_USERNAME,
                                                 password=DB_PASSWORD)
            cursor = connection.cursor()
            today = datetime.now()
            row_count = 0
            for dic in data_list:
                date_time_now = today.strftime("%Y-%m-%d %H:%M:%S")
                payment_status = 0
                row = (dic["pastel_code"], dic["total_due"], payment_status, date_time_now)
                query = "INSERT INTO accounts_receivable (pastel_code, total_due, payment_status, date_issued) VALUES (%s, %s, %s,%s)"
                cursor.execute(query, row)
                connection.commit()
                row_count += 1

            cursor.close()

            return row_count

        finally:
            if connection.is_connected():
                connection.close()
                print("MySQL connection is closed")