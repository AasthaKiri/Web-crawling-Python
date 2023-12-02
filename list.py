import requests
import json
response= requests.get('https://directory6.org/categ_tree_ajax.php?action=categtree')
data = response.json()
# parse_json = json.loads(data)
for i in range(len(data)):
    print(data[i]["title"])

def getList(dataJson):
    if dataJson != 'undefined' and dataJson != 'null' and len(dataJson)>0 :
        for i  in range(len(dataJson)):
            title = dataJson[i]["title"]
            key = dataJson[i]["key"]
            # print(key)
            subResponse = requests.get('https://directory6.org/categ_tree_ajax.php?key='+key+'&action=categtree')
            subdata = subResponse.json()
            # print({title:subdata})
            
            for i in range(len(subdata)):
                # print({title:subdata[i]["title","key"]})
                print({title: subdata[i]["title"], 'key':subdata[i]["key"]})
                if subdata != 'undefined' and subdata != 'null' and len(subdata)>0 :
                    # print({title:subdata[i]["title"]})
                    getList(subdata)
getList(data)