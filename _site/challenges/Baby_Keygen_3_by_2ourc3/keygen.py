import random
import string

def create_random_string():
    s = ['A'] + [random.choice(string.ascii_letters + string.digits) for _ in range(10)]  
    s[3] = '-'  
    s[7] = '-'
    return ''.join(s)

result = create_random_string()
print(result)  
