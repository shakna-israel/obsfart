from obsfart import Obsfart

f = Obsfart()

print("Add a list of integers:")
print(f.a([1,1,1,1,1,1,1,1,1,1,1]))

print("Add two integers:")
print(f.a(1,1))

print("\n\nA more realistic list example:")
il = [1,6,9,12,8]
print(f.a(il))
