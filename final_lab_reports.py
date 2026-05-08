#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, title, paragraph):
    report = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    # Paragraph objects handle the <br/> tags 
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["Normal"])
    report.build([report_title, Spacer(1, 20), report_info])