import requests

"""def get_phone(name):
    print(name)
    phone = requests.get(f'http://localhost:5000/api?action=phone&name={name}')
    print("hej " + phone)

    return  #phone.text
    """
    
    
def get_name(phone):
    print("hej " + phone)
    name = requests.get(f'http://localhost:5000/api?action=name&phone={phone})
    return name.text
    
def get_phone(name):
    print("hej " + phone)
    phone = requests.get(f'http://localhost:5000/api?action=phone&name={name})
    return phone.text