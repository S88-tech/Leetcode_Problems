class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        ans=0
        for s in sentences:
            word=s.count(" ")+1
            ans=max(ans,word)
        return ans    

        