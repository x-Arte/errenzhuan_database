from Classes import recources, valuedict, db, app, administrator, admin_dict
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import request, url_for, redirect, flash, render_template

db.reflect()

@app.route('/add_resource>', methods=['GET', 'POST'])
def add_resource():
    temp_dict = valuedict.copy()  # 存储属性及其对应值的字典
    rowcount = len(recources.query.all())  # 统计总行数，用来添加id。如果出现id重复的报错，改一下这里
    if request.method == 'POST':
        for key in temp_dict.keys():
            temp_dict[key] = request.form.get(key)
        add1 = recources(rowcount + 1, temp_dict)
        db.session.add(add1)  # 将记录插入到映射表中
        try:
            db.session.commit()  # 提交数据库
            flash('Item add.')  # 显示成功添加的提示
        except SQLAlchemyError as e:
            db.session.rollback()


@app.route('/add_admin>', methods=['GET', 'POST'])
def add_admin():
    temp_dict = admin_dict.copy()  # 存储属性及其对应值的字典
    rowcount = len(administrator.query.all())  # 统计总行数，用来添加id。如果出现id重复的报错，改一下这里
    if request.method == 'POST':
        for key in temp_dict.keys():
            temp_dict[key] = request.form.get(key)
        add1 = administrator(rowcount + 1, temp_dict)
        db.session.add(add1)  # 将记录插入到映射表中
        try:
            db.session.commit()  # 提交数据库
            flash('Admin add.')  # 显示成功添加的提示
        except SQLAlchemyError as e:
            db.session.rollback()


@app.route('/delete_resource/<int:Recource_id>', methods=['GET', 'POST'])
def delete_resource(Recource_id):
    # 我也不知道这个该用get还是post，后期前端决定了就加一个if判断
    dele = recources.query.filter_by(id_resources=Recource_id).first()
    # == select * from recources where id = Recource_id
    db.session.delete(dele)  # 从表中删除记录
    try:
        db.session.commit()
        flash('resource delete.')  # 显示创建失败的提示
    except SQLAlchemyError as e:
        db.session.rollback()


@app.route('/delete_admin/<int:Administrator_id>', methods=['GET', 'POST'])
def delete_admin(Administrator_id):
    # 我也不知道这个该用get还是post，后期决定了就加一个if判断
    dele = administrator.query.filter_by(id_administrator=Administrator_id).first()
    # == select * from recources where id = Recource_id
    db.session.delete(dele)  # 从表中删除记录
    try:
        db.session.commit()
        flash('Admin delete.')  # 显示删除成功
    except SQLAlchemyError as e:
        db.session.rollback()


'''
valuedict['path_resources'] = "https://baidu.com"
add1 = recources(18,valuedict)
db.session.add(add1)  # 将记录插入到映射表中
try:
    db.session.commit()
    #flash('Admin delete.')  # 显示删除成功
except SQLAlchemyError as e:
    db.session.rollback()
    print("error")

admin_dict['name_administrator'] = 'myadmin'
add1 = administrator(2,admin_dict)
db.session.add(add1)  # 将记录插入到映射表中
db.session.commit()  # 提交数据库

admin_dict['name_administrator'] = 'myadmin2'
add1 = administrator(3,admin_dict)
db.session.add(add1)  # 将记录插入到映射表中
db.session.commit()  # 提交数据库

deli = administrator.query.filter_by(id_administrator='2').first()
# == select * from tproducts where id = '1201'
db.session.delete(deli)  # 从表中删除记录
db.session.commit()
'''