from Classes import recources, valuedict, db, app, administrator, admin_dict
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import request, url_for, redirect, flash, render_template

db.reflect()

@app.route('/')
def home():
    # res = recources.query.filter_by(type_resources='剧本')
    return render_template('home.html')


@app.route('/search', methods=['POST','GET'])
def search():
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        text = request.form.get('text')  # 传入表单对应输入字段的 name 值
        # 验证数据
        if text == "":
            flash('Invalid input.')  # 显示错误提示
            return redirect(url_for('home'))  # 重定向回主页
        # 查询表单数据从数据库 result

        return render_template('search.html')
    return render_template('search.html')
    # return redirect(url_for('home'))  # 重定向回主页
