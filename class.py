# creating class
class car():
    pass


# creating object
honda = car()
maruthi = car()

# creating attributes to object
honda.model = ' crv '
honda.price = 200000

maruthi.model = 'ritz'
maruthi.price = 100000

print(honda.__dict__)
print(maruthi.__dict__)
