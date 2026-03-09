import os

# Konfiguracja ścieżek
source_path = '/mnt/data/input_sequences.txt'
index_file = 'indeksy.txt' # Założenie: plik z mapowaniem indeks -> nazwa
output_dir = './wyniki/'

# Słownik indeksów (przykład: {'ATCGATCG': 'pacjent_1.txt'})
index_map = {
    'ATCGATCG': 'probka_A.txt',
    'GCTAGCTA': 'probka_B.txt'
}

def demultiplex():
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(source_path, 'r') as f_in, \
         open(os.path.join(output_dir, 'undetermined.txt'), 'w') as f_undeter:
        
        # Otwieramy pliki wynikowe dynamicznie (opcjonalnie można użyć słownika uchwytów)
        for line in f_in:
            sequence = line.strip()
            if len(sequence) < 16:
                f_undeter.write(sequence + '\n')
                continue

            # Pobranie indeksów
            start_index = sequence[:8]
            end_index = sequence[-8:]

            # Logika przypisania (tutaj sprawdzamy np. tylko startowy lub oba)
            if start_index in index_map:
                file_name = index_map[start_index]
                with open(os.path.join(output_dir, file_name), 'a') as f_out:
                    f_out.write(sequence + '\n')
            else:
                f_undeter.write(sequence + '\n')

if __name__ == "__main__":
    demultiplex()