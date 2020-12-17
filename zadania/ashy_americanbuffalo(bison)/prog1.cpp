#include <iostream>
#include <iomanip>
#include <ctime>
#include <cstdlib>
#include <fstream>
#include <cmath>
#include <windows.h>

using namespace std;

void tworz(char** &tab, int w, int k){
    tab=new char*[w];
    for(int i=0;i<w;i++){
        tab[i] = new char[k];
    }
}

bool wczytaj(char**&tab, int w, int k, string nazwa){
    ifstream plik;
    plik.open(nazwa.c_str());

    if (!plik.good())
        return false;

    for(int i=0;i<w;i++){
        for(int j=0;j<k;j++){

            if(!plik.eof()){
                plik>>tab[i][j];
            }else{
                plik.close();
                return false;
            }
        }
    }

    plik.close();
    return true;
}

void drukuj(char**&tab, int w, int k){
    for(int i=0;i<w;i++){
        for(int j=0;j<k;j++){
            cout<<tab[i][j]<<'\t';
        }
        cout<<endl;
    }
}

void kasuj(char**&tab, int w){
    for(int i=0;i<w;i++){
        delete []tab[i];
    }
    delete []tab;
}

void funkcja(char**&tab, int w, int k, char zn1, char zn2){
    int* wek = new int[k];

    for(int j=0;j<k;j++){

        int l_elem = 0;

        for(int i=0;i<w;i++){
            if ((tab[i][j]>=zn1)&&(tab[i][j]<=zn2))
                l_elem++;
        }

        wek[j] = l_elem;
    }

    for(int j=1;j<k;j++){
        if (wek[j]>wek[j-1]){
            cout<<"Indeks: "<<j<<endl;
        }
    }

    delete []wek;
}


int main(){

    char** a;
    char** b;
    int w,k;

    cout<<"Podaj w i k";
    cin>>w>>k;

    tworz(a,w,k);
    tworz(b,w,k);

    if(!wczytaj(a,w,k,"char int.txt"))
        return 1;

    if(!wczytaj(b,w,k,"char int.txt"))
        return 1;

    drukuj(a,w,k);
    cout<<endl;
    drukuj(b,w,k);

    funkcja(a,w,k,'a','z');
    funkcja(b,w,k,'0','9');

    kasuj(a,w);
    kasuj(b,w);

    return 0;

}
