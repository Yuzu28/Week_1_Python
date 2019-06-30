# Dictionary Example

# def add2(x)
#     return x+2

# myclass = {
#     'hello' : 'world',
#     'add2' : add2,
#     'ducks':{
#         0: 'Donald',
#         1: 'Daffy',
#     },
#     'x': 0,
#     'dir': 'Jonathan',
#     1:11

# }

# # donaldDuck = myclass["ducks"][0]
# # # donaldDuck  = myclass.get("ducks").get(0)
# # print(donaldDuck )



# Dictionary Exercise 1

phonebook_dict = { 
  'Alice': '703-493-1834', 
  'Bob': '857-384-1234', 
  'Elizabeth': '484-584-2923'
}

# print(phonebook_dict["Elizabeth"])

phonebook_dict['Kareem'] = '938-489-1234.'
# print(phonebook_dict)

del phonebook_dict ["Alice"]
phonebook_dict['Bob'] = '968-345-2345'

print(phonebook_dict )











