import sys, re
sys.path.append('E:\\Spider\\movie')
from flask import Flask, render_template
from flask import Blueprint, request
from flask_sqlalchemy import SQLAlchemy 
from learn.models.movie import Movie
from learn.search import data_search
from learn.models.movie import db 

web = Blueprint('web', __name__)

@web.route('/', methods=['GET', 'POST'])
def test():
    
    #获取爬取到的名字，磁力链接，封面，介绍
    # names, links, images, introductions = data_search.data_get()

    # #将数据映射到数据库中
    # for name, link, image, introduction in zip(names, links, images, introductions):
    #     if not Movie.query.filter_by(name=str(name)).first():
    #         movie = Movie(name=str(name), link=str(link), image=str(image), introduction=str(introduction))
    #         db.session.add(movie)
    #         db.session.commit()
    
    return render_template('/search.html')
     

@web.route('/search', methods=['POST', 'GET'])
def search():
    postData = request.form # 利用request对象获取POST请求数据
    #获取所有的匹配信息(模糊搜索)
    all_results = Movie.query.filter(
            Movie.name.like("%" + postData['name'] + "%") if postData['name'] is not None else ""
        ).all()
    
    Data = []
    sum = 0

    for x in all_results:
        data = []
        
        data_name = x.name
        data_link = x.link
        data_image = x.image
        data_introduction = x.introduction 
        print(data_introduction)
        re.sub('&middot;', '', data_introduction)
        print(data_introduction)
        data.append(data_name)
        data.append(data_link)
        data.append(data_image)
        data.append(data_introduction)
        
        Data.append(data)
        sum += 1
    
    return render_template('/result.html', data=Data, sum=sum) 


