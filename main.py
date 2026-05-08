import warnings
from src.data_pipeline import DatasetMerger

# Ignore warnings for cleaner output
warnings.filterwarnings('ignore')

def main():
    # Inisialisasi proses merger
    merger = DatasetMerger()
    
    # Eksekusi penggabungan dan pembersihan
    merger.execute()
    
    # Simpan hasil akhir ke CSV
    merger.save('output/merged_crop_data.csv')

if __name__ == "__main__":
    main()
