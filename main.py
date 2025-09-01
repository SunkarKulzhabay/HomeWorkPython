#Task 4
text = 'In the hole in the ground there lived a hobbit'
text1 = text.lower()
a = text1.find('h')
b = text1.rfind('h')
print(text[:a] + text[b+1:] )

