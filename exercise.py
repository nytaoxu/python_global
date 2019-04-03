from pprint import pprint

sentence = "This is a common interview question"
dict = {}
for letter in sentence:
    if letter == ' ':
        continue
    if letter in dict:
        dict[letter] += 1
    else:
        dict[letter] = 1

# print("dict[" "] =", dict.get(" ", None))

result_key = ""
result_value = -1
for key, value in dict.items():
    if value > result_value:
        result_key = key
        result_value = value

print("The most common character is", result_key,
      ", and it appears", result_value, "times.")
print(dict)
pprint(dict)
pprint(sorted(dict.items(), key=lambda item: item[1], reverse=True)[0])
