import string
def remove_punctuation(text):
  return text.translate(str.maketrans("","", string.punctuation))
input_str = "Hello!!!, he said --- and went."
print(remove_punctuation(input_str))