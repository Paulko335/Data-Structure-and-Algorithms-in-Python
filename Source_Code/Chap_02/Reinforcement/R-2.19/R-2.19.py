# R-2.19
# When using the ArithmeticProgression class of Section 2.4.2 with an increment
# of 128 and a start of 0, how many calls to next can we make
# before we reach an integer of 2^63 or larger?

# We start at 0 and each increments adds 128
# Therefore the number of steps is : 2^63 // 128
#                                  = 2^63 // 2^7
#                                  = 2^(63 - 7)
#                                  = 2^56
#                                  = 72 057 594 037 927 936