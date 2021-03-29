# A control device has 4 buttons that can be used to move a character around a screen in 4 directions: Up(U), Down (D), Left (L), 
# and Right (R). The movement needs to be optimized by deleting unnecessary instructions while maintaining the same destination. 
# Given the original set of instructions, what is the maximum number that can be deleted and still have the character reach the 
# destination? Note: The instructions that are deleted do not need to be contiguous

def getMaxDeletions(s):
    # u = s.count('U')
    # d = s.count('D')
    # r = s.count('R')
    # l = s.count('L')

    u=d=r=l= 0
    for i in s:
        if i == 'U':
            u += 1
        elif i == 'D':
            d += 1
        elif i == 'R':
            r += 1
        else:
            l += 1

    return (min(u,d) + min(r,l))*2

print(getMaxDeletions('URDR')) #2
print(getMaxDeletions('RRR')) #0
print(getMaxDeletions('RUDRL')) #4