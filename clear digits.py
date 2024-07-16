class Solution:
    def clearDigits(self, s: str) -> str:
        
        #storage place for new string
        storage = []
        
        for ele in s:
            if ele.isdigit():
                while storage and storage[-1].isdigit():
                    storage.pop()
                if storage:
                    storage.pop()
            else:
                storage.append(ele)
        
        return "".join(storage)
        