import requests
import json

payload = {'Nombre':'Gio', 'Curso':'Python'}

##Consume metodo GET.
def methodGet():
    url = 'http://httpbin.org/get'
    response = requests.get(url, params=payload)
    #print(response.url)

    if (response.status_code == 200):
        content = response.content
        file = open('content.json', 'wb')
        file.write(content)
        file.close()

        dataJson = response.json()
        origin = dataJson['origin']
        urlJson = dataJson['url']
        print('*****GET: ' + origin + '  ' + urlJson)

##Consume metodo POST.
def methodPost():
    url = 'http://httpbin.org/post'
    headers = {'Content-type':'json','Access-token':'12345'}
    response = requests.post(url, json=payload, headers=headers)
    
    if (response.status_code == 200):
        #print(json.dumps(json.loads(response.content), indent=1))
        headersResponse = response.headers
        print(headersResponse)

if __name__ == "__main__":
    #methodGet()
    methodPost()
