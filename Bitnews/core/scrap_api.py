import json
import re
import codecs
import logging
import datetime
import io
import sys
# from datetime import datetime, d ate
from bs4 import BeautifulSoup, BeautifulStoneSoup

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core import serializers
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls import url
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.http.response import HttpResponse
from django.db.models.query_utils import Q
from django.db.transaction import atomic

from base_api import CustomBaseModelResource
from utils import generate_unique_customer_id
from .models import UserProfile, Category, Language
from news.models import News, NewsCategory, NewsLanguage
from feeds.models import NewsFeedItems, Feeds


logger = logging.getLogger("bitnews")

#################### Django REST FRAMEWORK API#####################

def keydata(item):
    for key in item:
        try:
            if key=='link':
                d1 = str(item[key])
                d2 = d1.strip("[").strip("]").replace("'","").replace(", u",",\n")
                news_link = d2[1:]
                s1=d1.strip('[').strip('"').replace('http://','').replace("'","").replace("u","")
                source=s1[0:12].title()
            if key=='description':
                d3 = str(item[key])
                # for extracting image url from descrption
                temp = [d3]
                soup = BeautifulSoup(''.join(temp))
                link=soup.find('a')
                try:    
                    image_url=link.contents[0]['src']
                except:
                    image_url=None
                d4 = d3.strip("[").strip("]").replace(",","").replace("'","").replace("\\","")
                temp_desc = d4[1:]
                news_description=re.sub('<[^>]+>', '', temp_desc)
            if key=='title':
                d5 = str(item[key])
                d6 = d5.strip("[").strip("]").replace("'","").replace("\u","").replace('"','')
                news_title = d6[1:]
            if key=='pubdate':
                d7 = str(item[key])
                d8 = d7.strip("[").strip("]").replace("'","")
                news_temp_pubdate = d8[6:-4]
                news_pubdate = datetime.datetime.strptime(news_temp_pubdate,'%d %b %Y %H:%M:%S')
             # news_pubdate = datetime.datetime.strftime(news_pubdate_format,'%a, %d %b %Y %H:%M:%S')
        except:
            break
    proc_data={'news_link':news_link,'source':source,'image_url':image_url,
        'news_description':news_description,'news_title':news_title,
        'news_pubdate':news_pubdate}
    return(proc_data)

@api_view(['GET','POST'])
def read_file(request):
    # import ipdb; ipdb.set_trace()
    filenames = [  '/home/neelesh/Office/Bitnomix/bitnewsscrap/business.json',
                  '/home/neelesh/Office/Bitnomix/bitnewsscrap/cricket.json',
                  '/home/neelesh/Office/Bitnomix/bitnewsscrap/education.json',
                  '/home/neelesh/Office/Bitnomix/bitnewsscrap/entertainment.json',
                  '/home/neelesh/Office/Bitnomix/bitnewsscrap/health.json',
                  '/home/neelesh/Office/Bitnomix/bitnewsscrap/india.json',
                  '/home/neelesh/Office/Bitnomix/bitnewsscrap/lifestyle.json',
                  '/home/neelesh/Office/Bitnomix/bitnewsscrap/sports.json',
                  '/home/neelesh/Office/Bitnomix/bitnewsscrap/tech.json',
                  '/home/neelesh/Office/Bitnomix/bitnewsscrap/world.json',
                ]
################################### Dainik Bhaskar#####################################33

    # with open('/home/neelesh/Office/Bitnomix/bitnewsscrap/newdainik.json', 'r') as f:
    #     json_string = f.read()
    #     f.close()
    #     data = json.loads(json_string)
    #     for item in data:
    #         try:
    #             for key in item:
    #                 if key=='link':
    #                     d1 = item[key]
    #                     d2 = d1.strip("[").strip("]").replace("'","").replace(", u",",\n")
    #                     news_link = d2

    #                 if key=='description':
    #                     d3 = item[key]
    #                     # for extracting image url from descrption
    #                     for i in d3:
    #                         a= codecs.BOM_UTF8 + i.encode("utf-8",errors="ignore")
    #                     d4 = a.replace("&nbsp;"," ") 
    #                     news_description=d4
                    
    #                 if key=='title':
    #                     d0=item[key]
    #                     for i in d0:
    #                         a= codecs.BOM_UTF8 + i.encode("utf-8",errors="ignore")
    #                     d5 = a.replace("&nbsp;"," ")
    #                     news_title = d5
                    
    #                 if key=='image':
    #                     d6=str(item[key])
    #                     d7 = d6.strip("[").strip("]").replace("'","")
    #                     image_url = d7[1:]
    #                     if image_url is None:
    #                         print" This on is empty======================>>>"
    #                 if key=='pubdate':
    #                     d8 = str(item[key])
    #                     d9 = d8.strip("[").strip("]").replace("'","")
    #                     news_temp_pubdate = d9[6:-4]
    #                     news_pubdate = datetime.datetime.strptime(news_temp_pubdate,'%d %b %Y %H:%M:%S')
    #                  # news_pubdate = datetime.datetime.strftime(news_pubdate_format,'%a, %d %b %Y %H:%M:%S')              

    #             try:
    #                 news_cat = NewsCategory.objects.get(name='Business')
    #             except:
    #                 news_cat = NewsCategory(name='Business')
    #                 news_cat.save()
    #             try:
    #                 news_lang = NewsLanguage.objects.get(name='Hindi')
    #             except:
    #                 news_lang = NewsLanguage(name='Hindi')
    #                 news_lang.save()

    #             news_obj= News(title=news_title, content=news_description,source='Dainik Bhaskar', 
    #                                 link=news_link, pubdate=news_pubdate, image_url=image_url,
    #                                 category=news_cat, language=news_lang)
    #             news_obj.save()
    #         except:
    #             continue
########################################LOK SATTA- MARATHI############################
    import ipdb; ipdb.set_trace()
    with open('/home/neelesh/Office/Bitnomix/bitnewsscrap/loksatta.json', 'r') as f:
        json_string = f.read()
        f.close()
        data = json.loads(json_string)
        for item in data:
            try:
                for key in item:
                    if key=='link':
                        d1 = item[key]
                        d2 = d1.strip("[").strip("]").replace("'","").replace(", u",",\n")
                        news_link = d2

                    if key=='description':
                        d3 = item[key]
                        # for extracting image url from descrption
                        for i in d3:
                            a= codecs.BOM_UTF8 + i.encode("utf-8",errors="ignore")
                        d4 = a.replace("&nbsp;"," ") 
                        news_description=d4
                    
                    if key=='title':
                        d0=item[key]
                        for i in d0:
                            a= codecs.BOM_UTF8 + i.encode("utf-8",errors="ignore")
                        d5 = a.replace("&nbsp;"," ")
                        news_title = d5
                    
                    if key=='image':
                        d6=str(item[key])
                        d7 = d6.strip("[").strip("]").replace("'","")
                        image_url = d7[1:]
                        if image_url is None:
                            continue
                    if key=='pubdate':
                        d8 = str(item[key])
                        d9 = d8.strip("[").strip("]").replace("T"," ")
                        news_temp_pubdate = d9[2:-7]
                        news_pubdate = datetime.datetime.strptime(news_temp_pubdate,'%Y-%m-%d %H:%M:%S')

                try:
                    news_cat = NewsCategory.objects.get(name='India')
                except:
                    news_cat = NewsCategory(name='India')
                    news_cat.save()
                try:
                    news_lang = NewsLanguage.objects.get(name='Marathi')
                except:
                    news_lang = NewsLanguage(name='Marathi')
                    news_lang.save()
                print"==========SAB DETAI====", news_title, news_description , news_link, news_cat, news_lang
                news_obj= News(title=news_title, content=news_description,source='Loksatta', 
                                    link=news_link, pubdate=news_pubdate, image_url=image_url,
                                    category=news_cat, language=news_lang)
                news_obj.save()
            except:
                continue

########################################TIMES OF INDIA########################'Times of India'
#     with open(filenames[0], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)
#                 try:
#                     news_cat = NewsCategory.objects.get(name='Business')
#                 except:
#                     news_cat = NewsCategory(name='Business')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Times of India', 
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue

#     with open(filenames[1], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)
#                 try:
#                     news_cat = NewsCategory.objects.get(name='Cricket')
#                 except:
#                     news_cat = NewsCategory(name='Cricket')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Times of India',
#                                 image_url=item['image_url'],link=item['news_link'], pubdate=item['news_pubdate'], 
#                                 category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue

#     with open(filenames[2], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)
#                 try:
#                     news_cat = NewsCategory.objects.get(name='Education')
#                 except:
#                     news_cat = NewsCategory(name='Education')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Times of India',
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)                  
#                 news_obj.save()
#             except:
#                 continue

#     with open(filenames[3], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)            
#                 try:
#                     news_cat = NewsCategory.objects.get(name='Entertainment')
#                 except:
#                     news_cat = NewsCategory(name='Entertainment')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Times of India',
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue

#     with open(filenames[4], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)            
#                 try:
#                     news_cat = NewsCategory.objects.get(name='Health')
#                 except:
#                     news_cat = NewsCategory(name='Health')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Times of India',
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue

#     with open(filenames[5], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)            
#                 try:
#                     news_cat = NewsCategory.objects.get(name='India')
#                 except:
#                     news_cat = NewsCategory(name='India')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Times of India',
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue

#     with open(filenames[6], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)            
#                 try:
#                     news_cat = NewsCategory.objects.get(name='Lifestyle')
#                 except:
#                     news_cat = NewsCategory(name='Lifestyle')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Times of India',
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue

#     with open(filenames[7], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)            
#                 try:
#                     news_cat = NewsCategory.objects.get(name='Sports')
#                 except:
#                     news_cat = NewsCategory(name='Sports')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Times of India',
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue

#     with open(filenames[8], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 try:
#                     item=keydata(items)
#                 except:
#                     continue            
#                 try:
#                     news_cat = NewsCategory.objects.get(name='Tech')
#                 except:
#                     news_cat = NewsCategory(name='Tech')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Times of India',
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue

#     with open(filenames[9], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)            
#                 try:
#                     news_cat = NewsCategory.objects.get(name='World')
#                 except:
#                     news_cat = NewsCategory(name='World')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Times of India',
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue
# ###########################################EconomicTimes Files
#     et_filenames = [ '/home/neelesh/Office/Bitnomix/bitnewsscrap/et-economy.json',
#                   '/home/neelesh/Office/Bitnomix/bitnewsscrap/et-industry.json',
#                   '/home/neelesh/Office/Bitnomix/bitnewsscrap/et-jobs.json',
#                   '/home/neelesh/Office/Bitnomix/bitnewsscrap/et-magazines.json',
#                   '/home/neelesh/Office/Bitnomix/bitnewsscrap/et-markets.json',
#                   '/home/neelesh/Office/Bitnomix/bitnewsscrap/et-smallbiz.json',
#                   '/home/neelesh/Office/Bitnomix/bitnewsscrap/et-tech.json',
#                   '/home/neelesh/Office/Bitnomix/bitnewsscrap/et-wealth.json',
#                 ]

#     with open(et_filenames[0], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)            
#                 try:
#                     news_cat = NewsCategory.objects.get(name='Economy')
#                 except:
#                     news_cat = NewsCategory(name='Economy')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source=item['source'],
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue

#     with open(et_filenames[1], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)            
#                 try:
#                     news_cat = NewsCategory.objects.get(name='Industry')
#                 except:
#                     news_cat = NewsCategory(name='Industry')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Economic Times',
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue

#     with open(et_filenames[2], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)            
#                 try:
#                     news_cat = NewsCategory.objects.get(name='Jobs')
#                 except:
#                     news_cat = NewsCategory(name='Jobs')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Economic Times',
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue

#     with open(et_filenames[3], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)            
#                 try:
#                     news_cat = NewsCategory.objects.get(name='Magazines')
#                 except:
#                     news_cat = NewsCategory(name='Magazines')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Economic Times',
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue

#     with open(et_filenames[4], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)            
#                 try:
#                     news_cat = NewsCategory.objects.get(name='Markets')
#                 except:
#                     news_cat = NewsCategory(name='Markets')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Economic Times',
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue

#     with open(et_filenames[5], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)            
#                 try:
#                     news_cat = NewsCategory.objects.get(name='Smallbiz')
#                 except:
#                     news_cat = NewsCategory(name='Smallbiz')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Economic Times',
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue

#     with open(et_filenames[6], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)            
#                 try:
#                     news_cat = NewsCategory.objects.get(name='Tech')
#                 except:
#                     news_cat = NewsCategory(name='Tech')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Economic Times',
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue

#     with open(et_filenames[7], 'r') as f:
#         json_string = f.read()
#         f.close()
#         data = json.loads(json_string)
#         for items in data:
#             try:
#                 item=keydata(items)            
#                 try:
#                     news_cat = NewsCategory.objects.get(name='Wealth')
#                 except:
#                     news_cat = NewsCategory(name='Wealth')
#                     news_cat.save()
#                 try:
#                     news_lang = NewsLanguage.objects.get(name='English')
#                 except:
#                     news_lang = NewsLanguage(name='English')
#                     news_lang.save()

#                 news_obj= News(title=item['news_title'], content=item['news_description'],source='Economic Times',
#                                     link=item['news_link'], pubdate=item['news_pubdate'],image_url=item['image_url'],
#                                     category=news_cat, language=news_lang)
#                 news_obj.save()
#             except:
#                 continue

    return Response({'message':'News saved succesfully', 'status':200})