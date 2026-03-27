new_name = "Luke"                                       #dodaję nową nazwę do pliku names.txt, ale nie nadpisuję go, tylko dopisuję do niego, więc używam trybu 'a' czyli append, a nie 'w' czyli write, bo ten drugi tryb nadpisuje cały plik, a ja chcę tylko dopisać nową nazwę do istniejącego pliku.
with open("names.txt", 'a') as write_file:
    write_file.write(new_name)


new_name = "Luke"                                       #tworzymy nowy plik new_names.txt i zapisujemy do niego nową nazwę, ale tym razem używamy trybu 'w' czyli write, bo chcemy nadpisać cały plik, a nie dopisać do niego, więc jeśli plik już istnieje, to zostanie nadpisany, a jeśli nie istnieje, to zostanie utworzony.    
with open("new_names.txt", 'w') as write_file:
    write_file.write(new_name)

