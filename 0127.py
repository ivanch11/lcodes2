class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        print ("wordlist1", wordList)
        wordList = set(wordList)
        print ("wordlist2", wordList)
        dq = collections.deque([[beginWord, 1]])
        while dq:
            word, length = dq.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    candidate = word[:i] + c + word[i+1:]
                    if candidate in wordList:
                        wordList.remove(candidate)
                        dq.append([candidate, length + 1])
        return 0    