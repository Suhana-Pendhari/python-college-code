# 3.Bitwise Operation Practice
# Take two integers and show the result of:
# •	Bitwise AND (&)
# •	Bitwise OR (|)
# •	Bitwise XOR (^)
# •	Bitwise NOT (~) for each number

a,b = map(int, input("Enter two numbers: ").split())

print("-----Bitwise Operation Practice-----")
print("a AND b: ", a&b)
print("a OR b: ", a|b)
print("a XOR b: ", a^b)
print("~ a: ", ~a)
print("~ b: ", ~b)
print("------------------------------------")
