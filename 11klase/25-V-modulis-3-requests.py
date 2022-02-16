import requests

def vienkarss_get(url):   
    r = requests.get(url)
    r.status_code
    if r.status_code == 200:
        print('Success!')
        print("statusa kods: {}".format(r.status_code))
        print("HTML dokuments: {}".format(r.text))

    elif r.status_code == 404:
        print('Not Found.')
vienkarss_get("https://python.org")
