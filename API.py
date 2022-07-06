import requests

def get_phone(var):
    phone = requests.get(f'http://localhost:5000/api?action=phone&name={variable1}')
    return phone.text
    
def get_name(var):
    name = requests.get(f'http://localhost:5000/api?action=name&phone=0435-4355438')
    return name.text