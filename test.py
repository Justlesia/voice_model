import requests

url = 'http://localhost:9696/2015-03-31/functions/function/invocations'

# data = {'url': 'http://drive.google.com/uc?export=download&id=1vDIdGhxcp-2XgKgqVWZGnweLHj3IOueY'}  # no
data = {'url': 'http://drive.google.com/uc?export=download&id=1H2osnRRUN4b1Uge_cLE0_ki81iDjtqci'}  # yes

result = requests.post(url, json=data).json()
print(result)
