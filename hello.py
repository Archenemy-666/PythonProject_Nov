
print("hello world");

a = 23;
b = 33;

print(a,b);	

#immutable strings tuples numbers

c = 22.43
print(c);

#condition statements 

if(a>b):

	print("a is greater");

elif(b>c):

	print("b is greater");


else:

	print("c is greater");

# tuples 

tuple = (a,b,1.2,'string');
print(tuple);

#mutable data types : Lists , Dictionaries and Sets 

lists = [a, b, c, 24.23, 'sid'];
print(lists);
print(lists[2]);

dict = {'name' : 'sid' , 'age' : '22' , 'gender' : 'male'}
for i in dict:
	if(i.key() == 'name'):
		print(i);
