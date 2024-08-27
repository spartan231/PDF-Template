from fpdf import FPDF
import pandas as pd

# creates instances of pdf's
pdf = FPDF(orientation="P", unit="mm", format="A4")

# pages not broken auto

pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", size=24)
    pdf.set_text_color(254, 50, 50)
    pdf.cell(w=0, h=12, txt=row["Topic"],
             align="L", ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)

    # set the footer for the header page
    pdf.ln(265)
    pdf.set_font(family="Times",style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(280)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

# sets the font

# w = width, 0 end of the page side to side
# ln = break line
# height similar to the text size



# generates the pdf
pdf.output("output.pdf")