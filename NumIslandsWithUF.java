public class NumIslandsWithUF {
    public static void main (String[] arg) {


        char[][] grid = {{'1','1','1','1','0'},{'1','1','0','1','0'},{'1','1','0','0','0'},{'0','0','0','0','0'}};
        System.out.println(numIslands(grid));
}

public static int numIslands(char[][] grid){ 

    int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
    int m = grid.length;
    int n = grid[0].length;
    UnionFind uf = new UnionFind(grid);
    for (int i =0; i < m; i++ ) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == '1') {
                for (int[] dir: dirs) {
                    
                    int x = dir[0] + i;
                    int y = dir[1] + j;
                    if (x < 0 || y < 0 || x > m -1 || y > n -1 || grid[x][y] == '0') {
                        continue;
                    }
                    int curId = i * n + j;
                    int nextId = x * n + y;
                    uf.union(curId, nextId);
                }
            }

        }
    }
    return uf.numOfComponents;

}
}
    

