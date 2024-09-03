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
    private void dfs(int[][] grid, int row, int col, StringBuilder shape, String direction) {
        if (row < 0 || row >= grid.length || col < 0 || col >= grid[0].length || grid[row][col] == 0) {
            return;
        }

        grid[row][col] = 0; // 방문 처리
        shape.append(direction); // 이동 방향 기록

        // DFS를 사용하여 상하좌우 탐색
        dfs(grid, row + 1, col, shape, "D"); // 아래로 이동
        dfs(grid, row - 1, col, shape, "U"); // 위로 이동
        dfs(grid, row, col + 1, shape, "R"); // 오른쪽으로 이동
        dfs(grid, row, col - 1, shape, "L"); // 왼쪽으로 이동

        shape.append("B"); // 백트래킹 표시
    }

    public int numDistinctIslands(int[][] grid) {
        int n = grid.length, m = grid[0].length;
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};
        HashSet<String> islands = new HashSet<>();

        for (int row=0; row<n; row++) {
            for (int col=0; col<m; col++) {
                if (grid[row][col] == 1) {
                    StringBuilder shape = new StringBuilder();
                    dfs(grid, row, col, shape, "O");
                    islands.add(shape.toString());

                }
            }
        }
        // for (String island : islands) {
        //     System.out.println(island);
        // }
        return islands.size();
        

        
    }
}'''