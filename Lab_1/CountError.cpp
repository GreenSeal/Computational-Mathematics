#include<cmath>
#include<fstream>
#include<string>

int POINT_X = 5;

long double abs(long double x) {
    if(x >= 0.0l) return x;
    else return -x;
}

long double Func1(long double x) {
    return sin(x*x);
}
long double Func2(long double x) {
    return cos(sin(x));
}

long double Func3(long double x) {
    return exp(sin(cos(x)));
}

long double Func4(long double x) {
    return log(x+3);
}

long double Func5(long double x) {
    return sqrt(x+3);
}

long double DiffFunc1(long double x) {
    return cos(x*x)*2*x;
}
long double DiffFunc2(long double x) {
    return -sin(sin(x))*cos(x);
}

long double DiffFunc3(long double x) {
    return exp(sin(cos(x)))*cos(cos(x))*(-sin(x));
}

long double DiffFunc4(long double x) {
    return 1/(x+3);
}

long double DiffFunc5(long double x) {
    return 1/(2*sqrt(x+3));
}

long double Formula1(long double (*func)(long double), long double x, long double h) {
    return (func(x+h) - func(x))/h;
}

long double Formula2(long double (*func)(long double), long double x, long double h) {
    return (func(x) - func(x-h))/h;
}

long double Formula3(long double (*func)(long double), long double x, long double h) {
    return (func(x+h) - func(x-h))/(2*h);
}

long double Formula4(long double (*func)(long double), long double x, long double h) {
    return 4*(func(x+h) - func(x-h))/(3*2*h) - (func(x+2*h) - func(x-2*h))/(3*4*h);
}

long double Formula5(long double (*func)(long double), long double x, long double h) {
    return 3*((func(x+h) - func(x-h))/(2*2*h)) - 3*((func(x+2*h) - func(x-2*h))/(5*4*h)) + (func(x+3*h) - func(x-3*h))/(10*6*h);
}

void WriteData(std::ofstream& output, long double (*DiffFunc)(long double), long double (*Func)(long double)) {
    setlocale(LC_ALL,"Russian");
    //SetConsoleOutputCP(1251);
    //SetConsoleCP(1251);
    long double d_func = DiffFunc(POINT_X);
    output << "h;form1;form2;form3;form4;form5\n";
    for (int i = 0; i < 41; ++i) {
	long double h = pow(0.5, i+1);
	std::string str_res1 = std::to_string(abs(d_func - Formula1(Func, POINT_X, h)));
    	std::string str_res2 = std::to_string(abs(d_func - Formula2(Func, POINT_X, h)));
        std::string str_res3 = std::to_string(abs(d_func - Formula3(Func, POINT_X, h)));
        std::string str_res4 = std::to_string(abs(d_func - Formula4(Func, POINT_X, h)));
        std::string str_res5 = std::to_string(abs(d_func - Formula5(Func, POINT_X, h)));

        output << h << ";" << str_res1.replace(str_res1.find("."), 1, ",") << ";"; 
        output << str_res2.replace(str_res2.find("."), 1, ",") << ";" ;
        output << str_res3.replace(str_res3.find("."), 1, ",") << ";";
        output << str_res4.replace(str_res4.find("."), 1, ",") << ";";
        output << str_res5.replace(str_res5.find("."), 1, ",") << "\n";
	
    }
}

int main() {
    std::string path_and_file = "/mnt/c/Users/denis/Documents/Вычматы/Output";
    std::string file_type = ".csv";

    std::ofstream output1(path_and_file + std::to_string(1) + file_type);
    WriteData(output1, DiffFunc1, Func1);

    std::ofstream output2(path_and_file + std::to_string(2) + file_type);
    WriteData(output2, DiffFunc2, Func2);
    
    std::ofstream output3(path_and_file + std::to_string(3) + file_type);
    WriteData(output3, DiffFunc3, Func3);

    std::ofstream output4(path_and_file + std::to_string(4) + file_type);
    WriteData(output4, DiffFunc4, Func4);

    std::ofstream output5(path_and_file + std::to_string(5) + file_type);
    WriteData(output5, DiffFunc5, Func5);
    
    return 0;
}
