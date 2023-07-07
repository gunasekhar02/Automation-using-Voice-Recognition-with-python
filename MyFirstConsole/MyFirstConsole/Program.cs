using System;

namespace MyFirstConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = 10;
            int b = 90;
            int temp;
            temp = a;
            a = b;
            b= temp;
            Console.WriteLine(a);
            Console.WriteLine(b);

            Console.WriteLine("Hello World!");

        }
    }
}
