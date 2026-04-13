wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

def person(ward):
    staff = {}
    for dept, docs in ward.items():    # for the items in the wards             
       for doc in docs:                # in all the doctors
           if doc not in staff:        # if the doctors are not in the dictionary
               staff[doc] = [dept]     # format of the dictionary, the doctor = [list of jobs]
           else:   # when it is in the dictionary
               staff[doc].append(dept)  # add all the occupations into the list by adding the depts
    print(staff["Bob"]) # print the new dictionary
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
