# C-5.30
# When Bob wants to send Alice a message M on the Internet, he breaks M
# into n data packets, numbers the packets consecutively, and injects them
# into the network. When the packets arrive at Alice’s computer, they may
# be out of order, so Alice must assemble the sequence of n packets in order
# before she can be sure she has the entire message. Describe an efficient
# scheme for Alice to do this, assuming that she knows the value of n. What
# is the running time of this algorithm?


def full_message_received(lst, length):
    if sum(lst) == (length-1)*length/2:  # indexes start at 0,
        return True                      # therefore replace n by n-1 in the formula n*(n+1)/2
    return False


n = 4
packets_indexes = [3, 1, 2, 0]
print(full_message_received(packets_indexes, n))
