#!/usr/bin/env python
# coding: utf-8

# In[25]:


def string_to_binary(string):
    binary_data = ""
    for char in string:
        code_point = ord(char)
        binary_representation = bin(code_point)[2:].zfill(8)
        binary_data += binary_representation
    return binary_data
def binary_to_string(binary):    
    binary_substrings = [binary[i:i+8] for i in range(0, len(binary), 8)]
    result = ''.join([chr(int(substring, 2)) for substring in binary_substrings])
    return result   
input_string = input("Enter a string: ")
binary_result = string_to_binary(input_string)
coded_seq=[]
DSSS=[]
encoder=[1,0,0,0,0,0,0,0,0,0,1]
inverted_list = [1 if bit == 0 else 0 for bit in encoder]
for x in binary_result:
    if x=='1':
        coded_seq.extend(int(x) for x in encoder)
    else:
        coded_seq.extend(int(x) for x in inverted_list)       
error=int(input("Enter the rate of error:"))
error_data= ''.join(['1' if bit == '0' and (i+1) % error == 0 else '0' if bit == '1' and (i+1) % error == 0 else bit for i, bit in enumerate(binary_result)])
error_seq=[1 if bit == 0 and (i+1) % error == 0 else 0 if bit == 1 and (i+1) % error == 0 else bit for i, bit in enumerate(coded_seq)]
for i in range(0,len(binary_result)*11,11):
    count=error_seq[i:i+10].count(1)
    DSSS.append('1' if count<=5 else '0')
DSSS=''.join(DSSS)    
num_differences = sum(c1 != c2 for c1, c2 in zip(DSSS,binary_result))
num_differences2= sum(c1 != c2 for c1, c2 in zip(error_data,binary_result))
print("Accuracy of Data using DSSS:%.2f" %((len(binary_result)-num_differences)/len(binary_result)*100))
print("Accuracy of Data without using DSSS:%.2f" %((len(binary_result)-num_differences2)/len(binary_result)*100))
print("The data from DSSS:",binary_to_string(DSSS))
print("The data from error_data:",binary_to_string(error_data))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




