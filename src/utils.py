import pandas as pd
import os


def _get_file(filename="Organizations for Ecosystem Analysis.xlsx"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    organization_xl_path = os.path.join(current_dir,  '..', 'data', 'raw', filename)
    return organization_xl_path


def _get_column_as_list(file, header, column_name):
    df = pd.read_excel(file, header=header, usecols=[column_name])
    column_list = df[column_name].tolist()
    return column_list


_sheet = _get_file()

column_list = [x for x in _get_column_as_list(_sheet, 6, 'Website') if pd.notna(x)]

