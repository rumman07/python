
# coding: utf-8

# In[5]:


#Write a function to return most frequesntly occuring number 
def most_freq(array): 
    max_count = -1
    max_item = None 
    count = {}
    for i in array : 
        if i not in count : 
            count[i] = 1
        else: 
            count[i] += 1
        if count[i] > max_count : 
            max_count = count[i]
            max_item = i
    return max_item
    
    
print(most_freq([1, 3, 1, 2, 1, 1]))


# In[6]:


#Return coomon elem in two given arrays
def common_elem(arr1, arr2): 
    result = []
    p1 = 0
    p2 = 0 
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] == arr2[p2]: 
            result.append(arr1[p1])
            p1 += 1
            p2 += 1
        elif arr1[p1] > arr2[p2]: 
            p2 += 1
            
        else: 
            p1 +=1
    return result 

common_elem([1, 3, 4, 6, 9], [1, 2, 4, 5, 9, 10])
        


# In[8]:


def is_rotation(list1, list2):
    if len(list1) != len(list2):
        return False
    key = list1[0]
    key_loc = -1
    for i in range(len(list2)):
        if list2[i] == key:
            key_loc = i
            break
        if key_loc == -1:
            return False
    for i in range(len(list1)):
        j = (key_loc + i) % len(list1)
        if list1[i] != list2[j]:
            return False
    return True

print(is_rotation([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 1, 2, 3]))


# In[11]:


#No repeating character in a string 
def non_rep(str): 
    char_count = {}
    for c in str: 
        if c not in char_count: 
            char_count[c] = 1
        else: 
            char_count[c] += 1
            
    for c in str: 
        if char_count[c] == 1: 
            return c
    return None

print(non_rep("aabbdbc"))


# In[13]:


#Write a function that takes two strings and  returns True if they are one away from each other 
def is_one_away(str1, str2): 
    if len(str1) - len(str2) >= 2 or len(str2) - len(str1) >= 2:
        return False 
    elif len(str1) == len(str2):
        return is_one_away_same_length(str1, str2)
    elif len(str1) > len(str2): 
        return is_one_away_diff_length(str1, str2)
    else: 
        return is_one_away_diff_length(str2, str1)
    

def is_one_away_same_length(str1, str2): 
    count_diff = 0 
    for i in range(len(str1)): 
        if not str1[i] == str2[i]:
            count_diff += 1
            if count_diff > 1:
                return False 
    return True 

def is_one_away_diff_length(str1, str2): 
    i = 0 
    count_diff = 0 
    while i < len(str2): 
        if str1[i + count_diff] == str2[i]: 
            i += 1
        else: 
            count_diff += 1
            if count_diff > 1: 
                return False 
    return True 

        
print(is_one_away("abcde", "abcd"))


# In[172]:



a = [["a", "b", "c", "d"], 
     [1, 1, 0, 0],
     [0, 0, 1, 1], 
     [0, 0, 1, -1]]

for i in range(4):
    print(a[i][0],a[i][1], a[i][2], a[i][3])
   


# In[ ]:




