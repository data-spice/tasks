# Functions

# def greet():
#     print("Hello peris")

# greet()
# greet()

####    FUNCTIONS WITH A PARAMETER

# def greet_any(name):
#     print(f"Hello {name}")


# greet_any("Peris")
# greet_any("Victor")

####    FUNC WITH MULTIPLE PARAMETERS

# def id(name,phone_no):
#     return (f"Name: {name}  Phone Number: {phone_no}")

# print(id("David",24555262728))
# id("Kush ", 12345)

## Kwargs **  args *
## Return value

def sum(*a):
    sum=0
    for number in a:
        sum = sum+number
    return sum

print(sum(1))

    

    