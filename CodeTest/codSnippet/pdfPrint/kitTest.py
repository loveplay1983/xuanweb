# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""

import pdfkit

options = {
    # 'quiet': '',
    'page-size': 'A4',
    'margin-top': '0.0001cm',
    'margin-right': '0.0001cm',
    'margin-bottom': '0.0001cm',
    'margin-left': '0.0001cm',
    'disable-smart-shrinking': '',
    'dpi': 300
}

pdfkit.from_url("http://localhost:5000/patients/4", "4.pdf", options=options)

# from weasyprint import HTML
# pdf = HTML("http://localhost:5000/patients/10").write_pdf("weasy.pdf")
