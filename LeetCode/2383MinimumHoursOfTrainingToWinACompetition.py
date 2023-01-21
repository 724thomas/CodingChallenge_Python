#https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        en=initialEnergy
        ex=initialExperience
        hour=0
        for i in range(len(energy)):
            if en<=energy[i]:
                add=energy[i]-en+1
                en+=add
                hour+=add
            if ex<=experience[i]:
                add=experience[i]-ex+1
                ex+=add
                hour+=add
            en-=energy[i]
            ex+=experience[i]
        return hour