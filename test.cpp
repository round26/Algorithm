#include<iostream>
#include<vector>

using namespace std;

vector<int> a[101];
bool check[101];
int cnt = 0;

void dfs(int x){
    check[x] = true;
    cnt++;
    
    for (int i=0; i<a[x].size();i++){
        if(!check[a[x][i]]){
            dfs(a[x][i]);
        }
    }
    return;
}

int main(void){
    int n,m;
    cin >> n >> m;
    for (int i=0;i<m;i++){
        int u,v;
        cin >> u >> v;
        a[u].push_back(v);
        a[v].push_back(u);
    }
    dfs(1);
    cout << cnt-1 << endl;
    return 0;
}