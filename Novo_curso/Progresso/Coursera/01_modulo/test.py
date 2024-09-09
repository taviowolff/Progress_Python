# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# pos = data.find('.')
# print(data[pos:pos+3])

text = "X-DSPAM-Confidence: 0.8475"

x = text.find(' ')
print(x) # o espaço está no 19

num_str = text[19:]
num_float = float(num_str)
