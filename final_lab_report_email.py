#!/usr/bin/env python3
import os, datetime, reports, emails

def process_data(directory):
    report_content = ""
    for file in sorted(os.listdir(directory)):
        if file.endswith(".txt"):
            with open(os.path.join(directory, file), 'r') as f:
                lines = f.readlines()
                report_content += f"name: {lines[0].strip()}<br/>weight: {lines[1].strip()}<br/><br/>"
    return report_content

if __name__ == "__main__":
    path = os.path.expanduser("~") + "/supplier-data/descriptions/"
    title = f"Processed Update on {datetime.date.today().strftime('%B %d, %Y')}"
    paragraph = process_data(path)
    reports.generate_report("/tmp/processed.pdf", title, paragraph)
    
    msg = emails.generate_email("automation@example.com", "student@example.com", 
                                "Upload Completed - Online Fruit Store", 
                                "All fruits are uploaded successfully.", "/tmp/processed.pdf")
    emails.send_email(msg)