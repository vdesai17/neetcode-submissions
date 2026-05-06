class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        for s in strs:
            fingerprint = [0] * 26
            for char in s:
                fingerprint[ord(char) - ord('a')] += 1
            result[tuple(fingerprint)].append(s)

        return list(result.values())       
