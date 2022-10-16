# -*- coding: utf-8 -*-
"""
Author : Michael Xuan
Project: Study
Email  : michaelxuan@hotmail.com
"""

# import pdfkit
# pdfkit.from_url("http://localhost:5000/patients/10", "10.pdf")


from weasyprint import HTML
pdf = HTML("http://localhost:5000/patients/10").write_pdf("weasy.pdf")
