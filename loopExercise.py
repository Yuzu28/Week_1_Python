

# 1. Sum the Numbers

Number = [1, 2, 3, 4, 5, 6]
sum = sum(Number)
print(sum)

# Solution 2

Number = [1, 2, 3, 4, 5, 6]
result = 0
for x in Number:
    result+= x
    print(result)

# 2. Largest Number

Number = [2,33,1,14,8]
Maximum = max(Number)
print(Maximum)

# 4. Even Numbers
Number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in Number:
    if x % 2 ==0:
        print(x)


# 5. Positive Numbers

Num = [-1, 2, 5, -6, 4, 6, -23]
for x in Num:
    if x > 0:
        print(x)


# 6. Positive Numbers II 
Num = [-1, 2, 5, -6, 4, 6, -23]
new = []
for x in Num:
    if x > 0:
       new.append(x)
print(new)
        

# 7. Multiply a list
mylist = [1, 2, 3, 4, 5, 6]
factor = 5
my_new_list = []
for i in mylist:
    my_new_list.append(i * factor)
print(my_new_list)

# 8. Multiply Vectors
one = [2, 4, 5]
two = [2, 3, 6]
ans=[]
for i in range(0, len(one)):
        ans.append(one[i]*two[i])
print(ans)


# 9. Matrix Addition

Skip








# 11. De-dup (Delete dups)


num = [1, 3, 4, 4, 4, 6, 6, 7, 7, 8, 8]
res = [] 
for i in num: 
    if i not in res: 
        res.append(i)
print(res)

string = ["Jet", "Jedi", "Jedi", "Jof"]
bot = [] 
for i in string: 
    if i not in bot: 
        bot.append(i)
print(bot)


# 1. 1 to 10

for x in range(1,11):
    print(x)



# 2. n to m

x = int(input("Enter a start number"))
y = int(input("Enter a end number"))

for x in range(x,y + 1):
    print(x)



# 3. Odd Numbers



for x in range(1,11):
    if x % 2 ==1:
        print(x)



# 4.Print a Square


stars = "*****"
lines = 0

while lines < 5:
    print(stars)
    lines = lines + 1



# 5. Print a Square II

dim = int(input("Give me a number?"))
stars = "*"
lines = 0

while lines < dim:
    print(stars * dim)
    lines = lines + 1



# 6. Print a Box



width = int(input("Width? "))
height = int(input("Height? "))

star_w = 0
star_h = 0

while star_w < height:
    print(("*") * width)
    while star_h < (height - 2):
        print(("*" + ((" ") * (width - 2)) + "*"))
        star_h = star_h + 1
    star_w = star_w + height
    print(("*") * width)


# 7. Print a Triangle

star = 1
height = int(input("What is the height? "))

print(((" ") * (height - (star))) + (("*") * star) + ((" ") * (height - star)))
while star < height:
    print(((" ") * (height - (star + 1))) + (("*") * (star + 1) + ("*" * star) + ((" ") * (height - (star + 1)))))
    star = star + 1





# 9. Multiplication Table


num_one = 1
num_two = 1
max_num = 10

while num_one <= max_num:
    while num_two <= max_num:
        multiply = num_one * num_two
        print("%d X %d = %d" % (num_one, num_two, multiply))
        num_two += 1
    num_two = 1
    num_one += 1