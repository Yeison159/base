from flask import Flask
import pymysql


class Database:

    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = ""
        db = "gestionrecursos"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def list_employees(self):
        self.cur.execute("SELECT * from usuario")
        result0 = self.cur.fetchall()

        return result0

    def lisByUser(self, id):

        try:
            sql = "select * from usuario where usuario_id = %s"
            self.cur.execute(sql, id)
            result3 = self.cur.fetchall()
        finally:
            return result3

    def lisBycount(self):

        try:
            sql = "select * from usuario where usuario_id"
            self.cur.execute(sql)
            result1 = self.cur.fetchmany(12)
        finally:
            return result1
