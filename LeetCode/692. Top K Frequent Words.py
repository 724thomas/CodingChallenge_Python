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
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> map = new HashMap<>();
        for (String word : words) {
            map.put(word, map.getOrDefault(word, 0)+1);
        }

        List<String> sortedList = new ArrayList<>(map.keySet());
        Collections.sort(sortedList, (word1, word2) -> {
            int freq1 = map.get(word1);
            int freq2 = map.get(word2);

            if (freq1 == freq2) {
                return word1.compareTo(word2);
            }

            return freq2 - freq1;
        });

        return sortedList.subList(0, k);

    }
}'''