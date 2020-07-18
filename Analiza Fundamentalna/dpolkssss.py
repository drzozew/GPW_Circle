from update_csv import Update_csv_file as UPF
from read_file_csv import Read_file as RF



x = UPF('testowy.csv', None, None, None, None, None)
x.spolka_data_add(x.data_add())


y = RF('testowy.csv')
y.print_file(y.read_file())
