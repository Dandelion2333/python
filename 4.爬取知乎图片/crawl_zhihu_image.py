# -*- coding: utf-8 -*-

import requests
import json
import time
import re
import os
import datetime
import pandas as pd
from urllib import parse
from lxml import html

UrlDataCnt = 1
SaveImageCnt = 1
ObjectUrlPage = 0
LastImage = 0

QuestionId = 1
DefaultFolder = "download-zhihu-image"
DownloadFolder = "NewFolder"

def SelectModel():
    DownloadMode = input("please input download model(default model is 0, ID model is 1):")
    #print("DownloadMode is ",DownloadMode)
    return DownloadMode

def DefualtMode():
    global DownloadFolder
    global QuestionId
    DownloadFolder = DefaultFolder      # default save folder
    QuestionId = 297715922              # default id

def InputMessage():
    global QuestionId
    global DownloadFolder

    QuestionId = input("please input id:")
    DownloadFolder = input("please input folder name:")

    # print("Id:", QuestionId)
    # print("folder name:", DownloadFolder)

def MakeDir():
    if not os.path.exists(DownloadFolder):
        print("create the path successful")
        os.mkdir(DownloadFolder)
    else:
        print("the path is exist")
 
def GetHtmlData(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
 
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        return r.text
    
    except requests.HTTPError as e:
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unknown Error !")
        
def ParseHtmlData(html):
    JsonData = json.loads(html)['data']
    #print("JsonData:", JsonData)
    UrlData = []
    
    try:
        for item in JsonData:
            #print("item:",item)
            Formula = "(ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?" 

            Content = item['content']          
            print("Content", Content)

            p = re.compile(Formula)
            iterator = p.finditer(Content)
            for match in iterator:
                #print(match.span())
                #print(match.group())
                UrlData.append(match.group())
                print("match:",match.group())

        return UrlData
    
    except Exception as e:
        print("error")
        
def SaveImage(Image):
    global SaveImageCnt
    ImageName = str(SaveImageCnt) + ".jpg"
    SaveImageCnt = SaveImageCnt + 1

    ImagePath = os.path.join(DownloadFolder, ImageName)
    with open(ImagePath, 'wb') as  f:
        #print('Output:', ImagePath)
        f.write(Image)

def ParseImageData(ImageUrl):
    resp = requests.get(ImageUrl)
    Image = resp.content
    #print("Image:",Image)
    # remove the same picture
    global LastImage
    if LastImage != Image:
        SaveImage(Image)
    LastImage = Image
    
def ParseImageUrlData(UrlData):
    global UrlDataCnt
    for Url in UrlData:
        print("Url:", Url)
        ParseImageData(Url)
        # if UrlDataCnt % 4 == 0:
        #     #print("Url:", Url)
        #     #ParseImageData(Url)
        # UrlDataCnt += 1     

def GetObjectUrl():
    # print("ObjectUrlPage:", ObjectUrlPage)
    # print("QuestionId:", QuestionId)

    ObjectUrl = "https://www.zhihu.com/api/v4/questions/"+str(QuestionId)+"/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset="+str(ObjectUrlPage)+"&platform=desktop&sort_by=default"

    return ObjectUrl
 
def DataProcessing():
    global ObjectUrlPage

    # get object-url
    ObjectUrl = GetObjectUrl()

    # get totals number
    Html = GetHtmlData(ObjectUrl)
    UrlTotals = json.loads(Html)['paging']['totals']
    print("UrlTotals:",UrlTotals)
    print('---'*10)
      
    # Traverse all URLs
    while(ObjectUrlPage < UrlTotals):
        # get data from object-url
        Html = GetHtmlData(ObjectUrl)
        ImageUrlData = ParseHtmlData(Html)
        ParseImageUrlData(ImageUrlData)

        # get object-url
        ObjectUrlPage += 5
        ObjectUrl = GetObjectUrl()
        
    
if __name__ == '__main__':
    Model = SelectModel()       # select download model
    if Model == '1':
        InputMessage()          # input message from you
    else:
        DefualtMode()  

    MakeDir()           # create folder 
    
    DataProcessing()    # data processing 

    print("finish")