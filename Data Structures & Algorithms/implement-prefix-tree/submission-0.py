class PrefixTree:

    def __init__(self):
        self.words = {}
        

    def insert(self, word: str) -> None:
        currentDictionary = self.words
        lastChar = ""
        for c in word:
            lastChar = c
            if c in currentDictionary:
                currentDictionary = currentDictionary[c]
            else:
                nextDictionary = {}
                currentDictionary[c] = nextDictionary
                currentDictionary = nextDictionary
        
        currentDictionary["/"] = {}
            


    def search(self, word: str) -> bool:
        currentDictionary = self.words
        for c in word:
            if c in currentDictionary:
                currentDictionary = currentDictionary[c]
            else:
                return False
        
        return "/" in currentDictionary 
        

    def startsWith(self, prefix: str) -> bool:
        currentDictionary = self.words
        for c in prefix:
            if c in currentDictionary:
                currentDictionary = currentDictionary[c]
            else:
                return False
        
        return True
        
        