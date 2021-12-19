from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy  #
from mypassword import pwd
from flask import jsonify

from flask import request, url_for, redirect, flash, render_template

app = Flask(__name__)
# 初始化扩展，传入程序实例 app
# 连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{pwd}@localhost:3306/mydb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# from db import recources , administrator
# 管理员
# 登录查询，通过名字查询


@app.route('/admin', methods=['GET', 'POST'])  # 对应登陆界面
def real_login():
    db.reflect()
    all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
    administrator = db.session.query(all_table['administrator'])
    # administrator= administrator.query.all()

    if request.method == 'POST':
        administrator_name = request.form.get('text')  # 输入名字
        administrator_paw = request.form.get('password')  # 输入密码
        adm = administrator.filter_by(name_administrator=administrator_name).all()

        if adm is None or adm[0][2] != administrator_paw:
            #flash('密码错误.')  # 显示错误提示
            return render_template('login.html')  # 重定向回主页

        # return jsonify(dict_show1)测试
    return render_template('admin.html', adm=adm)  # 进入登录后的界面


if __name__ == '__main__':
    app.run()
