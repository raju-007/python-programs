import time
def time_fun(func):
	def wrapper(*args,**kargs):
		start=time.time()
		result=func(*args,**kargs)
		end=time.time()
		print(str(end-start)*1000)
		return result
	return wrapper
@time_fun
def ca_sqr(num):
	result=[]
	for n in num:
		result.append(n*n)
	return result
array=range(1-10000000000)
ob=ca_sqr(array)


