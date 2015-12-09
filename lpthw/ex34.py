# -*- coding: utf-8 -*-

'''
ex34.py
Accessing Elements of Lists
'''

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

'''
Let's do some check with Python code.
'''
# 1. The animal at 1.
# The animal at 1 is the second and is a python.
print animals[1]

# 2. The 3rd animal.
# The 3rd animal is at 2 and is a peacock.
print animals[2]

# 3. The 1st animal.
# The 1st animal is at 0 and is a bear.
print animals[0]

# 4. The animal at 3.
# The animal at 3 is the 4th and is a kangaroo.
print animals[3]

# 5. The 5th animal.
# The 5th animal is at 4 and is a whale.
print animals[4]

# 6. The animal at 2.
# The animal at 2 is the 3rd animal and is a peacock.
print animals[2]

# 7. The 6th animal.
# The 6th animal is at 5 and is a platypus.
print animals[5]

# 8. The animal at 4.
# The animal at 4 is the 5th animal and is a whale.
print animals[4]


'''
Key points:
1. Python starts counting at 0.
2. Notice the gap between ordinal(1st, 2nd, ...) and cardinal(0, 1, ...).
'''