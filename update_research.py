import json
from Classes import recources, valuedict, db, app, administrator, admin_dict
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import request, url_for, redirect, flash, render_template, jsonify
from flask import Flask
from mypassword import pwd

db.reflect()


def getData():
    juben = recources.query.filter_by(type_resources='剧本')
    juben_cn = juben.count()
    pic_cn = recources.query.filter_by(type_resources='图片').count()
    video_cn = recources.query.filter_by(type_resources='视频').count()
    return juben, juben_cn, pic_cn, video_cn


@app.route('/', methods=['POST','GET'])
def home():
    juben, juben_cn, pic_cn, video_cn = getData()
    return render_template('home.html', juben = juben ,juben_cn = juben_cn, pic_cn = pic_cn, video_cn = video_cn)


@app.route('/login')  # 对应登陆界面
def login_page():
    return render_template('login.html')


@app.route('/api/getAll')
def getAll():
    results = []
    for id_resources,title_resources,path_resources in db.session.query(recources.id_resources,recources.title_resources,recources.path_resources).order_by(recources.id_resources):
        tmp = {}
        tmp['id'] = id_resources
        tmp['name'] = title_resources
        tmp['url'] = path_resources
        #print(tmp)
        results.append(tmp)
    res = {'list': results}
    print(res)
    return jsonify(res)  # :please return {list:[{id:id,name:title,url:path}]}


@app.route('/search', methods=['POST','GET'])
def search():
    text = ""
    if request.method == 'POST':  # 处理编辑表单的提交请求
        text = request.form['text']
    print(text)
    results = recources.query.filter_by(title_resources=text)
    for result in results:
        if result.type_resources == '图片':
            result.path_resources = 'static/images/'+ result.path_resources.split('\\')[-1]
            # print(result.path_resources)
    return render_template('search.html',results=results)

@app.route('/admin')  # 对应登陆界面
def real_login():
    all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}
    administrator = db.session.query(all_table['administrator'])
    # administrator= administrator.query.all()
    administrator_name = request.args.get('text')  # 输入名字
    administrator_paw = request.args.get('password')  # 输入密码
    adm = administrator.filter_by(name_administrator=administrator_name).all()
    if adm == [] or adm[0][2] != administrator_paw:
        return redirect('/login')

    # return jsonify(dict_show1)测试
    return render_template('admin.html', username=administrator_name)  # 进入登录后的界面


# 改，编辑
# 可更新除id外的所有内容
@app.route('/edit/<int:Recource_id>', methods=['GET', 'POST'])
def index(Recource_id):
    db.reflect()
    all_table = {table_obj.name: table_obj for table_obj in db.get_tables_for_bind()}  # 获取数据库所有表名
    Recources = db.session.query(all_table['recources'])  # 得到resource表
    # Resource = Recources.query.filter_by(id_resources=Recource_id).all()#找到要编辑的资源内容
    Resource = recources.query.filter_by(id_resources=Recource_id)
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        # dict_show = {}
        type = request.form.get('type')  # 传入表单对应输入字段的 name 值
        path = request.form.get('path')
        content = request.form.get('content')
        Title = request.form.get('title')
        Author = request.form.get(' Author')
        Version = request.form.get('Version')
        Publication = request.form.get('Publication')
        Date = request.form.get('Date')
        Description = request.form.get(' Description')
        Keyword = request.form.get(' Keyword')
        Form = request.form.get(' Form')
        Format = request.form.get('Format')
        Language = request.form.get(' Language')
        Audience = request.form.get('Audience')
        origin = request.form.get('origin')
        Link = request.form.get('  Link')
        Authority = request.form.get('Authority')
        Coverage = request.form.get(' Coverage')
        Source = request.form.get(' Source')
        Collection = request.form.get(' Collection')
        processing = request.form.get('processing')
        service = request.form.get('service')
        acceptance = request.form.get('acceptance')
        alternative_title = request.form.get('alternative_title')
        parallel_title = request.form.get(' parallel_title')
        other_title_information = request.form.get('  other_title_information')
        parallel_series_title = request.form.get(' parallel_series_title')
        series_total = request.form.get('series_total')
        series = request.form.get(' series')
        personal_name = request.form.get(' personal_name')
        team_name = request.form.get(' team_name')
        meeting_name = request.form.get('meeting_name')
        parallel_responsibility = request.form.get('parallel_responsibility')
        other_res_information = request.form.get('other_res_information')
        responsibility_way = request.form.get('responsibility_way')
        publication_place = request.form.get('publication_place')
        publication_people = request.form.get(' publication_people')
        produce_place = request.form.get(' produce_place')
        produce_people = request.form.get(' produce_people')
        photo_date = request.form.get('photo_date')
        record_date_vedio = request.form.get('record_date_vedio')
        record_date_movie = request.form.get('record_date_movie')
        publication_date = request.form.get('publication_date')
        up_date = request.form.get('up_date')
        create_date = request.form.get('create_date')
        summary = request.form.get('summary')
        content = request.form.get('content')
        reward = request.form.get('reward')
        singing_style = request.form.get('singing_style')
        music_part = request.form.get('music_part')
        singing_form = request.form.get('singing_form')
        playing_form = request.form.get('playing_form')
        additional_type = request.form.get('additional_type')
        additional_des = request.form.get('additional_des')
        channel_id = request.form.get(' channel_id')
        channel_content = request.form.get('channel_content')
        note = request.form.get(' note')
        finding_route = request.form.get(' finding_route')
        show_type = request.form.get(' show_type')
        show_form = request.form.get('show_form')
        number = request.form.get('number')
        size = request.form.get('size')
        time = request.form.get('time')
        enter_point = request.form.get('enter_point')
        standard = request.form.get('standard')
        width_height = request.form.get(' width_height')
        voice_character = request.form.get('voice_character')
        color = request.form.get(' color')
        subtitle_form = request.form.get(' subtitle_form')
        resolution_ratio = request.form.get(' resolution_ratio')
        Audio_format = request.form.get('Audio_format')
        voice_quality = request.form.get('voice_quality')
        picture_quality = request.form.get('picture_quality')
        audio_programming_format = request.form.get(' audio_programming_format')
        audio_data_ratio = request.form.get('audio_data_ratio')
        audio_frequency = request.form.get(' audio_frequency')
        audio_depth = request.form.get(' audio_depth')
        movie_programming_format = request.form.get(' movie_programming_format')
        movie_sampling_format = request.form.get('movie_sampling_format')
        movie_data_ratio = request.form.get('movie_data_ratio')
        document_format = request.form.get('document_format')
        channel_language = request.form.get('channel_language')
        subtitle_id = request.form.get('subtitle_id')
        subtitle_language = request.form.get('subtitle_language')
        obtain_way = request.form.get('obtain_way')
        provider = request.form.get('provider')
        origin_version = request.form.get('origin_version')
        other_version = request.form.get('other_version')
        include = request.form.get('include')
        being_included = request.form.get('being_included')
        reference = request.form.get('reference')
        being_refered = request.form.get(' being_refered')
        copyright_owner = request.form.get('copyright_owner')
        copyright_shengming = request.form.get(' copyright_shengming')
        authorization_user = request.form.get(' authorization_user')
        authorization_usage = request.form.get(' authorization_usage')
        authorization_date = request.form.get('authorization_date')
        authorization_period = request.form.get('authorization_period')
        authorization_place = request.form.get('authorization_place')
        authorization_doc = request.form.get(' authorization_doc')
        authorization_others = request.form.get('authorization_others')
        time_coverage = request.form.get(' time_coverage')
        space_coverage = request.form.get(' space_coverage')
        collection_place = request.form.get(' collection_place')
        collection_company = request.form.get('collection_company')
        call_number = request.form.get('call_number')
        zhengji_people = request.form.get('zhengji_people')
        processing_unit = request.form.get('processing_unit')
        service_way = request.form.get('service_way')
        service_section = request.form.get('service_section')
        service_time = request.form.get(' service_time')
        service_address = request.form.get('service_address')
        service_object = request.form.get(' service_object')
        acceptance_time = request.form.get('acceptance_time')
        acceptance_way = request.form.get('acceptance_way')
        acceptance_people = request.form.get('acceptance_people')
        acceptance_advice = request.form.get('acceptance_advice')
        acceptance_report = request.form.get('acceptance_report')

        # 验证数据
        # if not title: #or not year or len(year) > 4 or len(title) > 60:
        #     flash('Invalid input.')  # 显示错误提示
        #     return redirect(url_for('index'))  # 重定向回主页

        # 若传入不为空，则更新
        if type is not None:
            Resource.update({'type_resources': type})  #
        if path is not None:
            Resource.update({'path_resources': path})  #
        if content is not None:
            Resource.update({'content_resources': content})  #
        if Title is not None:
            Resource.update({'title_resources': Title})  #
        if Author is not None:
            Resource.update({'author_resources': Author})  #
        if Version is not None:
            Resource.update({'version_resources': Version})  #
        if Publication is not None:
            Resource.update({'publication_resources': Publication})  #
        if Date is not None:
            Resource.update({'date_resources ': Date})  #
        if Description is not None:
            Resource.update({'description_resources ': Description})  #
        if Keyword is not None:
            Resource.update({'keyword_resources ': Keyword})  #
        if Form is not None:
            Resource.update({'form_resources ': Form})  #
        if Format is not None:
            Resource.update({'format_resources ': Format})  #
        if Language is not None:
            Resource.update({'language_resources ': Language})  #
        if Audience is not None:
            Resource.update({'audience_resources': Audience})  #
        if Link is not None:
            Resource.update({'link_resources': Link})  #
        if origin is not None:
            Resource.update({'origin_resources': origin})  #
        if Authority is not None:
            Resource.update({'authority_resources': Authority})  #
        if Coverage is not None:
            Resource.update({'coverage_resources': Coverage})  #
        if Source is not None:
            Resource.update({'source_carrier ': Source})  #
        if Collection is not None:
            Resource.update({'collection_information ': Description})  #
        if processing is not None:
            Resource.update({'resource_processing ': processing})  #
        if service is not None:
            Resource.update({'form_resources ': service})  #
        if acceptance is not None:
            Resource.update({'resource_service ': acceptance})  #

        if alternative_title is not None:  ###################3
            Resource.update({'alternative_title': alternative_title})  #
        if parallel_title is not None:
            Resource.update({'parallel_title': parallel_title})  #
        if other_title_information is not None:
            Resource.update({'other_title_information': other_title_information})  #
        if parallel_series_title is not None:
            Resource.update({'parallel_series_title': parallel_series_title})  #
        if series_total is not None:
            Resource.update({'series_total': series_total})  #
        if series is not None:
            Resource.update({'series': series})  #
        if personal_name is not None:
            Resource.update({'personal_name': personal_name})  #
        if team_name is not None:
            Resource.update({'team_name ': team_name})  #
        if meeting_name is not None:
            Resource.update({'meeting_name ': meeting_name})  #
        if parallel_responsibility is not None:
            Resource.update({'parallel_responsibility ': parallel_responsibility})  #
        if other_res_information is not None:
            Resource.update({'other_res_information ': other_res_information})  #
        if responsibility_way is not None:
            Resource.update({'responsibility_way ': responsibility_way})  #
        if publication_place is not None:
            Resource.update({'publication_place ': publication_place})  #
        if publication_people is not None:
            Resource.update({'publication_people': publication_people})  #
        if produce_place is not None:
            Resource.update({'produce_place': produce_place})  #
        if produce_people is not None:
            Resource.update({'produce_people': produce_people})  #
        if photo_date is not None:
            Resource.update({'photo_date': photo_date})  #
        if record_date_vedio is not None:
            Resource.update({'record_date_vedio': record_date_vedio})  #
        if record_date_movie is not None:
            Resource.update({'record_date_movie ': record_date_movie})  #
        if publication_date is not None:
            Resource.update({'publication_date ': publication_date})  #
        if up_date is not None:
            Resource.update({'up_date ': up_date})  #
        if create_date is not None:
            Resource.update({'create_date ': create_date})  #
        if summary is not None:
            Resource.update({'summary ': summary})  #
        if content is not None:
            Resource.update({'content ': content})  #
        if reward is not None:
            Resource.update({'reward': reward})  #
        if singing_style is not None:
            Resource.update({'singing_style': singing_style})  #
        if music_part is not None:
            Resource.update({'music_part': music_part})  #
        if singing_form is not None:
            Resource.update({'singing_form': singing_form})  #
        if playing_form is not None:
            Resource.update({'playing_form': playing_form})  #
        if additional_type is not None:
            Resource.update({'additional_type': additional_type})  #
        if additional_des is not None:
            Resource.update({'additional_des': additional_des})  #
        if channel_id is not None:
            Resource.update({'channel_id ': channel_id})  #
        if channel_content is not None:
            Resource.update({'channel_content ': channel_content})  #
        if note is not None:
            Resource.update({'note ': note})  #
        if finding_route is not None:
            Resource.update({'finding_route ': finding_route})  #
        if show_type is not None:
            Resource.update({'show_type ': show_type})  #
        if show_form is not None:
            Resource.update({'show_form ': show_form})  #
        if number is not None:
            Resource.update({'number': number})  #
        if size is not None:
            Resource.update({'size': size})  #
        if time is not None:
            Resource.update({'time': time})  #
        if enter_point is not None:
            Resource.update({'enter_point': enter_point})  #
        if standard is not None:
            Resource.update({'standard': standard})  #
        if width_height is not None:
            Resource.update({'width_height ': width_height})  #
        if voice_character is not None:
            Resource.update({'voice_character ': voice_character})  #
        if color is not None:
            Resource.update({'color ': color})  #
        if subtitle_form is not None:
            Resource.update({'subtitle_form ': subtitle_form})  #
        if resolution_ratio is not None:
            Resource.update({'resolution_ratio ': resolution_ratio})  #
        if Audio_format is not None:
            Resource.update({'Audio_format ': Audio_format})  #
        if voice_quality is not None:
            Resource.update({'voice_quality': voice_quality})  #
        if picture_quality is not None:
            Resource.update({'picture_quality': picture_quality})  #
        if audio_programming_format is not None:
            Resource.update({'audio_programming_format': audio_programming_format})  #
        if audio_data_ratio is not None:
            Resource.update({'audio_data_ratio': audio_data_ratio})  #
        if audio_frequency is not None:
            Resource.update({'audio_frequency': audio_frequency})  #
        if audio_depth is not None:
            Resource.update({'audio_depth': audio_depth})  #
        if movie_programming_format is not None:
            Resource.update({'movie_programming_format': movie_programming_format})  #
        if movie_sampling_format is not None:
            Resource.update({'movie_sampling_format ': movie_sampling_format})  #
        if movie_data_ratio is not None:
            Resource.update({'movie_data_ratio ': movie_data_ratio})  #
        if document_format is not None:
            Resource.update({'document_format ': document_format})  #
        if channel_language is not None:
            Resource.update({'channel_language ': channel_language})  #
        if subtitle_id is not None:
            Resource.update({'subtitle_id ': subtitle_id})  #
        if subtitle_language is not None:
            Resource.update({'subtitle_language ': subtitle_language})  #
        if obtain_way is not None:
            Resource.update({'obtain_way': obtain_way})  #
        if provider is not None:
            Resource.update({'provider': provider})  #
        if origin_version is not None:
            Resource.update({'origin_version': origin_version})  #
        if other_version is not None:
            Resource.update({'other_version': other_version})  #
        if include is not None:
            Resource.update({'include': include})  #
        if being_included is not None:
            Resource.update({'being_included ': being_included})  #
        if reference is not None:
            Resource.update({'reference ': reference})  #
        if being_refered is not None:
            Resource.update({'being_refered ': being_refered})  #
        if copyright_owner is not None:
            Resource.update({'copyright_owner ': copyright_owner})  #
        if copyright_shengming is not None:
            Resource.update({'copyright_shengming ': copyright_shengming})  #
        if authorization_user is not None:
            Resource.update({'authorization_user ': authorization_user})  #
        if authorization_usage is not None:
            Resource.update({'authorization_usage': authorization_usage})  #
        if authorization_date is not None:
            Resource.update({'authorization_date': authorization_date})  #
        if authorization_period is not None:
            Resource.update({'authorization_period': authorization_period})  #
        if authorization_place is not None:
            Resource.update({'authorization_place': authorization_place})  #
        if authorization_doc is not None:
            Resource.update({'authorization_doc': authorization_doc})  #
        if authorization_others is not None:
            Resource.update({'authorization_others': authorization_others})  #
        if time_coverage is not None:
            Resource.update({'time_coverage': time_coverage})  #
        if space_coverage is not None:
            Resource.update({'space_coverage ': space_coverage})  #
        if collection_place is not None:
            Resource.update({'collection_place ': collection_place})  #
        if collection_company is not None:
            Resource.update({'collection_company ': collection_company})  #
        if call_number is not None:
            Resource.update({'call_number ': call_number})  #
        if zhengji_people is not None:
            Resource.update({'zhengji_people ': zhengji_people})  #
        if processing_unit is not None:
            Resource.update({'processing_unit ': processing_unit})  #
        if service_way is not None:
            Resource.update({'service_way': service_way})  #
        if service_section is not None:
            Resource.update({'service_section': service_section})  #
        if service_time is not None:
            Resource.update({'service_time': service_time})  #
        if service_address is not None:
            Resource.update({'service_address': service_address})  #
        if service_object is not None:
            Resource.update({'service_object': service_object})  #############
        if acceptance_time is not None:
            Resource.update({'acceptance_time ': acceptance_time})  #
        if acceptance_way is not None:
            Resource.update({'acceptance_way ': acceptance_way})  #
        if acceptance_people is not None:
            Resource.update({'acceptance_people ': acceptance_people})  #
        if acceptance_advice is not None:
            Resource.update({'acceptance_advice ': acceptance_advice})  #
        if acceptance_report is not None:
            Resource.update({'acceptance_report ': acceptance_report})  #

        db.session.commit()  # 提交改动
        flash('Item edit.')  # 显示成功创建的提示
        return {'success': True}  # 重定向回主页
    return {'success': False}
