class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        #create a list of words
        str_split1 = s1.split()
        str_split2 = s2.split()
        
        #initlize a counter objects
        counter_dict1 = Counter(str_split1)
        counter_dict2 = Counter(str_split2)
        lst = []
        
        #create a loop that loops though word in list and checks if its the list.
        for key in counter_dict1:
            if counter_dict1[key] == 1 and counter_dict2[key] == 0:
                lst.append(key)
        
        for key in counter_dict2:
            if counter_dict2[key] == 1 and counter_dict1[key] == 0:
                lst.append(key)
        
                
        return lst

        
        
        
       