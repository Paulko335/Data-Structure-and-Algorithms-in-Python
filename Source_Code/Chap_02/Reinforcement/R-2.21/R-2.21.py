# R-2.21
# What are some potential efficiency disadvantages of having very shallow
# inheritance trees, that is, a large set of classes, A, B, C, and so on, such
# that all of these classes extend a single class, Z?

# The class Z must be very generic (very few methods implemented).
# Therefore, child classes are going to need many methods. and possibly redundent ones
y