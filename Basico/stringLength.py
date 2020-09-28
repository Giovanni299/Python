def lengthOfLongestSubstring(s):
        value = ''
        valueTemp = ''
        for i, letter in enumerate(s):
            #print(i, s[i:])
            valueTemp = letter
            #print('----------',valueTemp)
            for j, letter2 in enumerate(s[i+1:]):
                #print('>>>', valueTemp, letter2)
                if letter2 in valueTemp:
                    value = valueTemp if len(valueTemp) > len(value) else value
                    break

                valueTemp += letter2
                #print('====', valueTemp)
            
            value = valueTemp if len(valueTemp) > len(value) else value

        #print('****', value)      
        return len(value)

def main():    
    s = 'abcabcbb'
    print(lengthOfLongestSubstring(s))
    s = 'bbbbb'
    print(lengthOfLongestSubstring(s))
    s = 'pwwkew'
    print(lengthOfLongestSubstring(s)) 

if __name__ == "__main__":
    main()