// Project 5b: Solving graph colring using steepest descent
//             and adv. local search algorithm
// Jae Hoon Kim and Victor Liang

#include <iostream>
#include <limits.h>
#include "d_except.h"
#include <fstream>

#include <boost/graph/adjacency_list.hpp>

#include <cmath>
#include <unordered_map>

#define LargeValue 99999999
#define clockdiff(x) (float)(clock()-x)/CLOCKS_PER_SEC

using namespace std;
using namespace boost;

//int const NONE = -1;  // Used to represent a node that does not exist
int g_numColor = -1;

struct VertexProperties;
struct EdgeProperties;

typedef adjacency_list<vecS, vecS, bidirectionalS, VertexProperties, EdgeProperties> Graph;

struct VertexProperties
{
    pair<int,int> cell; // maze cell (x,y) value
    Graph::vertex_descriptor pred;
    bool visited;
    bool marked;
    int weight;
};

// Create a struct to hold properties for each edge
struct EdgeProperties
{
    int weight;
    bool visited;
    bool marked;
};

//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
void setNodeWeights(Graph &, int);
void setNodeVisited(Graph &, bool);
void setNodeMarked(Graph &, bool);

void initializeGraph(Graph &g, ifstream &fin)
// Initialize g using data from fin.
{
    int n, e;
    int j,k;
    
    fin >> g_numColor >> n >> e;
    Graph::vertex_descriptor v;
    
    // Add nodes.
    for (int i = 0; i < n; i++)
        v = add_vertex(g);
    
    for (int i = 0; i < e; i++)
    {
        fin >> j >> k;
        add_edge(j,k,g);  // Assumes vertex list is type vecS
        add_edge(k,j,g);  // Needed for fast coloring
    }
    
    setNodeWeights(g, INT_MIN);
    setNodeVisited(g, false);
    setNodeMarked(g, false);
}

void inline setNodeWeights(Graph &g, int w)
// Set all node weights to w.
{
    pair<Graph::vertex_iterator, Graph::vertex_iterator> vItrRange = vertices(g);
    for (Graph::vertex_iterator vItr= vItrRange.first; vItr != vItrRange.second; ++vItr) g[*vItr].weight = w;
}

void inline setNodeVisited(Graph &g, bool b)
// Set all node visited to b.
{
    pair<Graph::vertex_iterator, Graph::vertex_iterator> vItrRange = vertices(g);
    for (Graph::vertex_iterator vItr= vItrRange.first; vItr != vItrRange.second; ++vItr) g[*vItr].visited = b;
}

void inline setNodeMarked(Graph &g, bool b)
// Set all node marked to b.
{
    pair<Graph::vertex_iterator, Graph::vertex_iterator> vItrRange = vertices(g);
    for (Graph::vertex_iterator vItr= vItrRange.first; vItr != vItrRange.second; ++vItr) g[*vItr].marked = b;
}

void inline resetNodes(Graph &g, int w = 0, bool v = false, bool m = false)
{
    setNodeWeights(g, w);
    setNodeVisited(g, v);
    setNodeMarked(g, m);
}

// int checkConflicts(...)
// Description: Checks the number of conflicts.
// Limitations: none.
// Assumptions: Valid graph
int checkConflicts(Graph &g)
{
    int conflictCount = 0;
    pair<Graph::vertex_iterator, Graph::vertex_iterator> vItrRange = vertices(g);
    
    setNodeVisited(g, false);
    
    // Loop over all nodes in the graph
    for (Graph::vertex_iterator vItr = vItrRange.first; vItr != vItrRange.second; ++vItr)
    {
        g[*vItr].visited = true;
        
        // Get a pair containing iterators pointing to the beginning and end of the list of nodes adjacent to node v
        pair<Graph::adjacency_iterator, Graph::adjacency_iterator> ad_vItrRange = adjacent_vertices(*vItr, g);
        
        if (g[*vItr].weight == INT_MIN) {
            for (Graph::adjacency_iterator ad_vItr = ad_vItrRange.first; ad_vItr != ad_vItrRange.second; ++ad_vItr)
                if (!g[*ad_vItr].visited)
                    ++conflictCount;
        }
        else {
            // Loop over adjacent nodes in the graph
            for (Graph::adjacency_iterator ad_vItr = ad_vItrRange.first; ad_vItr != ad_vItrRange.second; ++ad_vItr)
                if ( (!g[*ad_vItr].visited && g[*vItr].weight == g[*ad_vItr].weight) )
                    ++conflictCount;
        }
    }
    
    setNodeVisited(g, false);
    
    return conflictCount;
}

// int greedyColoring(...)
// Description: Greedy way of finding the somtimes optimal solution.
// Limitations: Does not save the best coloring found if time limit exceeds. (easy add-on)
// Assumptions: Valid graph, valid colors, and valid time limit.
int greedyColoring(Graph &g, int numColors, int t)
{
    clock_t startTime = clock();
    if (clockdiff(startTime) >= t) return -1;
    
    // Get a pair containing iterators pointing the beginning and end of the list of nodes
    pair<Graph::vertex_iterator, Graph::vertex_iterator> vItrRange = vertices(g);
    
    // Loop over all nodes in the graph
    for (Graph::vertex_iterator vItr = vItrRange.first; vItr != vItrRange.second; ++vItr)
    {
        if (clockdiff(startTime) >= t) return -1;
        
        vector<bool> colorAvailable(g_numColor, true); // Colors that are ok to use
        pair<Graph::adjacency_iterator, Graph::adjacency_iterator> ad_vItrRange = adjacent_vertices(*vItr, g);
        
        // Loop over adjacent nodes in the graph
        for (Graph::adjacency_iterator ad_vItr= ad_vItrRange.first; ad_vItr != ad_vItrRange.second; ++ad_vItr)
        {
            if (clockdiff(startTime) >= t) return -1;
            
            int ad_v_weight = g[*ad_vItr].weight;
            if (ad_v_weight >= 0 && ad_v_weight < g_numColor)
                colorAvailable[ad_v_weight] = false;
        }
        
        int i = 0;
        for (auto b : colorAvailable)
        {
            if (b) { g[*vItr].weight = i; break; }
            ++i;
        }
        
        // Select one if every color causes conflict
        if (i == colorAvailable.size())
            g[*vItr].weight = 1;
    }
    
    cout << "Greedy Coloring took: " << clockdiff(startTime)
    << "s | Limit was: " << t << "s" << endl;
    
    return 0;
}

// unsigned long neighborhood(...)
// Description: return vItr index if no conflict, else ad_vItr index
// Limitations: none.
// Assumptions: Valid graph, valid colors, and valid vertex iterator.
unsigned long neighborhood(Graph &g, int numColors, Graph::vertex_iterator vItr)
{
    pair<Graph::adjacency_iterator, Graph::adjacency_iterator> ad_vItrRange = adjacent_vertices(*vItr, g);
    for (Graph::adjacency_iterator ad_vItr= ad_vItrRange.first; ad_vItr != ad_vItrRange.second; ++ad_vItr)
    {
        int cur_weight = g[*vItr].weight;
        int ad_weight = g[*ad_vItr].weight;
        if (cur_weight == ad_weight) return *ad_vItr;
    }
    return *vItr;
}

// int steepestDescentColoring(...)
// Description: Keep picking best neighbors
// Limitations: none.
// Assumptions: Valid graph, valid colors, and valid vertex iterator.
int steepestDescentColoring(Graph &g, int numColors, int t)
{
    clock_t startTime = clock();
    if (clockdiff(startTime) >= t) return -1;
    
    // Get a pair containing iterators pointing the beginning and end of the list of nodes
    pair<Graph::vertex_iterator, Graph::vertex_iterator> vItrRange = vertices(g);
    
    // Loop over all nodes in the graph
    for (Graph::vertex_iterator vItr = vItrRange.first; vItr != vItrRange.second; ++vItr)
    {
        if (clockdiff(startTime) >= t) return -1;
        
        // Choose neighbor that conflicts
        unsigned long neighbor = neighborhood(g, numColors, vItr);
        
        // If no neighbors conflict, continue
        if (*vItr == neighbor) continue;
        
        // Check which colors would be best.
        int bestColor = 0;
        int minConflicts = LargeValue;
        for (int i = 0; i < numColors; ++i) {
            g[*vItr].weight = i;
            int cur_conflictCount = checkConflicts(g);
            if (minConflicts > cur_conflictCount) {
                bestColor = i;
                minConflicts = cur_conflictCount;
            }
        }
        
        g[*vItr].weight = bestColor;
    }
    
    cout << "Steepest Descent Coloring took: " << clockdiff(startTime)
    << "s | Limit was: " << t << "s" << endl;
    
    return 0;
}

// void inline selectOneWithMinConflict(...)
// Description: This will find a color with min conflict locally.
// Limitations: none.
// Assumptions: Valid graph, valid colors, and valid vertex iterator.
void inline selectOneWithMinConflict(Graph &g, int numColors, Graph::vertex_iterator &vItr)
{
    int bestColor = -1, minConflict = LargeValue;
    vector<int> conflictCount(numColors, 0);
    pair<Graph::adjacency_iterator, Graph::adjacency_iterator> ad_vItrRange = adjacent_vertices(*vItr, g);
    
    for (Graph::adjacency_iterator ad_vItr= ad_vItrRange.first; ad_vItr != ad_vItrRange.second; ++ad_vItr)
    {
        int ad_weight = g[*ad_vItr].weight;
        if (ad_weight != INT_MIN)
            conflictCount[ad_weight]++;
    }
    
    for (int i = 0; i < numColors; ++i)
    {
        if (minConflict > conflictCount[i]) {
            minConflict = conflictCount[i];
            bestColor = i;
        }
    }
    
    g[*vItr].weight = bestColor;
    
    return;
}

// int advLocalSearchAlgorithm(...)
// Description: optimized early continuations.
// Limitations: none.
// Assumptions: Valid graph, valid colors, and valid vertex iterator.
int advLocalSearchAlgorithm(Graph &g, int numColors, int t)
{
    clock_t startTime = clock();
    if (clockdiff(startTime) >= t) return -1;
    
    // Get a pair containing iterators pointing the beginning and end of the list of nodes
    pair<Graph::vertex_iterator, Graph::vertex_iterator> vItrRange = vertices(g);
    
    // Loop over all nodes in the graph
    for (Graph::vertex_iterator vItr = vItrRange.first; vItr != vItrRange.second; ++vItr)
    {
        if (clockdiff(startTime) >= t) return -1;
        selectOneWithMinConflict(g, numColors, vItr);
    }
    
    cout << "Faster Adv. Local Search Algorithm Coloring took: " << clockdiff(startTime)
    << "s | Limit was: " << t << "s" << endl;
    
    return 0;
}


// Should give the total number of conflicts, and the color assigned to each node for each instance.
void printSolution(Graph &g)
{
    pair<Graph::vertex_iterator, Graph::vertex_iterator> vItrRange = vertices(g);
    
    cout << "Min conflict count is " << checkConflicts(g) << endl;
    for (Graph::vertex_iterator vItr = vItrRange.first; vItr != vItrRange.second; ++vItr)
        cout << *vItr << " is " << g[*vItr].weight << endl;
}


int main()
{
    //char x;
    ifstream fin;
    string fileName;
    
    const char* inputFileNames[11] = {"color12-3.input",
        "color12-4.input",
        "color24-4.input",
        "color24-5.input",
        "color48-5.input",
        "color48-6.input",
        "color96-6.input",
        "color96-7.input",
        "color192-6.input",
        "color192-7.input",
        "color192-8.input"};
    
    const char* outputFileNames[11] = {"color12-3.output",
        "color12-4.output",
        "color24-4.output",
        "color24-5.output",
        "color48-5.output",
        "color48-6.output",
        "color96-6.output",
        "color96-7.output",
        "color192-6.output",
        "color192-7.output",
        "color192-8.output"};
    
    const char* outputFileNames_ADV[11] = {"color12-3.output_ADV",
        "color12-4.output_ADV",
        "color24-4.output_ADV",
        "color24-5.output_ADV",
        "color48-5.output_ADV",
        "color48-6.output_ADV",
        "color96-6.output_ADV",
        "color96-7.output_ADV",
        "color192-6.output_ADV",
        "color192-7.output_ADV",
        "color192-8.output_ADV"};
    
    // To run certain files, change the loop value.
    for (int i = 0; i < 11; i++) {
        
        fileName = inputFileNames[i];
        
        fin.open(fileName.c_str());
        if (!fin)
        {
            cerr << "Cannot open " << fileName << endl;
            exit(1);
        }
        
        try
        {
            freopen(outputFileNames[i],"w",stdout); // Redirect output
            cout << "Reading graph" << endl;
            Graph g;
            initializeGraph(g,fin);
            
            cout << "Num nodes: " << num_vertices(g) << endl;
            cout << "Num edges (one direction): " << num_edges(g) / 2 << endl;
            cout << "Num edges (bi- direction): " << num_edges(g) << endl;
            cout << endl;
            
            if (greedyColoring(g, g_numColor, 300) == -1)
                cout << "Timed out..." << endl;
            printSolution(g);
            
            if (steepestDescentColoring(g, g_numColor, 300) == -1)
            cout << "Timed out..." << endl;
            printSolution(g);
            
            //+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            
            
            fin.clear();
            fin.seekg(0, ios::beg);
            freopen(outputFileNames_ADV[i],"w",stdout); // Redirect output
            cout << "Reading graph" << endl;
            Graph g2;
            initializeGraph(g2,fin);
            
            cout << "Num nodes: " << num_vertices(g2) << endl;
            cout << "Num edges (one direction): " << num_edges(g2) / 2 << endl;
            cout << "Num edges (bi- direction): " << num_edges(g2) << endl;
            cout << endl;
            
            if (greedyColoring(g2, g_numColor, 300) == -1)
                cout << "Timed out..." << endl;
            cout << "Victor's computer" << endl;
            printSolution(g2);
            
            if (advLocalSearchAlgorithm(g2, g_numColor, 300) == -1)
                cout << "Timed out..." << endl;
            printSolution(g2);
        }
        catch (indexRangeError &ex)
        {
            cout << ex.what() << endl; exit(1);
        }
        catch (rangeError &ex)
        {
            cout << ex.what() << endl; exit(1);
        }
        
        fin.close();
    }
}
