""" ATTEMPT 1 - Failed

def string_compression(text_input):
    text_input = text_input.lower()
    
    word_list = text_input.split(' ')
    str_list = []
    
    for word in word_list:
        str_list.append(list(word))

    for s, word in enumerate(str_list):
        repeat_count = 0
        repeat_index = []
        for i in range(0, len(word)-2): 
            print (i, word[i])
            for k in range(i+1, len(word)-1):
                print (k, word[k])
                if word[i] == word[k]:
                    repeat_index.append(k)
                    repeat_count += 1
                    print (f"repeat count {repeat_count}")
                    break
                else:
                    break
        temp_word = word

        if len(repeat_index) == 0:
            pass
        else:
            for x,y in enumerate(repeat_index):
                if x == 0 and (repeat_index[x+1] - repeat_index[x] = 1):
                    temp_word[repeat_index[x]] = len(repeat_index) + 1
                else:
                    temp_word.pop(y)
        str_list[s] = temp_word
        print (str_list)                    
string_compression('shoppping and mississippi and swimming to test it')
"""

def string_compression(text_input):
    text_input = text_input.lower()   
    output_list = []
    i = 1

    for idx, letter in enumerate(text_input):
        
        if idx == 0:
            output_list.append(letter)
            continue
        
        if letter == output_list[-1]:
            i += 1
            continue
            
        elif i > 1:
            output_list.append(str(i))
            output_list.append(letter)
            i = 1
            
        else:
            output_list.append(letter)
            
                
    return ''.join(output_list)
    
print (string_compression('misssippi and swimming')) 