# D:\pycharm\pycharmworkspace
# -*-coding:utf-8-*-
# Author: lzq
# Time: 2021/12/13
# 说明：
from Classes import recources, valuedict, db, app, administrator, admin_dict
from update_research import home
import add_delete
import adm_log
import Classes

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)
    home()
