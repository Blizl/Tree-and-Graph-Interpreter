//
//  main.cpp
//  Project 5a
//
//

// Jae Hoon Kim and Victor Liang

#include <iostream>
#include <limits.h>
#include <list>
#include <fstream>
#include <queue>
#include <vector>
#include <time.h>
#include <string>

#include <cmath>
#include <unistd.h>

using namespace std;

#include "d_except.h"
#include "d_matrix.h"
#include "knapsack.h"

#define clockdiff(x) (float)(clock()-x)/CLOCKS_PER_SEC

// WILL NOT GET THE MOST OPTIMAL SOLUTION ALL THE TIME - Greedy
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

// void greedyKnapsack(...)
// Description: Greedy way of finding the somtimes optimal solution.
// Limitations: Does not always get the most optimal solution.
// Assumptions: Valid knapsack and valid time limit.
void greedyKnapsack(knapsack &k, int t)
{
    clock_t startTime;
    startTime = clock();
    const int costLimit = k.getCostLimit();
    
    while( clockdiff(startTime) <= t && k.getCost() < costLimit)
    {
        float max = -1.0;
        int index = -1;
        
        // Find the most desnse.
        for (int i = 0; i < k.getNumObjects(); ++i)
        {
            if (k.isSelected(i) || k.getCost()+k.getCost(i) > costLimit) continue;
            float currentDensity = k.getValue(i) / (float) k.getCost(i);
            max = max < currentDensity ? index = i, currentDensity : max;
        }
        
        // If no more, return
        if (max == -1.0)
        {
            cout << "Time taken for Greedy: " << clockdiff(startTime)
            << "s | Limit was: " << t << "s" << endl;
            cout << "Cost Limit: " << k.getCostLimit() << endl;
            return;
        }
        // Select the max found.
        k.select(index);
        //cout << "Selected: " << index << endl; // Debug selection order
    }
}

inline void neighborhoodFunction(knapsack &k, int currentlySelected, int toBeSelected)
{
    if (k.isSelected(currentlySelected) && !k.isSelected(toBeSelected)) {
        k.unSelect(currentlySelected);
        k.select(toBeSelected);
        return;
    }
    exit(1);
}

void steepestDescentKnapsack(knapsack &k, int t)
{
    clock_t startTime;
    startTime = clock();
    for (int i = 1; i < k.getNumObjects() && clockdiff(startTime) <= t; ++i)
    {
        if (k.isSelected(i)) {
            for (int j = 0; j < k.getNumObjects(); ++j) {
                if (!k.isSelected(j)
                    && k.getCostLimit() >= (k.getCost() - k.getCost(i) + k.getCost(j))
                    && k.getValue() <= k.getValue() - k.getValue(i) + k.getValue(j)) {
                    neighborhoodFunction(k, i, j);
                    break;
                }
            }
        }
    }
    cout << "Time taken for Steepest Descent: " << clockdiff(startTime)
    << "s | Limit was: " << t << "s" << endl;
    cout << "Cost Limit: " << k.getCostLimit() << endl;
    return;
}

void tabuSearchAlgorithm(knapsack &k, int t)
{
    bool *tabuList = new bool[k.getNumObjects()];
    clock_t startTime;
    startTime = clock();
    for (int i = 1; i < k.getNumObjects() && clockdiff(startTime) <= t; ++i)
    {
        if (!tabuList[i] && k.isSelected(i)) {
            for (int j = 0; j < k.getNumObjects(); ++j) {
                if (!tabuList[j] && !k.isSelected(j)
                    && k.getCostLimit() >= (k.getCost() - k.getCost(i) + k.getCost(j))
                    && k.getValue() <= k.getValue() - k.getValue(i) + k.getValue(j)) {
                    neighborhoodFunction(k, i, j);
                    tabuList[i] = tabuList[j] = true;
                    break;
                }
            }
        }
    }
    cout << "Time taken for Tabu Search: " << clockdiff(startTime)
    << "s | Limit was: " << t << "s" << endl;
    cout << "Cost Limit: " << k.getCostLimit() << endl;
    
    delete[] tabuList;
    return;
}

void dynamicProgramming(knapsack &k)
{
   int i, w;
   int n = k.getNumObjects();
   int W = k.getCostLimit();
   
   int K[n+1][W+1];
 
   for (i = 0; i <= n; i++)
   {
       for (w = 0; w <= W; w++)
       {
           if (i==0 || w==0)
               K[i][w] = 0;
           else if (k.getCost(i -1) <= w)
                 K[i][w] = max(k.getValue(i -1)+ K[i-1][w-k.getCost(i -1)],  K[i-1][w]);
           else
                 K[i][w] = K[i-1][w];
       }
   }
   i = n;
   int k_value = W;
    while (i >0 && k_value >0){
      if (K[i][k_value] != K[i-1][k_value]){
        k.select(i-1);
        i = i-1;
        k_value = k_value-k.getCost(i);
      }
      else{
        i = i-1;
      }
    }

   return K[n][W];
}


int main()
{
    //char x;
    ifstream fin;
    //stack <int> moves;
    string fileName;
    
    const char* inputFileNames[12] = {"knapsack8.input",
        "knapsack12.input",
        "knapsack16.input",
        "knapsack20.input",
        "knapsack28.input",
        "knapsack32.input",
        "knapsack48.input",
        "knapsack64.input",
        "knapsack128.input",
        "knapsack256.input",
        "knapsack512.input",
        "knapsack1024.input"};
    
    const char* outputFileNames[12] = {"knapsack8.output",
        "knapsack12.output",
        "knapsack16.output",
        "knapsack20.output",
        "knapsack28.output",
        "knapsack32.output",
        "knapsack48.output",
        "knapsack64.output",
        "knapsack128.output",
        "knapsack256.output",
        "knapsack512.output",
        "knapsack1024.output"};
    
    const char* outputFileNames_ADV[12] = {"knapsack8.output_ADV",
        "knapsack12.output_ADV",
        "knapsack16.output_ADV",
        "knapsack20.output_ADV",
        "knapsack28.output_ADV",
        "knapsack32.output_ADV",
        "knapsack48.output_ADV",
        "knapsack64.output_ADV",
        "knapsack128.output_ADV",
        "knapsack256.output_ADV",
        "knapsack512.output_ADV",
        "knapsack1024.output_ADV"};
    
    // To run certain files, change the loop value.
    for (int i = 0; i < 12; i++) {
        
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
            cout << "Reading knapsack instance" << endl;
            knapsack k(fin);
            
            // produces an initial solution
            greedyKnapsack(k, 300);
            
            cout << "*** *** Before Steepest Descent:" << endl;
            k.printSolution();
            
            // using steepest descent to find a locally optimal soution
            steepestDescentKnapsack(k, 300);
            
            cout << endl << "Best solution found after Steepest Descent" << endl;
            k.printSolution();
            
            //++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            fin.clear();
            fin.seekg(0, ios::beg);
            freopen(outputFileNames_ADV[i],"w",stdout); // Redirect output
            cout << "Reading knapsack instance" << endl;
            knapsack k2(fin);
            
            // produces an initial solution
            greedyKnapsack(k2, 300);
            cout << "Victor's computer" << endl;
            cout << "*** *** Before Steepest Descent:" << endl;
            k2.printSolution();
            
            // using steepest descent to find a locally optimal soution
            tabuSearchAlgorithm(k2, 300);
            
            cout << endl << "Best solution found after Adv Algo (Tabu Search)" << endl;
            k2.printSolution();
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
