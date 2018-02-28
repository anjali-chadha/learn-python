class WordPatter:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split(' ')
        pattern_list = list(pattern)
        
        m = len(str_list)
        n = len(pattern_list)
    
        if m != n:
            return False
        
        pattern_dict = {}
        pattern_set = set()
        
        for i in range(m):
            key = str_list[i]
            value = pattern_list[i]
            if key in pattern_dict.keys():
                v = pattern_dict.get(key)
                if v != value: 
                    return False
            elif value in pattern_set:
                return False
            else:
                pattern_dict[key] = value
                pattern_set.update(value)
        return True
                
                
                
            
