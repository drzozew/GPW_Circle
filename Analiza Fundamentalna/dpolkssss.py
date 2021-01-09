from update_csv import Update_csv_file as UPF
from read_file_csv import Read_file as RF



"""x = UPF('testowy.csv', None, None, None, None, None)
x.data_add()
x.spolka_data_add()"""


y = RF('testowy.csv')
y.write_head(y.read_file())
