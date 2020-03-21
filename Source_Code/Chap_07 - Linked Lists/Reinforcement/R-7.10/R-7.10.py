# R-7.10
# There seems to be some redundancy in the repertoire of the positional
# list ADT, as the operation L.add first(e) could be enacted by the alternative
# L.add before(L.first( ), e). Likewise, L.add last(e) might be performed
# as L.add after(L.last( ), e). Explain why the methods add first
# and add last are necessary.