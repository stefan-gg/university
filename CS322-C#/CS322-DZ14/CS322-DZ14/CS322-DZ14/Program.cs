using System;

namespace CS322_DZ14
{
	class Program
	{
		static void Main(string[] args)
		{
			string[] HorosopskiZnaci = {"Ovan", "Bik",
										"Blizanci", "Rak", "Lav", "Devica",
										"Vaga", "Škorpija", "Strelac",
										"Jarac", "Vodolija", "Ribe" };

			Console.WriteLine("Unesite Vase ime : \n");
			string Ime = Console.ReadLine();
			Console.WriteLine("Unesite Vase prezime : \n");
			string Prezime = Console.ReadLine();

			string Pattern = "dd/MM/yyyy"; 
			Console.WriteLine("Unesite datum rodjenja (format dd/MM/yyyy) : \n");

			DateTime DatumRodjenja = DateTime.ParseExact(Console.ReadLine(), Pattern, null);

			int Dan = DatumRodjenja.Day;
			int Mesec = DatumRodjenja.Month;

			switch (Mesec)
			{
				case 1:
					if (Dan >= 1 && Dan <= 19)
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[9]);
						break;
					} else
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[10]);
						break;
					}

				case 2:
					if (Dan >= 1 && Dan <= 18)
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[10]);
						break;
					}
					else
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[11]);
						break;
					}

				case 3:
					if (Dan >= 1 && Dan <= 20)
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[11]);
						break;
					}
					else
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[0]);
						break;
					}

				case 4:
					if (Dan >= 1 && Dan <= 19)
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[0]);
						break;
					}
					else
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[1]);
						break;
					}

				case 5:
					if (Dan >= 1 && Dan <= 20)
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[1]);
						break;
					}
					else
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[2]);
						break;
					}

				case 6:
					if (Dan >= 1 && Dan <= 21)
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[2]);
						break;
					}
					else
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[3]);
						break;
					}

				case 7:
					if (Dan >= 1 && Dan <= 22)
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[3]);
						break;
					}
					else
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[4]);
						break;
					}

				case 8:
					if (Dan >= 1 && Dan <= 22)
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[4]);
						break;
					}
					else
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[5]);
						break;
					}

				case 9:
					if (Dan >= 1 && Dan <= 22)
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[5]);
						break;
					}
					else
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[6]);
						break;
					}

				case 10:
					if (Dan >= 1 && Dan <= 22)
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[6]);
						break;
					}
					else
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[7]);
						break;
					}

				case 11:
					if (Dan >= 1 && Dan <= 21)
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[7]);
						break;
					}
					else
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[8]);
						break;
					}

				case 12:
					if (Dan >= 1 && Dan <= 21)
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[8]);
						break;
					}
					else
					{
						Console.WriteLine("Vaš znak je " + HorosopskiZnaci[9]);
						break;
					}
			}
		}
	}
}