
namespace CS322_DZ02_Stefan_Gogic_4056
{
	partial class Form1
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Windows Form Designer generated code

		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			this.label1 = new System.Windows.Forms.Label();
			this.label2 = new System.Windows.Forms.Label();
			this.label3 = new System.Windows.Forms.Label();
			this.textBoxIme = new System.Windows.Forms.TextBox();
			this.textBoxAdresa = new System.Windows.Forms.TextBox();
			this.textBoxPrezime = new System.Windows.Forms.TextBox();
			this.button1 = new System.Windows.Forms.Button();
			this.textBoxJMBG = new System.Windows.Forms.TextBox();
			this.textBoxBrojLicneKarte = new System.Windows.Forms.TextBox();
			this.textBoxTelefon = new System.Windows.Forms.TextBox();
			this.label4 = new System.Windows.Forms.Label();
			this.label5 = new System.Windows.Forms.Label();
			this.label6 = new System.Windows.Forms.Label();
			this.labelGreska = new System.Windows.Forms.Label();
			this.labelNacionalnost = new System.Windows.Forms.Label();
			this.SuspendLayout();
			// 
			// label1
			// 
			this.label1.AutoSize = true;
			this.label1.Location = new System.Drawing.Point(358, 61);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(30, 17);
			this.label1.TabIndex = 0;
			this.label1.Text = "Ime";
			this.label1.Click += new System.EventHandler(this.label1_Click);
			// 
			// label2
			// 
			this.label2.AutoSize = true;
			this.label2.Location = new System.Drawing.Point(358, 123);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(59, 17);
			this.label2.TabIndex = 1;
			this.label2.Text = "Prezime";
			// 
			// label3
			// 
			this.label3.AutoSize = true;
			this.label3.Location = new System.Drawing.Point(358, 183);
			this.label3.Name = "label3";
			this.label3.Size = new System.Drawing.Size(53, 17);
			this.label3.TabIndex = 2;
			this.label3.Text = "Adresa";
			// 
			// textBoxIme
			// 
			this.textBoxIme.Location = new System.Drawing.Point(466, 61);
			this.textBoxIme.Name = "textBoxIme";
			this.textBoxIme.Size = new System.Drawing.Size(100, 22);
			this.textBoxIme.TabIndex = 3;
			this.textBoxIme.TextChanged += new System.EventHandler(this.textBoxIme_TextChanged);
			// 
			// textBoxAdresa
			// 
			this.textBoxAdresa.Location = new System.Drawing.Point(466, 180);
			this.textBoxAdresa.Name = "textBoxAdresa";
			this.textBoxAdresa.Size = new System.Drawing.Size(100, 22);
			this.textBoxAdresa.TabIndex = 4;
			// 
			// textBoxPrezime
			// 
			this.textBoxPrezime.Location = new System.Drawing.Point(466, 120);
			this.textBoxPrezime.Name = "textBoxPrezime";
			this.textBoxPrezime.Size = new System.Drawing.Size(100, 22);
			this.textBoxPrezime.TabIndex = 5;
			// 
			// button1
			// 
			this.button1.Location = new System.Drawing.Point(429, 443);
			this.button1.Name = "button1";
			this.button1.Size = new System.Drawing.Size(75, 23);
			this.button1.TabIndex = 6;
			this.button1.Text = "Unesi";
			this.button1.UseVisualStyleBackColor = true;
			this.button1.Click += new System.EventHandler(this.button1_Click);
			// 
			// textBoxJMBG
			// 
			this.textBoxJMBG.Location = new System.Drawing.Point(466, 297);
			this.textBoxJMBG.Name = "textBoxJMBG";
			this.textBoxJMBG.Size = new System.Drawing.Size(100, 22);
			this.textBoxJMBG.TabIndex = 12;
			// 
			// textBoxBrojLicneKarte
			// 
			this.textBoxBrojLicneKarte.Location = new System.Drawing.Point(466, 357);
			this.textBoxBrojLicneKarte.Name = "textBoxBrojLicneKarte";
			this.textBoxBrojLicneKarte.Size = new System.Drawing.Size(100, 22);
			this.textBoxBrojLicneKarte.TabIndex = 11;
			// 
			// textBoxTelefon
			// 
			this.textBoxTelefon.Location = new System.Drawing.Point(466, 238);
			this.textBoxTelefon.Name = "textBoxTelefon";
			this.textBoxTelefon.Size = new System.Drawing.Size(100, 22);
			this.textBoxTelefon.TabIndex = 10;
			// 
			// label4
			// 
			this.label4.AutoSize = true;
			this.label4.Location = new System.Drawing.Point(358, 360);
			this.label4.Name = "label4";
			this.label4.Size = new System.Drawing.Size(102, 17);
			this.label4.TabIndex = 9;
			this.label4.Text = "Broj lične karte";
			// 
			// label5
			// 
			this.label5.AutoSize = true;
			this.label5.Location = new System.Drawing.Point(358, 300);
			this.label5.Name = "label5";
			this.label5.Size = new System.Drawing.Size(46, 17);
			this.label5.TabIndex = 8;
			this.label5.Text = "JMBG";
			// 
			// label6
			// 
			this.label6.AutoSize = true;
			this.label6.Location = new System.Drawing.Point(358, 238);
			this.label6.Name = "label6";
			this.label6.Size = new System.Drawing.Size(56, 17);
			this.label6.TabIndex = 7;
			this.label6.Text = "Telefon";
			this.label6.Click += new System.EventHandler(this.label6_Click);
			// 
			// labelGreska
			// 
			this.labelGreska.AutoSize = true;
			this.labelGreska.Location = new System.Drawing.Point(466, 407);
			this.labelGreska.Name = "labelGreska";
			this.labelGreska.Size = new System.Drawing.Size(0, 17);
			this.labelGreska.TabIndex = 13;
			// 
			// labelNacionalnost
			// 
			this.labelNacionalnost.AutoSize = true;
			this.labelNacionalnost.Location = new System.Drawing.Point(622, 124);
			this.labelNacionalnost.Name = "labelNacionalnost";
			this.labelNacionalnost.Size = new System.Drawing.Size(0, 17);
			this.labelNacionalnost.TabIndex = 14;
			this.labelNacionalnost.Click += new System.EventHandler(this.label7_Click);
			// 
			// Form1
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(875, 525);
			this.Controls.Add(this.labelNacionalnost);
			this.Controls.Add(this.labelGreska);
			this.Controls.Add(this.textBoxJMBG);
			this.Controls.Add(this.textBoxBrojLicneKarte);
			this.Controls.Add(this.textBoxTelefon);
			this.Controls.Add(this.label4);
			this.Controls.Add(this.label5);
			this.Controls.Add(this.label6);
			this.Controls.Add(this.button1);
			this.Controls.Add(this.textBoxPrezime);
			this.Controls.Add(this.textBoxAdresa);
			this.Controls.Add(this.textBoxIme);
			this.Controls.Add(this.label3);
			this.Controls.Add(this.label2);
			this.Controls.Add(this.label1);
			this.Name = "Form1";
			this.Text = "Form1";
			this.Load += new System.EventHandler(this.Form1_Load);
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Label label1;
		private System.Windows.Forms.Label label2;
		private System.Windows.Forms.Label label3;
		private System.Windows.Forms.TextBox textBoxIme;
		private System.Windows.Forms.TextBox textBoxAdresa;
		private System.Windows.Forms.TextBox textBoxPrezime;
		private System.Windows.Forms.Button button1;
		private System.Windows.Forms.TextBox textBoxJMBG;
		private System.Windows.Forms.TextBox textBoxBrojLicneKarte;
		private System.Windows.Forms.TextBox textBoxTelefon;
		private System.Windows.Forms.Label label4;
		private System.Windows.Forms.Label label5;
		private System.Windows.Forms.Label label6;
		private System.Windows.Forms.Label labelGreska;
		private System.Windows.Forms.Label labelNacionalnost;
	}
}

