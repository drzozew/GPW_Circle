import csv


class Update_csv_file():

    def __init__(self, file_name, company_name, kwartal,
                 kurs_akcji_na_koniec_kwartalu,
                 zysk_netto_kwartal, ilosc_akcji_kwartal):
        self.file_name = file_name
        self.company_name = company_name
        self.kwartal = kwartal
        self.kurs_akcji_na_koniec_kwartalu = kurs_akcji_na_koniec_kwartalu
        self.zysk_netto_kwartal = zysk_netto_kwartal
        self.ilosc_akcji_kwartal = ilosc_akcji_kwartal

    def spolka_data_add(self):
        with open(self.file_name, mode='a') as f:
            spolka_writer = csv.writer(
                f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            spolka_writer.writerow([self.company_name, self.kwartal,
                                    self.kurs_akcji_na_koniec_kwartalu,
                                    self.zysk_netto_kwartal, self.ilosc_akcji_kwartal])

    def data_add(self):
        self.company_name = input("Podaj nazwę spólki: ")
        self.kwartal = input("Podaj kwartał: ")
        self.kurs_akcji_na_koniec_kwartalu = input(
            "Podaj kurs akcji na koniec kwartału: ")
        self.zysk_netto_kwartal = input("Podaj zysk netto za kwartał")
        self.ilosc_akcji_kwartal = input(
            "Podaj ilość akcji na ostatni dzien kwartału: ")