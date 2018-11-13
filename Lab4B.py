#Isaiah Hernandez
#80591211
#Last Date Modified 11/12/18
class HashTableNode:
    def __init__(self, word, next):
        self.item = word
        self.next = next

class HashTable:
    def __init__(self, size):
        
        self.table = [None] * size
        
    def hash(self, k, count):
        return k % len(self.table)

    def insert(self, word, count):
        global comparisons
        loc = self.hash(word, count)
        
        if self.table[loc] != None:
            comparisons +=1
            
        self.table[loc] = HashTableNode( word, self.table[loc] )
        
    def get_load_factor(self): 
        
        num_elements = 0
        for i in range(len(self.table)):
            temp = self.table[i]

            while temp is not None:
                num_elements +=1
                temp = temp.next
        return num_elements / len(self.table)    
    def search(self, word, count):
        
        loc = self.hash(count,word)
        temp = self.table[loc]
        
        while temp!= None:
            if temp.item == word:
                return True
            temp = temp.next
        return False
        

def count_anagrams(word, hashtable, prefix="" ):
    num = getIntValue(word)
    english_words = hashtable
    global count
    
    if len(word) <= 1:
        str = prefix + word
        if english_words.search(str, num) == True: 
            count+=1

           
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur
            if cur not in before: # Check if permutations of cur have not been generated.
                count_anagrams(before + after,hashtable, prefix + cur)          
                
def getIntValue(word): #figures out the intger value of a word
    count = 0
    temp = list(word)
    for i in range(len(temp)):
            count += ord(temp[i])
    return count            

tot = 0
words = []
maxList = []
comparisons = 0
count = 0
node = HashTableNode(None, next)
with open("l.txt", 'r') as file: #used to find the total amount of words in the file
    for word in file:
        tot+=1
wordTable = HashTable(tot)
with open("l.txt", 'r') as file: #puts words in hash table and list 
    for word in file:
        P = word.split("\n")
        words.append(P[0])
        node.item = (P[0])
        count = getIntValue(node.item)           
        wordTable.insert(count ,node)

    



print("The load factor is", wordTable.get_load_factor())
print("The Average comparisons is", comparisons/tot)
word = "spot" #input("Enter your word! ")
count_anagrams(word, wordTable)
print("Total amount of anagrams is " + str(count))
for i in range(len(words)):
    count = 0
    count_anagrams(words[i], wordTable)
    maxList.append(count)
    print(count)
maxWord = maxList[0]
actual_word = words[0]
for i in range(1 ,len(words)): #finds word with the greatest amount of anagrams
    if maxList[i] > maxWord:
        maxWord = maxList[i]
        actual_word = words[i]
print(actual_word + " has the most anagrams with " + str(maxWord))





