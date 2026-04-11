import requests
url = "https://dummyjson.com/products"
response = requests.get(url)
print("Status Code:", response.status_code)
data = response.json()
print("Number of products:", len(data['products']))
print("First product:", data['products'][0])