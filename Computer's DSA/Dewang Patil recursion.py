'''
Name: Dewang Patil
Clg: LNCT, Bhopal
Branch: CSE
Enroll: 0103CS181050

Adv.Python assignment:-
'''


# recursive reversal of string:-

def reverse(st):
    
    if len(st) == 0:
        return ""
    if len(st) == 1:
        return st
    
    return st[len(st)-1] + reverse(st[:len(st)-1])



st = input()
print(reverse(st))

##################################################################

# check palindrome recursivly:-

def palin(st):
    
    if len(st) <= 1:
        return 'palindrome'

    if st[0] == st[len(st)-1]:
        return palin(st[1:len(st)-1])
    else:
        return 'not palindrome'



st = input()
print(palin(st))