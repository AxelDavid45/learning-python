# 3-4 Guest list
guests = ['Karla', 'Diana', 'Maria Jose']

print("Welcome: " + guests[0])
print("Welcome: " + guests[1])
print("Welcome: " + guests[2])

guest_removed = guests.pop()
guests.pop()  # Removing the 2nd element
guests.pop()  # Removing the 3rd element
print("We removed to our list to: " + guest_removed)
print(guests)  # All the elements has been removed
