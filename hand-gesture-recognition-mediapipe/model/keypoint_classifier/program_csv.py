import pandas as pd

# Tentukan path lengkap ke file CSV
path_file_csv = 'keypoint.csv'

# Baca file CSV menggunakan Pandas
data_csv = pd.read_csv(path_file_csv)

# Tampilkan data
print(data_csv)
