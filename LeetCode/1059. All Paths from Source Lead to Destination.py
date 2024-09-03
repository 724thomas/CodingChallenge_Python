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
    boolean dfs(Map<Integer, List<Integer>> graph, int node, int destination, int[]visited) {
        if (visited[node] != 0) {
            return visited[node] == 2;
        }

        if (!graph.containsKey(node)){
            return node == destination;
        }

        visited[node] = 1;

        for (int neighbor : graph.get(node)) {
            if (!dfs(graph, neighbor, destination, visited)) {
                return false;
            }
        }

        visited[node] = 2;
        return true;
    }

    public boolean leadsToDestination(int n, int[][] edges, int source, int destination) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] edge : edges){
            int u = edge[0], v = edge[1];
            if (!graph.containsKey(u)){
                graph.put(u, new ArrayList());
            }
            graph.get(u).add(v);
        }

        int[] visited = new int[n];
        return dfs(graph, source, destination, visited);
    }
}'''