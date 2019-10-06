# https://leetcode.com/problems/unique-morse-code-words/
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        l = []
        for w in words:
            s = ""
            for c in w:
                s += d[c]
            l.append(s)
        return len(set(l))