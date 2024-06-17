import json

customer = {
    "id": 1234,
    "name": "장원영",
    "history": [
        {"date" : "2024-06-17", "product" : "iPhone 14 Pro"},
        {"date" : "2045-06-18", "prodect" : "Galaxy S24 Ultra"},
    ]
}

json_string = json.dumps(customer, ensure_ascii=False)
print((json_string))
