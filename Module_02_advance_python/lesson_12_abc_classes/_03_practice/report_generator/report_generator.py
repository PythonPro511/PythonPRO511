from abc import ABC, abstractmethod


class ReportGenerator(ABC):

    @abstractmethod
    def generate_report(self, data):
        pass


class PDFReportGenerator(ReportGenerator):
    def generate_report(self, data):
        return f'PDF Report Content: {data}'

    def save_report(self, filename):
        print(f'Saving PDF report to {filename}.pdf')


class ExcelReportGenerator(ReportGenerator):
    def generate_report(self, data):
        return f'Excel Report Content: {data}'

    def save_report(self, filename):
        print(f'Saving Excel report to {filename}.xlsx')


class HTMLReportGenerator(ReportGenerator):
    def generate_report(self, data):
        # with open('data.html', 'w', encoding='utf-8') as file:
        #     file.write(f'<html><body>{data}</html></body>')
        return f'<html><body>{data}</html></body>'

    def save_report(self, filename):
        print(f'Saving HTML report to {filename}.html')


if __name__ == '__main__':
    pdf_gen = PDFReportGenerator()
    pdf_content = pdf_gen.generate_report("Sales Data")
    pdf_gen.save_report("sales_report")

    excel_gen = ExcelReportGenerator()
    excel_content = excel_gen.generate_report("Inventory List")
    excel_gen.save_report("inventory_report")

    html_gen = HTMLReportGenerator()
    html_content = html_gen.generate_report("User Statistics")
    html_gen.save_report("user_stats")
