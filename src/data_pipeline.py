import pandas as pd
from src.config import DATA_FILES, RENAME_MAP, COMMON_COLS

class DatasetMerger:
    def __init__(self):
        self.merged_df = None

    def execute(self):
        print("--- Memulai Proses Penggabungan Dataset ---")
        
        # 1. Load & Standardize
        dfs = []
        try:
            for i, file_path in enumerate(DATA_FILES):
                df = pd.read_csv(file_path)
                print(f"Dataset {i+1}: {len(df)} baris dimuat dari {file_path}")
                
                # Standarisasi kolom jika file kedua (Crop_recommendation-2.csv)
                # Dalam list kita, index 1 adalah file kedua
                if i == 1:
                    df = df.rename(columns=RENAME_MAP)
                
                dfs.append(df[COMMON_COLS])
        except Exception as e:
            print(f"Gagal memuat file: {e}")
            return None

        # 2. Penggabungan (Concatenation)
        combined = pd.concat(dfs, ignore_index=True)
        print(f"Total baris setelah penggabungan: {len(combined)}")

        # 4. Normalisasi Label
        # Menyeragamkan format (lowercase & tanpa spasi) agar tidak ada duplikasi kategori
        combined['label'] = combined['label'].str.lower().str.replace(' ', '').str.strip()

        # 5. Pembersihan Duplikat
        before_drop = len(combined)
        combined = combined.drop_duplicates()
        after_drop = len(combined)
        print(f"Duplikat dihapus: {before_drop - after_drop} baris.")

        # 6. Final Quality Check
        print("\n--- Ringkasan Data Akhir ---")
        print(f"Jumlah baris: {len(combined)}")
        print(f"Jumlah kolom: {len(combined.columns)}")
        print(f"Jumlah label unik: {combined['label'].nunique()}")
        
        if combined.isnull().values.any():
            print("\n[Peringatan] Ditemukan missing values. Melakukan imputasi median...")
            combined = combined.fillna(combined.median(numeric_only=True))

        self.merged_df = combined
        return combined

    def save(self, output_path='data/merged_crop_recommendation.csv'):
        if self.merged_df is not None:
            self.merged_df.to_csv(output_path, index=False)
            print(f"\nDataset berhasil disimpan di: {output_path}")
        else:
            print("Tidak ada data untuk disimpan.")
