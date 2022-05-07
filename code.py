#import this file into the main file
def Show(input):
  print(input)
def Type(input):
  if type(input)==str:
    return "Character"
  if type(input)==int:
    return "Integer"
  if type(input)==float:
    return "Decimal"
def Add_List(list, element):
  list.append(element)
def Insert_List(list, element, index):
  list.insert(index-1, element)
