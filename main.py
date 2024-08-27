from fpdf import FPDF
import pandas as pd

# creates instances of pdf's
pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", size=24)
    pdf.set_text_color(254, 50, 50)
    pdf.cell(w=0, h=12, txt=row["Topic"],
             align="L", ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

# sets the font

# w = width, 0 end of the page side to side
# ln = break line
# height similar to the text size



# generates the pdf
pdf.output("output.pdf")