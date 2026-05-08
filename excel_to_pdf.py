"""
Excel to PDF Automator - Portfolio Project 1
Author: Vajira L.
Description: Converts Excel files to clean PDFs using pandas + reportlab
"""
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def excel_to_pdf(excel_path, pdf_path, sheet_name=0):
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    df = df.fillna('')
    
    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
    data = [df.columns.tolist()] + df.values.tolist()
    
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2c3e50')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('GRID', (0,0), (-1,-1), 1, colors.grey),
    ]))
    
    doc.build([table])
    print(f"Converted {len(df)} rows to {pdf_path}")

if __name__ == "__main__":
    excel_to_pdf("sample_data.xlsx", "output.pdf")
