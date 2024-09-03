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
    int[] parent;
    int[] rank;

    int find(int p) {
        if (parent[p] != p) {
            parent[p] = find(parent[p]);
        }
        return parent[p];
    }

    boolean union(int a, int b){
        int ra = find(a);
        int rb = find(b);
        if (ra == rb) {
            return true;
        }
        if (rank[ra] > rank[rb]) {
            parent[rb] = ra;
        } else if (rank[ra] < rank[rb]) {
            parent[ra] = rb;
        } else {
            parent[rb] = ra;
            rank[ra]++;
        }

        return false;
    }

    public int earliestAcq(int[][] logs, int n) {
        Arrays.sort(logs, (a,b) -> Integer.compare(a[0], b[0]));
        parent = new int[n];
        rank = new int[n];
        for (int i=0; i<n; i++) {
            parent[i] = i;
            rank[i] = 1;
        }

        int friends = n-1;
        for (int[] log : logs){
            int time = log[0], u = log[1], v = log[2];
            if (!union(u,v)){
                friends--;
            }
            if (friends==0) {
                return time;
            }
        }

        return -1;
    }
}'''