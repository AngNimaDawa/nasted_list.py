#nasted list
# employee_info =[['nima','20',1000.0],['om','baneshower',23,15000.0],]
# for info in employee_info:
# 	print(info,type(info))

# m = [1,2,3],[4,5,6],[7,8,9]
# for row in m:
# 	print(row)

#task
# number_of_elements = int(input('enter the no of elements:'))
# num_list = []
# num2_list = []
# for i in range(number_of_elements)
# 	elements = int((input))
# 	num_list.append(elements)
# 	num2_list.append(elements**2)
# 	print(num_list)
# 	print(num2_list)
# question no 1
# g = [4,5,6]
# r = []
# for i in g:
# 	r.append(i**2)
 
# print(r)


# question no 2 
# m = [[1,2,3],
# 	[4,5,6],
# 	[7,8,9],]
# r = []
# for row in m:
# 	t = []
# 	for col in row:
# 		t.append(col**2)
# 	r.append(t)

# print(r)
# for row in g:
# 	t = []
# 	for col in row:
# 		t.append(col**2)
# 		r.append(t)
# 		print(r)

# list comprehension
# a = [1,2,3,4]
# r = [i**2 for i in a]

# print(r)


# names = ['nima','roshan','sabuz','santosh',]
# result = [name.capitalize() for name in names]
# print(result)
# m = [[1,2,3],
#       [4,5,6],
#       [7,8,9],]
# r = [col**2 for row in m for col in row]
# print(r)
# # r = [[col**2 for col in row]for row in m]
# print(r)

# multiples = [i for i in range(1,31) if i % 3 is 0]
# print(multiples)



#if elements is divisible by 3 then square of elements else as it is using list comprehension.
# data = range(1, 10)
# result = [i**2 if i % 3 is 0 else i for i in data]
# print(result)
