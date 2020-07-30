import os
import os.path
import pandas as pd
import win32com.client as win32

class DataCleanning(object):
    def __init__(self, input_dir, output_dir):
        self._input_dir = input_dir
        self._output_dir = output_dir

    def clean_data(self):
        for file in os.listdir(self._input_dir):
            try:
                file_to_clean_path = os.path.join(self._input_dir, file)
                file_to_save = os.path.join(self._output_dir, file)
                csv_file = pd.read_excel(file_to_clean_path)
                max_rows = csv_file.shape[0]
                eng_row = max_rows
                to_drop = []
                for index in range(0, max_rows):
                    print(csv_file.iloc[index].values[2])
                    if pd.isnull(csv_file.iloc[index].values[2]):
                        print(index)
                        print('isnull')
                        # csv_file.drop([index], inplace=True)
                        to_drop.append(index)
                    elif csv_file.iloc[index].values[2] == 'A1':
                        eng_row = index
                        break
                # for item in to_drop:
                #     csv_file.drop([item], inplace=True)
                for index in range(eng_row, max_rows):
                    to_drop.append(index)
                csv_file.drop(to_drop, inplace=True)
                print(csv_file)
                csv_file.to_excel(file_to_save, index=False)
            except Exception as e:
                print(str(e))


    def translate_excel_format(self, src_dir, dst_dir):
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        for file in os.listdir(src_dir):
            try:
                file_to_translate = os.path.join(src_dir, file)
                file_to_save = os.path.join(dst_dir, file)
                wb = excel.Workbooks.Open(file_to_translate)
                wb.SaveAs(file_to_save, FileFormat=56)
            except Exception as e:
                print(str(e))
        excel.Application.Quit()