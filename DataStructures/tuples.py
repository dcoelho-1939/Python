# Tuples are also one way of storing multiple values within a variable,
# just like a list. The difference is that with tuples you can't change 
# each value inside of it.

example = ("Davi", "Nayara", "Liara")
# if we try to do something like example[0] = "David" an error will occur.

# We can also work with duplicates and ordered values.
# The only actual difference is that a tuple is unchangeable.
# If we declare a tuple, we can't redeclare anything inside that tuple
# again. That's why its unchangeable.

example2 = ("Davi", "Nayara", "Liara", "Liara")
for i in example2:
    print(i)
