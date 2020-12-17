#include <bits/stdc++.h>
using namespace std;
const int X = 1;
const int Y = 9;

int rnd(int poc, int kon){
    return poc + rand() % (kon - poc + 1);
}

void fill_zeroes(int **tab, int n, int val = 0){
    for (int i = 0; i < n; i ++){
        for (int j = 0; j < n; j ++){
            if (i == 0 || i == n - 1 || j == 0 || j == n - 1 || i == j || j == n - i - 1){
                tab[i][j] = val;
            }
        }
    }
}

void fill_random(int** tab, int n, int poc, int kon){
    for (int i = 0; i < n; i ++){
        for (int j = 0; j < n; j ++)
            tab[i][j] = rnd(poc, kon);
    }
}

void show(int** tab, int n){
    for (int i = 0; i < n; i ++){
        for (int j = 0; j < n; j ++){
            cout << tab[i][j] << " ";
        }
        cout << endl;
    }
}

void save(int** tab, int n, string filename){
    fstream plik(filename, ios::out);
    for (int i = 0; i < n; i ++){
        for (int j = 0; j < n; j ++){
            plik << tab[i][j] << " ";
        }
        plik << endl;
    }
    plik.close();
}

int** init_matrix(int n){
    int** tab = new int*[n];
    for (int i = 0; i < n; i ++)
        tab[i] = new int[n];
    return tab;
} 

void init_matrix(int*** tab, int n){
    *tab = new int*[n];
    for (int i = 0; i < n; i ++)
        (*tab)[i] = new int[n];
} 

int* sum_of_X(int** tab, int n){
    int* result = new int[n];
    for (int i = 0; i < n; i ++){
        int poc = i;
        int kon = n - i - 1;
        if (poc > kon) swap(poc, kon);

        int sum = 0;
        for (int j = poc + 1; j <= kon - 1; j ++)
            sum += tab[i][j];
        result[i] = sum;
    }
    return result;
}

void swap(int& a, int& b){
    int bufor = a;
    a = b;
    b = bufor;
}

void swap(int* a, int* b){
    int bufor = *a;
    *a = *b;
    *b = bufor;
}

void swap2(int& a, int& b){
    a ^= b;
    b ^= a;
    a ^= b;
}

int main(){

    int N;
    cin >> N;
    int** A = init_matrix(N);
    int** B = init_matrix(N);
    // init_matrix(&tab, N);
    fill_random(A, N, X, Y);
    fill_zeroes(A, N); // bez roznicy czy dasz 0
    
    fill_random(B, N, -15, 10);
    fill_zeroes(B, N, 1);

    cout << "A:\n";
    show(A, N);
    cout << "B:\n";
    show(B, N);
    
    save(A, N, "halo.txt");
    int* tab = sum_of_X(B, N);
    cout << "sumy: \n";
    for (int i = 0; i < N; i ++)
        cout << tab[i] << endl;
    return 0; 
}