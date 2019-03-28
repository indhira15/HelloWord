
palabra=input("Palabra: ")
vocales=['a','e','i','o','u']
count=[0,0,0,0,0]
for i in palabra:
	if i in vocales:
		count[vocales.index(i)]=count[vocales.index(i)]+1

print(vocales)
print(count)
	
