# TechSphere Corporation - Payroll Automation Test

from fpdf import FPDF

def generate_invoice(emp_name, amount, file_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="TechSphere Corporation - Payroll Invoice", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Employee: {emp_name}", ln=True)
    pdf.cell(200, 10, txt=f"Amount: ₹{amount}", ln=True)
    pdf.output(file_name)

# Example
generate_invoice("EmployeeX", "50000", "invoice.pdf")
