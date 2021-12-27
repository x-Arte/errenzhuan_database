from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy  #
from mypassword import pwd
from flask import jsonify
from flask import request, url_for, redirect, flash,render_template
app = Flask(__name__)
#初始化扩展，传入程序实例 app
#连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] =f"mysql+pymysql://root:{pwd}@localhost:3306/mydb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class administrator(db.Model):
    __table_args__ = {'extend_existing': True}
    id_administrator = db.Column(db.Integer, primary_key=True, nullable=False)
    name_administrator = db.Column(db.String(45), )
    paw_administrator = db.Column(db.String(45), )

    def __init__(self, id,admin_dict):
        self.id_administrator = id
        for attr in admin_dict.keys():
            if admin_dict[attr]:
                setattr(self, attr, admin_dict[attr])
    def to_dict(self, admin_dict):
        temp = admin_dict.copy()
        temp["id_administrator"] = self.id_administrator
        for attr in admin_dict.keys():
            temp[attr] = getattr(self,attr)
        return temp

class recources(db.Model):
    __table_args__ = {'extend_existing': True}
    id_resources = db.Column(db.Integer, primary_key=True, nullable=False)
    type_resources = db.Column(db.String(45), )
    path_resources = db.Column(db.String(1024), )
    content_resources = db.Column(db.Text, )
    title_resources = db.Column(db.String(45), )
    author_resources = db.Column(db.String(45), )
    version_resources = db.Column(db.String(45), )
    publication_resources = db.Column(db.String(45), )
    date_resources  = db.Column(db.String(45), )
    description_resources = db.Column(db.String(45), )
    keyword_resources = db.Column(db.String(45), )
    form_resources = db.Column(db.String(45), )
    format_resources = db.Column(db.String(45), )
    language_resources = db.Column(db.String(45), )
    audience_resources = db.Column(db.String(45), )
    origin_resources = db.Column(db.String(45), )
    link_resources= db.Column(db.String(45), )
    authority_resources = db.Column(db.String(45), )
    coverage_resources = db.Column(db.String(45), )
    source_carrier = db.Column(db.String(45), )
    collection_information = db.Column(db.String(45), )
    resource_processing= db.Column(db.String(45), )
    resource_service = db.Column(db.String(45), )
    resources_acceptance = db.Column(db.String(45), )
    alternative_title = db.Column(db.String(45), )
    parallel_title = db.Column(db.String(45), )
    other_title_information = db.Column(db.String(45), )
    parallel_series_title= db.Column(db.String(45), )
    series_total = db.Column(db.String(45), )
    series = db.Column(db.String(45), )
    personal_name = db.Column(db.String(45), )
    team_name = db.Column(db.String(45), )
    meeting_name = db.Column(db.String(45), )
    parallel_responsibility = db.Column(db.String(45), )
    other_res_information = db.Column(db.String(45), )
    responsibility_way = db.Column(db.String(45), )
    publication_place = db.Column(db.String(45), )
    publication_people= db.Column(db.String(45), )
    produce_place = db.Column(db.String(45), )
    produce_people = db.Column(db.String(45), )
    photo_date = db.Column(db.String(45), )
    record_date_vedio = db.Column(db.String(45), )
    record_date_movie = db.Column(db.String(45), )
    publication_date = db.Column(db.String(45), )
    up_date = db.Column(db.String(45), )
    create_date = db.Column(db.String(45), )
    summary = db.Column(db.String(45), )
    content = db.Column(db.String(45), )
    reward = db.Column(db.String(45), )
    singing_style = db.Column(db.String(45), )
    music_part = db.Column(db.String(45), )
    singing_form = db.Column(db.String(45), )
    playing_form = db.Column(db.String(45), )
    additional_type= db.Column(db.String(45), )
    additional_des = db.Column(db.String(45), )
    channel_id = db.Column(db.String(45), )
    channel_content = db.Column(db.String(45), )
    note = db.Column(db.String(45), )
    finding_route = db.Column(db.String(45), )
    show_type = db.Column(db.String(45), )
    show_form = db.Column(db.String(45), )
    number = db.Column(db.String(45), )
    size = db.Column(db.String(45), )
    time = db.Column(db.String(45), )
    enter_point = db.Column(db.String(45), )
    standard = db.Column(db.String(45), )
    width_height = db.Column(db.String(45), )
    voice_character = db.Column(db.String(45), )
    color = db.Column(db.String(45), )
    subtitle_form = db.Column(db.String(45), )
    resolution_ratio = db.Column(db.String(45), )
    Audio_format = db.Column(db.String(45), )
    voice_quality = db.Column(db.String(45), )
    picture_quality = db.Column(db.String(45), )
    audio_programming_format = db.Column(db.String(45), )
    audio_data_ratio = db.Column(db.String(45), )
    audio_frequency = db.Column(db.String(45), )
    audio_depth = db.Column(db.String(45), )
    movie_programming_format = db.Column(db.String(45), )
    movie_sampling_format = db.Column(db.String(45), )
    movie_data_ratio = db.Column(db.String(45), )
    document_format = db.Column(db.String(45), )
    channel_language = db.Column(db.String(45), )
    subtitle_id = db.Column(db.String(45), )
    subtitle_language = db.Column(db.String(45), )
    obtain_way = db.Column(db.String(45), )
    provider = db.Column(db.String(45), )
    origin_version = db.Column(db.String(45), )
    other_version = db.Column(db.String(45), )
    include = db.Column(db.String(45), )
    being_included = db.Column(db.String(45), )
    reference = db.Column(db.String(45), )
    being_refered = db.Column(db.String(45), )
    copyright_owner = db.Column(db.String(45), )
    copyright_shengming = db.Column(db.String(45), )
    authorization_user = db.Column(db.String(45), )
    authorization_usage = db.Column(db.String(45), )
    authorization_date = db.Column(db.String(45), )
    authorization_period= db.Column(db.String(45), )
    authorization_place = db.Column(db.String(45), )
    authorization_doc = db.Column(db.String(45), )
    authorization_others = db.Column(db.String(45), )
    time_coverage = db.Column(db.String(45), )
    space_coverage = db.Column(db.String(45), )
    collection_place= db.Column(db.String(45), )
    collection_company = db.Column(db.String(45), )
    call_number = db.Column(db.String(45), )
    zhengji_people = db.Column(db.String(45), )
    processing_unit = db.Column(db.String(45), )
    service_way = db.Column(db.String(45), )
    service_section = db.Column(db.String(45), )
    service_time = db.Column(db.String(45), )
    service_address= db.Column(db.String(45), )
    service_object= db.Column(db.String(45), )
    Acceptance_time= db.Column(db.String(45), )
    Acceptance_way= db.Column(db.String(45), )
    Acceptance_people= db.Column(db.String(45), )
    Acceptance_advice= db.Column(db.String(45), )
    Acceptance_report= db.Column(db.String(45), )


    def __init__(self, id,valuedict):
        self.id_resources = id
        for attr in valuedict.keys():
            if valuedict[attr]:
                setattr(self, attr, valuedict[attr])

    def to_dict(self, valuedict):
        temp = valuedict.copy()
        temp["id_resources"] = self.id_resources
        for attr in valuedict.keys():
            temp[attr] = getattr(self, attr)
        return temp

admin_dict = {
    'name_administrator' :None,
    'paw_administrator' :None
}
valuedict = {
    'type_resources' :None,
  'path_resources' :None,
  'content_resources':None,
  'title_resources' :None,
  'author_resources' :None,
  'version_resources' :None,
  'publication_resources' :None,
  'date_resources' :None,
  'description_resources' :None,
  'keyword_resources' :None,
  'form_resources' :None,
  'format_resources' :None,
  'language_resources' :None,
  'audience_resources' :None,
  'origin_resources' :None,
  'link_resources' :None,
  'authority_resources' :None,
  'coverage_resources' :None,
  'source_carrier' :None,
  'collection_information' :None,
  'resource_processing' :None,
  'resource_service' :None,
  'resources_acceptance' :None,
  'alternative_title' :None,
  'parallel_title' :None,
  'other_title_information' :None,
  'parallel_series_title' :None,
  'series_total' :None,
  'series' :None,
  'personal_name' :None,
  'team_name' :None,
  'meeting_name' :None,
  'parallel_responsibility' :None,
  'other_res_information' :None,
  'responsibility_way' :None,
  'publication_place' :None,
  'publication_people' :None,
  'produce_place' :None,
  'produce_people' :None,
  'photo_date' :None,
  'record_date_vedio' :None,
  'record_date_movie' :None,
  'publication_date' :None,
  'up_date' :None,
  'create_date' :None,
  'summary' :None,
  'content' :None,
  'reward' :None,
  'singing_style' :None,
  'music_part' :None,
  'singing_form' :None,
  'playing_form' :None,
  'additional_type' :None,
  'additional_des' :None,
  'channel_id' :None,
  'channel_content' :None,
  'note' :None,
  'finding_route' :None,
  'show_type' :None,
  'show_form' :None,
  'number' :None,
  'size' :None,
  'time' :None,
  'enter_point' :None,
  'standard' :None,
  'width_height' :None,
  'voice_character' :None,
  'color' :None,
  'subtitle_form' :None,
  'resolution_ratio' :None,
  'Audio_format' :None,
  'voice_quality' :None,
  'picture_quality' :None,
  'audio_programming_format' :None,
  'audio_data_ratio' :None,
  'audio_frequency' :None,
  'audio_depth' :None,
  'movie_programming_format' :None,
  'movie_sampling_format' :None,
  'movie_data_ratio' :None,
  'document_format' :None,
  'channel_language' :None,
  'subtitle_id' :None,
  'subtitle_language' :None,
  'obtain_way' :None,
  'provider' :None,
  'origin_version' :None,
  'other_version' :None,
  'include' :None,
  'being_included' :None,
  'reference' :None,
  'being_refered' :None,
  'copyright_owner' :None,
  'copyright_shengming' :None,
  'authorization_user' :None,
  'authorization_usage' :None,
  'authorization_date' :None,
  'authorization_period' :None,
  'authorization_place' :None,
  'authorization_doc' :None,
  'authorization_others' :None,
  'time_coverage' :None,
  'space_coverage' :None,
  'collection_place' :None,
  'collection_company' :None,
  'call_number' :None,
  'zhengji_people' :None,
  'processing_unit' :None,
  'service_way' :None,
  'service_section' :None,
  'service_time' :None,
  'service_address' :None,
  'service_object' :None,
  'Acceptance_time' :None,
  'Acceptance_way' :None,
  'Acceptance_people' :None,
  'Acceptance_advice' :None,
  'Acceptance_report' :None
}

admin_res = {
    'id_resources': 0,
    'title_resources' : None,
    'path_resources' :  None
}