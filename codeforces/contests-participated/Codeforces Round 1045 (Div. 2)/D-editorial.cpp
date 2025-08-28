#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    vector<vector<int>> G(n);
    for (int i = 0; i < n - 1; i++) {
      int u, v;
      cin >> u >> v;
      u--, v--;
      G[u].push_back(v);
      G[v].push_back(u);
    }

    vector<int> dist(n), p(n);
    function<void(int, int)> dfs = [&](int now, int par) {
      p[now] = par;
      for (int i : G[now]) {
        if (i != par) {
          dist[i] = dist[now] + 1;
          dfs(i, now);
        }
      }
    };

    dist[0] = 0;
    dfs(0, -1);
    int x = max_element(dist.begin(), dist.end()) - dist.begin();
    dist[x] = 0;
    dfs(x, -1);
    int y = max_element(dist.begin(), dist.end()) - dist.begin();

    if (dist[y] == n - 1) {
      cout << -1 << '\n';
    } else {
      vector<int> on_diameter(n);
      int now = y;
      while (now != -1) {
        on_diameter[now] = 1;
        now = p[now];
      }
      int a = -1, b = -1, c = -1;
      for (int u = 0; u < n; u++) {
        for (int v : G[u]) {
          if (on_diameter[u] && !on_diameter[v]) {
            a = p[u], b = u, c = v;
            break;
          }
        }
        if (a != -1)
          break;
      }
      cout << a + 1 << ' ' << b + 1 << ' ' << c + 1 << '\n';
    }
  }
}