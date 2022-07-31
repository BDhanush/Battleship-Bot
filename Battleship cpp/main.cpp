#include <bits/stdc++.h>
#include "test boards.h"

using namespace std;

#define debug(x) cout<< #x <<"="<<x<<endl
#define all(x) x.begin(),x.end()
#define PI 3.1415926535897932384626

int c=0;
int bias=3;

class s
{
public:
    string teamname="to be named";
    vector<vector<int>> board;
    vector<vector<int>> o_board;
    vector<vector<int>> store;
    vector<int> ship_size;
    vector<vector<float>> probability;
};

bool hit_or_miss(s& self,int x,int y)
{
    if(self.o_board[x][y]==1)
    {
        //self.o_board[x][y]=0;
        return true;
    }
    return false;
}

void debug_store(s self)
{
    cout<<"\nstore\n";
    for(int i=0;i<10;i++)
    {
        for(int j=0;j<10;j++)
        {
            cout<<self.store[i][j]<<" ";
        }
        cout<<"\n";
    }
    cout<<"\n";
}

void debug_hit(set<int> s)
{
    cout<<"\nhits\n";
    for(auto i:s)
    {
        cout<<i<<" ";
    }
    cout<<"\n";
}

void debug_probability(s self)
{
    cout<<"\nprobability\n";
    for(int i=0;i<10;i++)
    {
        for(int j=0;j<10;j++)
        {
            cout<<self.probability[i][j]<<" ";
        }
        cout<<"\n";
    }
    cout<<"\n";
}

pair<int,int> attack(s& self)
{
    c++;
    self.probability=vector<vector<float>> (10,vector<float> (10,0));
    pair<int,int> maxi1={0,0};
    int maxi=0;
    for(int z=0;z<3;z++)
    {
        for(int i=0;i<10;i++)
        {
            for(int j=0;j<=10-self.ship_size[z];j++)
            {
                set<int> hits;
                int non_miss=0;
                //debug(j);
                //debug(j+self.ship_size[z]);
                for(int k=j;k<j+self.ship_size[z];k++)
                {
                    if(self.store[i][k]==1)
                    {
                        hits.insert(k);
                        //cout<<1<<"\n";
                    }
                    if(self.store[i][k]!=2)
                    {
                        non_miss++;
                    }
                }

                //debug_hit(hits);
                if(non_miss==self.ship_size[z])
                {
                    for(int k=j;k<j+self.ship_size[z];k++)
                    {
                        if(hits.find(k)!=hits.end())
                        {
                            self.probability[i][k]=0;
                        }else{
                            if(self.ship_size[z]==5 || self.ship_size[z]==4)
                            {
                                self.probability[i][k]+=(2*self.ship_size[z]*(hits.size()?bias*hits.size():1));
                            }else{
                                self.probability[i][k]+=(self.ship_size[z]*(hits.size()?bias*hits.size():1));
                            }
                        }
                    }
                }
            }
        }

        for(int j=0;j<10;j++)
        {
            for(int i=0;i<=10-self.ship_size[z];i++)
            {
                set<int> hits;
                int non_miss=0;
                for(int k=i;k<i+self.ship_size[z];k++)
                {
                    if(self.store[k][j]==1)
                    {
                        hits.insert(k);
                    }
                    if(self.store[k][j]!=2)
                    {
                        non_miss++;
                    }
                }

                if(non_miss==self.ship_size[z])
                {
                    for(int k=i;k<i+self.ship_size[z];k++)
                    {
                        if(hits.find(k)!=hits.end())
                        {
                            self.probability[k][j]=0;
                        }else{
                            if(self.ship_size[z]==5 || self.ship_size[z]==4)
                            {
                                self.probability[k][j]+=(2*self.ship_size[z]*(hits.size()?bias*hits.size():1));
                            }else{
                                self.probability[k][j]+=(self.ship_size[z]*(hits.size()?bias*hits.size():1));
                            }

                        }
                    }
                }
            }
        }
    }
    //debug_probability(self);

    for(int i=0;i<10;i++)
    {
        for(int j=0;j<10;j++)
        {
            if(self.probability[i][j]>maxi)
            {
                maxi=self.probability[i][j];
                maxi1={i,j};
            }
        }
    }
    return maxi1;
}

void test()
{
    s self;
    //int n=0,total=0;
    double average_score=0;
    self.teamname="to be named";
    self.board=vector<vector<int>> (10,vector<int> (10,0));
    for(int z=0;z<ars.size();z++)
    {
        int cou=0,n=0;
        self.o_board=ars[z];
        self.store=vector<vector<int>> (10,vector<int> (10,0));
        self.ship_size={5,4,3};
        //self.probability=vector<vector<float>> (10,vector<float> (10,0.0));

        //pair<int,int> p=attack(self);
        //debug_probability(self);
        while(n<21)
        {
            pair<int,int> co=attack(self);
            //debug(co.first);
            //debug(co.second);
            //debug_probability(self);
            if(hit_or_miss(self,co.first,co.second))
            {
                self.store[co.first][co.second]=1;
                n++;
            }else{
                self.store[co.first][co.second]=2;
            }
            cou++;
            //self.probability[co.first][co.second]=0;
            //debug_store(self);
            //total++;
        }
        //debug_store(self);
        average_score+=cou;
        debug(z);
        debug(cou);         //print
        cout<<"\n";
    }
    average_score/=ars.size();
    debug(average_score); //print
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int t=1;
    //cin>>t;

    while(t--)
    {
        test();
    }
    return 0;
}
