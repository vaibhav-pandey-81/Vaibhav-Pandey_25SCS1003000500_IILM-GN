//******* Practical 1st - Basic INPUT OUTPUT *********** */

// #include<iostream>
// using namespace std;
// int main(){
//     int op,num1,num2;
//     float result;
//     cout<<"Enter Operator \n 1.addition \n 2.subtraction \n 3.multiplication
//     \n 4.division"<<endl;

//     cin>>op;
//     cout<<"Enter 1st number :";
//     cin>>num1;
//     cout<<"Enter 2nd number :";
//     cin>>num2;

//     switch(op){
//         case 1:
//         result = num1+num2;
//         break;
//         case 2:
//         result = num1-num2;
//         break;
//         case 3:
//         result=num1*num2;
//         break;
//         case 4:
//         result= (float)num1/num2;
//         break;
//         default:
//         cout<<"Invalid Operator";
//         break;
//     }
//     cout<<"The result is : "<<result;

//     return 0;
// }

//******* Practical 2nd - Function *********** */

// #include <iomanip>
// #include <iostream>

// using namespace std;

// class rectangle {
//   int length = 2;
//   int breadth = 4;

// public:
//   void area();
//   void perimeter();
// };
// void rectangle::area() {
//   float area = length * breadth;
//   cout << fixed << setprecision(2);
//   cout << area;
// }
// void rectangle::perimeter() {
//   float per = 2 * (length + breadth);
//   cout << fixed << setprecision(2);
//   cout << per;
// }
// int main() {
//   rectangle ob1;
//   cout << "Area:";
//   ob1.area();
//   cout << endl << "Perimeter:";
//   ob1.perimeter();

//   return 0;
// }




// ********Practical 3rd - Function outside the class *********/
// #include<iostream>
// using namespace std;
// class item{
//     int number;
//     float cost;
//     public:
//     void getdata(int a, int b);
//     void putdata(void);
// };
// void item::getdata(int a, int b){ // ' :: ' scope resolution operator
//     number = a;
//     cost = b;
// }
// void item::putdata(void){
//     cout<<"Number "<<number<<endl;
//     cout<<"Cost "<<cost<<endl;
// }
// int main(){
//     item x;
//     x.getdata(8,9);
//     x.putdata();


//     return 0;
// }





//********Practical 4- Constructer**** */
// #include<iostream>
// using namespace std;
// class fib{
//     int n,a=0,b=1,n_term; //private
//     public:
//     fib(){
//         cout<<"Enter number => ";
//         cin>>n;
//     }
//     void fibo();
// };
// void fib::fibo(){ // scope resolution operator
//     cout<<"The fibonacci series upto "<<n<<"term is: "<<endl<<a<<endl<<b<<endl;
//     for(int i = 2; i<n ; i++){
//         n_term=a+b;
//         cout<<n_term<<endl;
//         a=b;
//         b=n_term;
//     }
// }
// int main(){
//     fib num1;
//     num1.fibo();
//     return 0;
// }


//******Practical 5 - Destructer******* */
// 1st***
// #include<iostream>
// using namespace std;
// class cons{
//     int a;
//     int b;
//     public:
//     cons(){
//         cout<<"Default Constructer\n";
//     }
//     cons(int x){
//         cout<<"One Para\n";
//     }
//     cons(int x, int y){
//         cout<<"Two Para\n";
//     }
//     ~cons(){
//         cout<<"Destructer Invoked\n";
//     }
// };
// int main(){
//     {cons ob1;}
//     {cons ob2(4);}
//     cons ob3(5,7);
//     return 0;
// }

//*** 2nd */
// #include<iostream>
// using namespace std;
// int a;
// class xyz{
//     public:
//     ~xyz(){
//         a=111;
//     }
// };
// int abc(){
//     a = 77;
//     {xyz ob1;}
//     return a;
// }
// int main(){
//     cout<< abc();
// }



// ******* Practical 6 -Copy Constructer ********
// #include<iostream>
// using namespace std;
// class ABC{
//   int a ;
//   int b ;
//   public:
//   ABC(){
//     a= 10;
//     b= 20;
//   }
//   ABC(int x, int y){
//     a=x;
//     b=y;
//   }
//   void printab(){
//     cout<<endl<<a<<endl<<b<<endl;
//   }
//   ABC(ABC &o){
//     a=o.a+5;
//     b=o.b+5;
//   }
// };

// int main(){
//   ABC v1;
//   ABC v2(30,40);
//   v2.printab();
//   ABC v3(v2);
//   // ABC v3=v2;
//   v3.printab();
//   return 0;
// }


/* Practical - 7 : Use of Switch Statement */
// #include<iostream>
// #include<iomanip>
// using namespace std;

// int sum(int x , int y ){
//   return x+y;
// }
// int sub(int x , int y ){
//   return x-y;
// }
// int mul(int x , int y ){
//   return x*y;
// }
// float divide(float x , float y ){
//   return x/y;
// }
// int mod(int x , int y ){
//   return x%y;
// }

// int main(){
//   int a,b;
//   char ch;
//   // char choice;
//   while(true){
//   char choice;
//   cout<<"Enter the operator: ";
//   cin>>ch; 
//   // if (ch=='q')
//   //   {
//   //     cout<<"You entered 'q' ";
//   //     break;
//   //   }
//   cout<<"Enter the numbers a and b :";
//   cin>>a>>b;
//     switch(ch){
//     case '+':
//     cout<<"You entered "<<ch<<endl;
//     cout<<"Answer = "<<sum(a,b)<<endl;
//     break;
//     case '-':
//     cout<<"You entered "<<ch<<endl;
//     cout<<"Answer = "<<sub(a,b)<<endl;
//     break;
//     case '*':
//     cout<<"You entered "<<ch<<endl;
//     cout<<"Answer = "<<mul(a,b)<<endl;
//     break;
//     case '/':
//     cout<<"You entered "<<ch<<endl;
//     cout<<"Answer = "<<divide(a,b)<<endl;
//     break;
//     case '%':
//     cout<<"You entered "<<ch<<endl;
//     cout<<fixed<<setprecision(3);
//     cout<<"Answer = "<<mod(a,b)<<endl;
//     break;
//     default:
//     cout<<"Invalid Operator "<<endl;
//   }
//   cout<<"Do you want to continue ? enter (y/n)";
//   cin>>choice;
//   if (choice=='n')
//     {
//       cout<<"You entered 'n' ";
//       break;
//     }
// }
//     return 0;
// }









// Operator Overloading of binary operators 
// #include<iostream>
// using namespace std;
// class complex{ // complex class created
//     // Data Members
//     int real ;
//     int img ; 
//     public:
//     complex(){ // Default Constructer
//         real = 0;
//         img = 0;
//     }
//     complex(int x , int y){ // Parametric Constructor
//         real = x;
//         img = y;
//     }
//     void display(){ // Display Member Function
//         (img>=0)?cout<<real<<" + i"<<img<<endl:cout<<real<<" - i"<<-img<<endl;
//     }
//     complex operator+(complex T){ // '+' operator overloading
//     complex ob;
//     ob.real = real + T.real;
//     ob.img = img + T.img;
//     return ob;
//     }
//     void operator >(complex T){ // '>' operator overloading
//         (real > T.real && img > T.img)? cout<<"True\n":cout<<"False\n";
//     }
//     void operator <(complex T){ // '<' operator overloading
//         (real < T.real && img < T.img)? cout<<"True\n":cout<<"False\n";
//     }
// };

// int main(){
//     complex C1; // C1 object 
//     C1.display(); // C1 output
//     complex C2(5,10); // C2 object 
//     C2.display();
//     complex C3(20,-40); // C3 object 
//     C3.display();
//     C1 = C2 + C3; // Initializing sum value of C2 and C3 object in C1 using Operator Overloading '+'
//     C1.display();
//     C1>C3; // '>' Operator overloading returns True
//     C1<C3; // '<' Operator Overloading returns False
//     return 0;
// }






// Operations and Programs on array using Class 
#include<iostream>
using namespace std;

class Array{
    public:
    int avgarr(int arr[], int n){ // member function for avg
        int sum = 0 ;
        for(int i = 0 ; i<n ; i++){
            sum+=arr[i];
        }
        int avg = (sum/n); // avg calculation
        return avg;
    }
    int maxnum(int arr[], int n){ // member function for max number 
        int max=arr[0];
        for(int i = 1 ; i<n ; i++){
            if(arr[i]>max){
                max = arr[i];
            }
        }
        return max;
    }
    int secondmax(int arr[], int n){ // member function for second max number
        int max=maxnum(arr, n); // calculation of max number by calling maxnum function 
        int max2=arr[0];
        for(int i = 1 ; i<n ; i++){
            // if(arr[i]>max){
            //     max = arr[i];
            // }
            if(arr[i]>max2 && arr[i]<max){
                max2=arr[i];
            }
        }
        return max2;
    }
};
int main(){
    int n;  // input n 
    cout<<"Enter n : ";
    cin>>n;
    int ar[n];
    cout<< "Enter Array elements :";
    for(int i = 0 ; i<n ; i++){ // input of array elements 
        cin>>ar[i];
    }
    Array A1; // A1 object created
    cout<<"Avg is : "<<A1.avgarr(ar, n)<<endl; // avg output
    cout<<"Max Number is : "<<A1.maxnum(ar, n)<<endl; // max number of array
    cout<<"Second Max Number is : "<<A1.secondmax(ar, n)<<endl; //second max number of array
    return 0;
}