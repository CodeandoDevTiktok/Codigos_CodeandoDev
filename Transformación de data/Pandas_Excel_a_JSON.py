import pandas

excel = pandas.read_excel("data_excel_a_json.xlsx",sheet_name="Hoja1")

excel.to_json("data.json",orient = "records")