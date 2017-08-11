// Knapsack class
// Version f08.1

class knapsack {
public:
  knapsack() {};
  knapsack(ifstream &fin);
  knapsack(const knapsack &);
  int getCost(int) const;
  int getValue(int) const;
  int getCost() const;
  int getValue() const;
  int getNumObjects() const;
  int getCostLimit() const;
  int getLeftCost() const;
  void printSolution();
  void select(int);
  void unSelect(int);
  bool isSelected(int) const;

    vector<pair<float, int>> denList;

  // Modifications
  double bound(int);
  void selectBestI(int);
  void unSelectBestI(int);
  void operator=(const knapsack &);

private:
  int numObjects;
  int costLimit;
  vector<int> value;
  vector<int> cost;
  vector<bool> selected;
  int totalValue;
  int totalCost;

  // Modifications
  int leftCost;
  int bounds;
};

knapsack::knapsack(ifstream &fin)
// Construct a new knapsack instance using the data in fin.
{
  int n, b, j, v, c;

  fin >> n; // read the number of objects
  fin >> b; // read the cost limit

  numObjects = n;
  costLimit = b;

  value.resize(n);
  cost.resize(n);
  selected.resize(n);

  for (int i = 0; i < n; i++) {
    fin >> j >> v >> c;
    value[j] = v;
    cost[j] = c;
    unSelect(j);
    denList.push_back(make_pair(v/float(c), i));
  }
  sort(denList.begin(), denList.end(), [](auto &left, auto &right) {
        return left.first > right.first;});

  for (auto x : denList)
    cout << x.first << ":" << x.second << " ";
  cout << endl;

  totalValue = 0;
  totalCost = 0;
  leftCost = costLimit;
  bounds = INT_MIN;
}

knapsack::knapsack(const knapsack &k)
// Knapsack copy constructor.
{
  int n = k.getNumObjects();

    value.clear();
    cost.clear();
    selected.clear();
  value.resize(n);
  cost.resize(n);
  selected.resize(n);
  numObjects = k.getNumObjects();
  costLimit = k.getCostLimit();
  leftCost = k.getCostLimit();
  denList = k.denList;

  totalCost = 0;
  totalValue = 0;
  bounds = INT_MIN;

  for (int i = 0; i < n; i++) {
    value[i] = k.getValue(i);
    cost[i] = k.getCost(i);
    if (k.isSelected(i))
      select(i);
    else
      unSelect(i);
  }
}

void knapsack::operator=(const knapsack &k)
{
    int n = k.getNumObjects();

    value.clear();
    cost.clear();
    selected.clear();
    value.resize(n);
    cost.resize(n);
    selected.resize(n);
    numObjects = k.getNumObjects();
    costLimit = k.getCostLimit();
    leftCost = k.getCostLimit();
    denList = k.denList;

    totalCost = 0;
    totalValue = 0;
    bounds = INT_MIN;

    for (int i = 0; i < n; i++) {
        value[i] = k.getValue(i);
        cost[i] = k.getCost(i);
        if (k.isSelected(i))
            select(i);
        else
            unSelect(i);
    }
}

int knapsack::getNumObjects() const { return numObjects; }

int knapsack::getCostLimit() const { return costLimit; }

int knapsack::getLeftCost() const { return leftCost; }

int knapsack::getValue(int i) const
// Return the value of the ith object.
{
  if (i < 0 || i >= getNumObjects()){
    cout << "getValue(" << i << ")" << endl;
    throw rangeError("Bad value in knapsack::getValue");
  }

  return value[i];
}

int knapsack::getCost(int i) const
// Return the cost of the ith object.
{
  if (i < 0 || i >= getNumObjects())
    throw rangeError("Bad value in knapsack::getCost");

  return cost[i];
}

int knapsack::getCost() const
// Return the cost of the selected objects.
{
  return totalCost;
}

int knapsack::getValue() const
// Return the value of the selected objects.
{
  return totalValue;
}

ostream &operator<<(ostream &ostr, const knapsack &k)
// Print all information about the knapsack.
{
  cout << "------------------------------------------------" << endl;
  cout << "Num objects: " << k.getNumObjects()
       << " Cost Limit: " << k.getCostLimit() << endl;

  int totalValue = 0;
  int totalCost = 0;

  for (int i = 0; i < k.getNumObjects(); i++) {
    totalValue += k.getValue(i);
    totalCost += k.getCost(i);
  }

  cout << "Total value: " << totalValue << endl;
  cout << "Total cost: " << totalCost << endl << endl;

  for (int i = 0; i < k.getNumObjects(); i++)
    cout << i << "  " << k.getValue(i) << " " << k.getCost(i) << endl;

  cout << endl;

  return ostr;
}

void knapsack::printSolution()
// Prints out the solution.
{
  cout << "------------------------------------------------" << endl;

  cout << "Total value: " << getValue() << endl;
  cout << "Total cost: " << getCost() << endl << endl;

  // Print out objects in the solution
  for (int i = 0; i < getNumObjects(); i++)
    if (isSelected(i))
      cout << i << "  " << getValue(i) << " " << getCost(i) << endl;

  cout << endl;
}

ostream &operator<<(ostream &ostr, vector<bool> v)
// Overloaded output operator for vectors.
{
  for (int i = 0; i < v.size(); i++)
    cout << v[i] << endl;

  return ostr;
}

void knapsack::select(int i)
// Select object i.
{
  if (i < 0 || i >= getNumObjects())
    throw rangeError("Bad value in knapsack::Select");

  if (selected[i] == false) {
    selected[i] = true;
    totalCost = totalCost + getCost(i);
    totalValue = totalValue + getValue(i);
    leftCost = leftCost - getCost(i);
  }
}

void knapsack::unSelect(int i)
// unSelect object i.
{
  if (i < 0 || i >= getNumObjects())
    throw rangeError("Bad value in knapsack::unSelect");

  if (selected[i] == true) {
    selected[i] = false;
    totalCost = totalCost - getCost(i);
    totalValue = totalValue - getValue(i);
    leftCost = leftCost + getCost(i);
  }
}

void knapsack::selectBestI(int i)
{
  select(denList[i].second);
}

 void knapsack::unSelectBestI(int i)
 {
   unSelect(denList[i].second);
 }

bool knapsack::isSelected(int i) const
// Return true if object i is currently selected, and false otherwise.
{
  if (i < 0 || i >= getNumObjects())
    throw rangeError("Bad value in knapsack::getValue");

  return selected[i];
}

double knapsack::bound(int index) {
  if (bounds != INT_MIN)
      return bounds;

  if (index < 0 || index >= getNumObjects()) {
    cout << "bound(" << index << ")" << endl;
    throw rangeError("Bad index value in knapsack::bound");
  }

  double realValue = getValue(denList[index].second);
  int realIndex = denList[index].second;
  int tempCost  = 0;

  if (index == 0)
    return leftCost * realValue;

  bounds = getValue()
    + ((tempCost = (leftCost - getCost(realIndex))) > 0 ?
      realValue
      + (index + 1 < getNumObjects() ?
          tempCost * denList[index+1].first
          : 0)
      : 0);
    return bounds;
}
