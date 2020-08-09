"""Find Smallest & largest Number from given list of numbers"""

small = None
large = None
while True:
    s = input("Enter Number: ")
    if s == 'done':
        break
    try:
        i = int(s)
    except:
        print("Invalid input")
        continue

    if small is None: small =i
    elif small > i:  small =i

    if large is None: large =i
    elif large < i: large = i

print ("Maximum is", large )
print ("Minimum is", small )
