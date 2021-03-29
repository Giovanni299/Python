import collections

def perfectTeam(skills):
    physics = skills.count('p')
    chemistry = skills.count('c')
    math = skills.count('m')
    botany = skills.count('b')
    zoology = skills.count('z')

    return min(physics, chemistry, math, botany, zoology)


    

print(perfectTeam('pcmbzpcmbz')) #2
print(perfectTeam('mppzbmbpzcbmpbmczcz')) #3
print(perfectTeam('pcmpp')) #0