public class UnionFind {
    int[] ranks;
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
                    ranks[id] = 1;
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

    public void unionWithRank(int node1, int node2) {
        int root1 = find(node1);
        int root2 = find(node2);
        if (root1 != root2) {
            if (ranks[root1] > ranks[root2]) {
                parent[root2] = root1;

            } else if (ranks[root1] < ranks[root2]) {
                parent[root1] = root2;
            } else {
                // Doesn't matter which we set the parent to, just need to make sure to increase the rank
                parent[root2] = root1;
                ranks[root1]++;
            }
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

    public int findWithPathCompression(int node) {
        int oldId = node;
        while (parent[node] != node) {
            node = parent[node];
        }
        parent[oldId] = node;
        return node;
    }


}