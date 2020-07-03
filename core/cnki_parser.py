import os
import openpyxl


class CNKIFormatItem(object):
    def __init__(self):
        self.elements = []





def format_parser_helper(path, format):
    try:
        files = os.listdir(path)
        for file in files:
            if format == 'CNKI':
                parser = CNKIFormatParser()
                parser.parse_cnki_files(file)
    except Exception as e:
        print(str(e))




class CNKIFormatParser(object):
    def __init__(self):
        pass

    def parse_cnki_files(self, file):
        try:
            wb = openpyxl.load_workbook(file)
            ws = wb.active
            rows = ws.max_row   
            columns = ws.max_column         
            cnki_items = []
            chinese = True
            for row in range(2, rows+1):
                guard = ws.cell(row, 1).value
                if guard == None:
                    continue
                elif guard == 'RT':
                    chinese = False
                    continue
                if chinese is True:
                    item = CNKIFormatItem()
                    for column in range(1, columns):                    
                        item.elements.append(ws.cell(row=row, column=column).value)
                elif chinese is False:
                    item = CNKIFormatItem()
                    for column in range(1, 10):                    
                        item.elements.append(ws.cell(row=row, column=column).value)
                    item.elements.append(None)
                    item.elements.append(ws.cell(row=row, column=10).value)
                    item.elements.append(ws.cell(row=row, column=11).value)  
                    item.elements.append(None)
                    item.elements.append(None)
                    item.elements.append(None)
                    item.elements.append(ws.cell(row=row, column=12).value)
                cnki_items.append(item)
            return cnki_items
        except Exception as e:
            print(str(e))


if __name__ == '__main__':
    path = "F:\\002-测试数据\\NewNetworkAttack\\input\\CNKI-637293898682050000.xlsx"
    parser = CNKIFormatParser()
    items = parser.parse_cnki_files(path)
    for item in items:
        print(item)