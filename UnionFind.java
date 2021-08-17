public class UnionFind {

    int[] parent;
    int m, n;
    int numOfComponents;

    UnionFind(char[][] grid) {
        this.m = grid.length;
        this.n = grid[0].length;
        this.parent = new int[m * n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j <n; j++) {
                if (grid[i][j] == '1') {
                    int id = i * n +j;
                    parent[id] = id;
                    numOfComponents++;
                }


            }
        }
    }

    public void union(int node1, int node2) {
        int root1 = find(node1);
        int root2 = find(node2);
        if (root1 != root2) {
            // Parents are not the same, so they are disconnected components
            // Make the root of this
            parent[root1] = root2;
            numOfComponents--;
        }

    }

    public int find(int node) {
        if (parent[node] == node) {
            return node;
        }
        while (parent[node] != node) {
            node = parent[node];
        }
        return node;
    }

}