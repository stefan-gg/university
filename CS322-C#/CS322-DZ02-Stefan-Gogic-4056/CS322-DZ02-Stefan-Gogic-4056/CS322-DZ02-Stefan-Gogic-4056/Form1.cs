using System;
using System.IO;
using System.Windows.Forms;

namespace CS322_DZ02_Stefan_Gogic_4056
{
	public partial class Form1 : Form
	{
		public Form1()
		{
			InitializeComponent();
		}

		private void label1_Click(object sender, EventArgs e)
		{

		}

		private void label6_Click(object sender, EventArgs e)
		{

		}

		private void button1_Click(object sender, EventArgs e)
		{
			int brojReciImena = textBoxIme.Text.Split(' ').Length;
			int brojReciPrezmena = textBoxPrezime.Text.Split(' ').Length;
			int brojReciAdresa = textBoxAdresa.Text.Split(' ').Length;



			if (brojReciImena != 1)
			{
				labelGreska.Text = "Ime mora biti 1 rec samo";
			}

			if (brojReciAdresa < 2)
			{
				labelGreska.Text = "Adresa mora biti najmanje 1 rec";
			}

			if (brojReciPrezmena > 0)
			{
				if (textBoxPrezime.Text.EndsWith("ic"))
				{
					labelNacionalnost.Text = "Osoba je iz Srbije ili iz BiH";
				}
				else if (textBoxPrezime.Text.EndsWith("ka"))
				{
					labelNacionalnost.Text = "Osoba je iz Makedonije i žensko je";
				}
				else if (textBoxPrezime.Text.EndsWith("ov"))
				{
					labelNacionalnost.Text = "Osoba je iz Makedonije i muško je";
				}

			}

			String poruka = textBoxIme.Text + " " + textBoxPrezime.Text + " " + textBoxJMBG.Text + " " + textBoxTelefon.Text + " " + textBoxAdresa.Text + " " + textBoxBrojLicneKarte.Text;

			MessageBox.Show(poruka);

			FileStream f = new FileStream("podaci.txt", FileMode.Create);
			StreamWriter s = new StreamWriter(f);

			s.WriteLine(poruka);
			s.Close();
			f.Close();

		}

		private void Form1_Load(object sender, EventArgs e)
		{
		}

		private void textBoxIme_TextChanged(object sender, EventArgs e)
		{

		}

		private void label7_Click(object sender, EventArgs e)
		{

		}

		private void button2_Click(object sender, EventArgs e)
		{
			this.BackColor = System.Drawing.Color.Yellow;
		}

		private void button3_Click(object sender, EventArgs e)
		{
			this.BackColor = System.Drawing.Color.Blue;
		}

		private void button4_Click(object sender, EventArgs e)
		{
			this.BackColor = System.Drawing.Color.Red;
		}

		private void button5_Click(object sender, EventArgs e)
		{
			labelTextBoxTekst.Text = textBox.Text;
		}
	}
}
