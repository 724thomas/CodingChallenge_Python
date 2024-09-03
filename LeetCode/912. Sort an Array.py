#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


'''class Solution {
    void mergeSort(int[] nums, int low, int high){
        if (low < high) {
            int mid = low + (high - low) / 2;

            mergeSort(nums, low, mid);
            mergeSort(nums, mid+1, high);

            merge(nums, low, mid, high);
        }
    }
    
    void merge(int[] nums, int low, int mid, int high) {
        int n1 = mid - low + 1;
        int n2 = high - mid;

        int[] left = new int[n1];
        int[] right = new int[n2];

        System.arraycopy(nums, low, left, 0, n1);
        System.arraycopy(nums, mid+1, right, 0, n2);

        int i = 0, j = 0;
        int k = low;
        while (i < n1 && j < n2) {
            if (left[i] <= right[j]) {
                nums[k] = left[i];
                i ++;
            } else {
                nums[k] = right[j];
                j ++;
            }
            k++;
        }

        while (i < n1) {
            nums[k] = left[i];
            i++;
            k++;
        }
        while (k <n2) {
            nums[k] = right[j];
            j++;
            k++;
        }
    }


    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length-1);
        return nums;
    }
}
'''