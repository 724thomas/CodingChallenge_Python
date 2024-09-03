#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


'''
import java.util.*;
class Solution {
    public boolean checkPossibility(int[] nums) {
        boolean found = false;
        int cmax = -Integer.MAX_VALUE;

        for (int i=0; i<nums.length-1; i++) {
            if (nums[i] > nums[i+1]) {
                if (found) {
                    return false;
                }
                found = true;
                if (nums[i+1] < cmax){
                    nums[i+1] = nums[i];
                    cmax = nums[i];
                }
            } else {
                cmax = Math.max(cmax, nums[i]);
            }
        }
        return true;
    }
}'''