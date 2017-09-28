def reverse(input_string):
  index = len(input_string) - 1
  result=''
  for _ in input_string:
    result += input_string[index]
    index -= 1
  return result


def minimum_value(array):
  minimum_value = array[0]
  for value in array:
    if minimum_value >= value:
      minimum_value = value
      
  return minimum_value


def find_average(array_avarage):
  sum = 0
  for i in range(len(array_avarage)):
    sum += array_avarage[i]
    
  return sum / len(array_avarage)

ivan = {
  "name":"ivan",
  "age": 34,
  "children": [{
    "name": "vasja",
    "age":12,
    }, {
      "name": "petja",
      "age": 10,
    
  }],
}

darja = {
  "name": "darja",
  "age": 41,
  "children": [{
    "name": "kirill",
    "age": 21,
    }, {
      "name": "pavel",
      "age": 15,
  }],
}
nikolay = {
  "name": "nikolay",
  "age": 54,
  "children": [{
    "name": "dmitryi",
    "age": 31,
    }, {
      "name": "victor",
      "age": 19,
  }],
}

emps = [ivan, darja, nikolay]


def find (emps):
  result = []
  for emp in emps:
    if 'children' in emp:
        for x in emp['children']:
          if x['age'] >= 18:
            result.append(emp['name'])
            break
  return result 
 
result = find(emps)
print(result)
      




def main():
  print(reverse('HELLO WORLD'))
  print(minimum_value([5,8,6,5,95,654,54,356,84,652,
  3,563,536,656,85,42,67,112,]))
  print(find_average([23,63,144,56,25,78,2,245,63,747,856,23,53,646,753,112,34,511,996,344,665]))
  find(emps)

main()