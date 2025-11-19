#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	
	int score[16] ;
	for(int i = 0; i < 16 ;i ++){
	    int count = 0;
	    int x = 16-i;
	    while(x > 1){
	        count ++;
	        x /= 2;
	    }
	    score[i] = count;
	}
	
	for(int i = 0; i < 16 ;i ++){
	    cout<<score[i] <<" ";
	}
	
	int n;
	cin>>n;
	while(n--){
	    int players[16kkoo];
        int play[16];
        int max_num  = 0;
	    for(int i = 0; i < 16 ;i ++){
	        cin>>players[i];
            play[i] = players[i];
	    }

        sort(players , players + 16);


        int map_score[players[15]];

        for(int i = 0 ; i< 16 ; i++){
            map_score[players[i]] = score[i];
        }

        for(int i = 0 ; i< 16; i++){
            cout<<map_score[play[i]]<<" ";
        }
        cout<<endl;




	}

    return 0;

}
