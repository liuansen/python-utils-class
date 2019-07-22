# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

import psycopg2

from ty_db_oper import DbOper


def get_db_access_info(db_access_id):
    dpoper = DbOper()
    sql = """
    select DB_IP, PORT, DBSID, DBUSR, DBPWD, DATABASE,
    UPPER(TARGET_SCHEMA)
    FROM F_DB_ACCESS_CTL_INFO
    WHERE DB_ACCESS_ID='%s'
    and DB_TYPE=LOWER('GREENPLUM')
    """ % db_access_id
    rows = dpoper.select(sql)
    print 'rows:', rows
    if len(rows) >= 1:
        rows = rows[0]
        ret_rows = {'DATABASE': rows['DATABASE'],
                    'DB_IP': rows['DB_IP'],
                    'DBUSR': rows['DBUSR'],
                    'DBPWD': rows['DBPWD'],
                    'PORT': rows['PORT']}
    else:
        raise Exception, "Oracle配置库中F_DB_ACCESS_CTL_INFO表无DB_ACCESS_ID={}的配置！".format(db_access_id)
    return ret_rows


class PostGreSQL(object):
    def __init__(self, row_list):
        self.gp_database = row_list['DATABASE']
        self.dp_ip = row_list['DB_IP']
        self.gp_usr = row_list['DBUSR']
        self.gp_pwd = row_list['DBPWD']
        self.port = row_list['PORT']
        self.content = False
        self.conn = None

    def get_content(self):
        self.conn = psycopg2.connect(
            database=self.gp_database, user=self.gp_usr,
            password=self.gp_pwd, host=self.dp_ip,
            port=self.port, sslmode='allow')
        self.content = True

    def cursor(self):
        return self.conn.cursor()

    def commit(self):
        if self.content:
            return self.conn.commit()
        else:
            raise Exception, "PostGreSQL库连接失败！"

    def select(self, sql):
        if self.content:
            cursor = self.cursor()
        else:
            self.get_content()
            cursor = self.cursor()
        cursor.execute(sql)
        self.commit()
        rows = cursor.fetchall()

        column_description_list = cursor.description
        column_map = {}
        for i in range(len(column_description_list)):
            col_desc = column_description_list[i]
            # print(col_desc)
            column_name = col_desc[0]
            column_map[i] = column_name

        return_row_list = []
        for origin_row in rows:
            row = {}
            for i in range(len(origin_row)):
                value = origin_row[i]
                row[column_map[i]] = value
            return_row_list.append(row)
        return return_row_list

    # 执行SQL，返回影响的数据行数
    def execute(self, sql):
        try:
            if not self.content:
                self.get_content()
            cursor = self.cursor()
            aff_row_num = cursor.execute(sql)
            cursor.close()
            return aff_row_num
        except Exception as e:
            print("db execute error:" + str(e))
            raise e


if __name__ == '__main__':
    post_list = get_db_access_info('spark_test_stage_gp')
    post_gre_sql = PostGreSQL(post_list)
    sql = """select * from base.gbr_inst_hier_tmp limit 20"""
    row = post_gre_sql.select(sql)
    print(row)
