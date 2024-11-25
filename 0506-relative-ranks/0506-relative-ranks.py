class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        rank = ['Gold Medal', 'Silver Medal', 'Bronze Medal'] + list(map(str, range(4, len(score) + 1)))
        
        result = [None] * len(score)
        
        for rank_idx, (idx, _) in enumerate(sorted_score):
            print(rank_idx, idx)
            result[idx] = rank[rank_idx]
        
        return result
