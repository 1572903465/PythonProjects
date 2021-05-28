import requests
import json

if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    data= {
        'on': 'true',
        'page': '1',
        'pageSize': '15',
        'productName':'',
        'conditionType': '1',
        'applyname':'',
        'applysn':'',
    }
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    json_ids = requests.post(url=url,headers=headers,data=data).json()
    print(json_ids)
    id_list = [] #存储企业的id
    all_data_list= [] #存储所有企业的详情数据
    for dic in json_ids['list']:
        id_list.append(dic['ID'])
    print(id_list)
    # with open('./化妆品.html','w',encoding='utf-8') as fp:
    #     fp.write(page_text)

    # 详情页url ：http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
    # 获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id':id
        }
        detail_json = requests.post(url=post_url,headers=headers,data=data).json()
        print(detail_json,'-----------------ending-----------------')
        all_data_list.append(detail_json)
    #持久化存储
    fp = open('./allData.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)