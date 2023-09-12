class utils:
    def reversed(self,num):
        num_str = str(num)
        rev_str = num_str[::-1]
        rev_num = int(rev_str)
        return rev_num
    def formatter(self,num):
        return bin(num),oct(num)
    
