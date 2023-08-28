def sort_data(data, sorting_parameter):

  """Sorts the data in the given list according to the specified sorting parameter.

 

  Args:

    data: The list of data to be sorted.

    sorting_parameter: The sorting parameter. 1 for age, 2 for name, and 3 for salary.

 

  Returns:

    The sorted list of data.

  """

 

  if sorting_parameter == 1:

    data.sort(key=lambda x: x["age"])

  elif sorting_parameter == 2:

    data.sort(key=lambda x: x["name"])

  elif sorting_parameter == 3:

    data.sort(key=lambda x: x["salary"])

  else:

    raise ValueError("Invalid sorting parameter")

 

  return data

 

def main():

  """Reads the data from the table and sorts it according to the user's choice."""

 

  data = [

      {"employee_id": "161E90", "name": "Raman", "age": 41, "salary": 56000},

      {"employee_id": "161F91", "name": "Himadri", "age": 38, "salary": 67500},

      {"employee_id": "161F99", "name": "Jaya", "age": 51, "salary": 82100},

      {"employee_id": "171E20", "name": "Tejas", "age": 30, "salary": 55000},

      {"employee_id": "171G30", "name": "Ajay", "age": 45, "salary": 44000},

  ]

 

  print("Select the sorting parameter:")

  print("1. Age")

  print("2. Name")

  print("3. Salary")

 

  sorting_parameter = int(input())

 

  sorted_data = sort_data(data, sorting_parameter)

 

  print("The sorted data is:")

  for employee in sorted_data:

    print(employee)

 

if _name_ == "_main_":

  main()