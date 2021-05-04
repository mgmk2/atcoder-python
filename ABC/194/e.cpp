#include <vector>
#include <algorithm>
#include <set>

int main()
{
    int n, m;
    std::cin >> n >> m;
    std::vector<int> a(n);
    for (auto &ai : a)
    {
        std::cin >> ai;
    }

    std::map<int, int> s;
    for (int i = 0; i < m; ++i)
    {
        s[a[i]] += 1;
    }
}