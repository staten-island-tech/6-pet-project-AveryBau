wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

def person(ward):
    staff = {}
    for department["name"] in ward:
         if department in staff:
              staff[department["name"]]
              continue
         else:
              staff[department["name"]] = {
                  
              }
              
    for department, docs in wards.items():
        print(department, docs)

person(wards)


""" def receipt(order):
    the_receipt = {}
    for sushi in order:
        if sushi["name"] in the_receipt:
            the_receipt[sushi["name"]]["quantity"] += 1
            continue
        else:
            the_receipt[sushi["name"]] = {
                "price": sushi["price"],
                "quantity": 1
            }
    for sushi, value in the_receipt.items():
        price = value["price"] * value ["quantity"]
        print(sushi, value["quantity"], price)


receipt(sushi_orders) """
