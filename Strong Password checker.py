class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        
        #declare a flag for passworg
        
        if len(password) < 8:
            return False
        
        #at least one lower flag
        flag_lower = False
        for ele in password:
            if ele.islower():
                flag_lower = True
        
        #at least one upper flag
        flag_upper = False
        for ele in password:
            if ele.isupper():
                flag_upper = True
                
        #at least one digit
        flag_digit = False
        for ele in password:
            if ele.isdigit():
                flag_digit = True
                
        #at least one special
        special_flag = False
        for ele in password:
            if ele in "!@#$%^&*()-+":
                special_flag = True
        
        #no adjacent charaters
        trail = password[0]
        flag_adjacent = True
        for ele in password[1:]:
            if trail == ele:
                return False
            else:
                trail = ele
        
       
        
        return flag_lower and flag_upper and flag_digit and special_flag and flag_adjacent
        