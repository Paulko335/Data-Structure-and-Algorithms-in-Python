# R-5.9
# Explain the changes that would have to be made to the program of Code
# Fragment 5.11 so that it could perform the Caesar cipher for messages
# that are written in an alphabet-based language other than English, such as
# Greek, Russian, or Hebrew


#encoder[k] = chr((k + shift) % 26 + ord('A'))
#decoder[k] = chr((k - shift) % 26 + ord('A'))

print("""
The original encoder and decoder use ord('A').
To use it in another language, simply replace the letter A 
with the first letter of the new alphabet.""")