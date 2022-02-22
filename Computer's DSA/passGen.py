from random import sample

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
nums = '0987654321'

alpha = ''.join(sample(alpha, 4))
nums = ''.join(sample(nums, 3))

password = alpha + nums + '@'
password = ''.join(sample(password, 8))
print(password)
