using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;


namespace DOI_Query {
	public partial class Form1 : Form {
		string[] lines;
		public Form1() {
			InitializeComponent();
		}

		private void button2_Click(object sender, EventArgs e) {
			System.Diagnostics.Process p = new System.Diagnostics.Process();
			p.StartInfo.FileName = "cmd.exe";
			p.StartInfo.Arguments = "/C python query.py " + textBox1.Text;
			//p.StartInfo.FileName = "python query.py " + textBox1.Text;
			p.StartInfo.UseShellExecute = false;
			p.StartInfo.RedirectStandardInput = true;
			//p.StartInfo.RedirectStandardOutput = true;
			p.Start();
			p.WaitForExit();
			//p.StandardInput.WriteLine("python query.py " + textBox1.Text);
			//p.StandardInput.WriteLine("exit");
			
			p.Close();
			lines = System.IO.File.ReadAllLines(@"result.txt");
			listBox1.Items.Clear();
			for (int i = 0; i < lines.Length; i += 26) {
				listBox1.Items.Add(lines[i]);
			}
			label29.Text = listBox1.Items.Count.ToString();
		}

		private void Form1_Load(object sender, EventArgs e) {
			lines = System.IO.File.ReadAllLines(@"result.txt");
			listBox1.Items.Clear();
			for (int i = 0; i < lines.Length; i += 26) {
				listBox1.Items.Add(lines[i]);
			}
			label29.Text = listBox1.Items.Count.ToString();
			linkLabel1.Links[0].LinkData = "http://www.devchen.com/";
		}

		private void listBox1_SelectedIndexChanged(object sender, EventArgs e) {
			textBox2.Text = lines[listBox1.SelectedIndex * 26 + 1];
			textBox3.Text = lines[listBox1.SelectedIndex * 26 + 2];
			textBox4.Text = lines[listBox1.SelectedIndex * 26 + 3];
			textBox5.Text = lines[listBox1.SelectedIndex * 26 + 4];
			textBox6.Text = lines[listBox1.SelectedIndex * 26 + 5];
			textBox26.Text = lines[listBox1.SelectedIndex * 26 + 6];
			textBox27.Text = lines[listBox1.SelectedIndex * 26 + 7];
			textBox7.Text = lines[listBox1.SelectedIndex * 26 + 8];
			textBox9.Text = lines[listBox1.SelectedIndex * 26 + 9];
			textBox10.Text = lines[listBox1.SelectedIndex * 26 + 10];
			textBox11.Text = lines[listBox1.SelectedIndex * 26 + 11];
			textBox12.Text = lines[listBox1.SelectedIndex * 26 + 12];
			textBox13.Text = lines[listBox1.SelectedIndex * 26 + 13];
			textBox16.Text = lines[listBox1.SelectedIndex * 26 + 14];
			textBox15.Text = lines[listBox1.SelectedIndex * 26 + 15];
			textBox14.Text = lines[listBox1.SelectedIndex * 26 + 16];
			textBox19.Text = lines[listBox1.SelectedIndex * 26 + 17];
			textBox18.Text = lines[listBox1.SelectedIndex * 26 + 18];
			textBox17.Text = lines[listBox1.SelectedIndex * 26 + 19];
			textBox22.Text = lines[listBox1.SelectedIndex * 26 + 20];
			textBox21.Text = lines[listBox1.SelectedIndex * 26 + 21];
			textBox20.Text = lines[listBox1.SelectedIndex * 26 + 22];
			textBox25.Text = lines[listBox1.SelectedIndex * 26 + 23];
			textBox24.Text = lines[listBox1.SelectedIndex * 26 + 24];
			textBox23.Text = lines[listBox1.SelectedIndex * 26 + 25];
			linkLabel1.Links[0].LinkData = "https://doi.org/" + lines[listBox1.SelectedIndex * 26];
			textBox8.Text = "https://doi.org/" + lines[listBox1.SelectedIndex * 26];
		}

		private void button1_Click(object sender, EventArgs e) {
			MessageBox.Show("Useage:\nSelect the folder which contains the data files and press Query.\nThe result will display in the window when finished.\nClick output to save CSV file for future use.\n\n\nDOI Query 文献管理系统\nCopyright 2016 BJUT\nAPI provided by http://www.altmetric.com/", "About DOI Query");
		}

		private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e) {
			System.Diagnostics.Process.Start(linkLabel1.Links[0].LinkData.ToString());
		}

		private void button3_Click(object sender, EventArgs e) {
			//output the csv
			using (System.IO.StreamWriter file =
			new System.IO.StreamWriter(@"output.csv")) {
				file.WriteLine("DOI,Title,Author,Info,Abstract,Keywords,U1,U2,Posts,Delicious,Facebook,Blogs,Forums,Google+,LinkedIn,News,Peer,Pinterest,Policy,QAs,Reddit,Research,Twitter,Youtube,Weibo,Wikipedia");
				for (int i = 0; i < lines.Length; i += 26) {
					string nowLine = "\"" + lines[i];
					for (int ii = 1; ii < 26; ii++) {
						nowLine += ("\",\"" + lines[i + ii]);
					}
					nowLine += "\"";
					file.WriteLine(nowLine);
				}
			}

			//open explorer and locate
			System.Diagnostics.ProcessStartInfo psi = new System.Diagnostics.ProcessStartInfo("Explorer.exe");
			psi.Arguments = "/e,/select,output.csv";
			System.Diagnostics.Process.Start(psi);
		}

		private void button4_Click(object sender, EventArgs e) {
			FolderBrowserDialog dilog = new FolderBrowserDialog();
			dilog.Description = "Select data folder: ";
			if (dilog.ShowDialog() == DialogResult.OK) {
				textBox1.Text = dilog.SelectedPath;
			}
		}
		void search() {
			if (textBox28.Text != "") {
				int idx = listBox1.FindString(textBox28.Text);
				if (idx == ListBox.NoMatches) {
					MessageBox.Show("Not found.");
				}
				else {
					listBox1.SelectedIndex = idx;
				}

			}
			else {
				MessageBox.Show("Search string cannot be empty.");
			}
		}
		private void button5_Click(object sender, EventArgs e) {
			search();
		}

		private void textBox2_KeyDown(object sender, KeyEventArgs e) {
			if (e.Modifiers == Keys.Control && e.KeyCode == Keys.A) {
				((TextBox)sender).SelectAll();
			}
		}

		private void textBox3_KeyDown(object sender, KeyEventArgs e) {
			if (e.Modifiers == Keys.Control && e.KeyCode == Keys.A) {
				((TextBox)sender).SelectAll();
			}
		}

		private void textBox4_KeyDown(object sender, KeyEventArgs e) {
			if (e.Modifiers == Keys.Control && e.KeyCode == Keys.A) {
				((TextBox)sender).SelectAll();
			}
		}

		private void textBox5_KeyDown(object sender, KeyEventArgs e) {
			if (e.Modifiers == Keys.Control && e.KeyCode == Keys.A) {
				((TextBox)sender).SelectAll();
			}
		}

		private void textBox6_KeyDown(object sender, KeyEventArgs e) {
			if (e.Modifiers == Keys.Control && e.KeyCode == Keys.A) {
				((TextBox)sender).SelectAll();
			}
		}

		private void textBox8_KeyDown(object sender, KeyEventArgs e) {
			if (e.Modifiers == Keys.Control && e.KeyCode == Keys.A) {
				((TextBox)sender).SelectAll();
			}
		}

		private void textBox28_KeyDown(object sender, KeyEventArgs e) {
			if (e.Modifiers == Keys.Control && e.KeyCode == Keys.A) {
				((TextBox)sender).SelectAll();
			}
			if (e.KeyCode == Keys.Enter) {
				search();
			}
		}
	}
}
