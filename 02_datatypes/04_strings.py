childrens = 12
fruits = 48
print(f"{fruits} fruits will be given to {childrens} childrens.")

random_string = "hello there! how are you?"
print(random_string[:])
print(random_string[4:])
print(random_string[:4])
print(random_string[::1])
print(random_string[::2])
print(random_string[::-1]) # reverse

print("----------------- encode/decode -------------------------")
special_string = "é è ê ë"
print(special_string)
encoded_string = special_string.encode("utf-8")
print(encoded_string)
decoded_string = encoded_string.decode("utf-8")
print(decoded_string)
