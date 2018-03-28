/////////////////
///实习周题目13//
//////Ver.1//////
/////Write By////
///秦武，胡启东//
/////////////////
#include <iostream>
#include <cstring>
using namespace std;
char w[1000010];
char t[1000010];
int lenw, lent;
int scan(char x[])
{
	cin >> x;
	return strlen(x);
}
int run()
{
	int cnt = 0;
	for (int i = 0; i < lenw; i++)
	{
		int flag = 1;
		for (int j = 0; j < lent; j++)
		{
			if (*(t + j) != *(w + i + j))
			{
				flag = 0;
				break;
			}
		}
		if (flag) cnt++;
	}
	return cnt;
}
int main()
{
	cout << "欢迎使用字符串匹配程序\n";
	cout << "结束程序请输入###\n";
	while (1)
	{
		cout << "请输入主串（串1）\n";
		lenw = scan(w);
		if (lenw == 3 && w[0] == '#'&&w[1] == '#'&&w[2] == '#') break;
		cout << "请输入待匹配子串（串2）\n";
		lent = scan(t);
		cout <<"串2在串1中出现了"<< run()<<"次" << endl;
	}
	return 0;
}