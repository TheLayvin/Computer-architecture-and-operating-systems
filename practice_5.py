import pandas as pd

def get_fs_data():
    data = {
        "Критерій": [
            "Розробник", 
            "Основний принцип", 
            "Оптимізація", 
            "Цілісність даних", 
            "Знімки (Snapshots)", 
            "Шифрування", 
            "Керування простором"
        ],
        "NTFS (Windows)": [
            "Microsoft",
            "Журналювання (Journaling)",
            "Універсальна (HDD та SSD)",
            "Журнал транзакцій",
            "Обмежена (VSS)",
            "BitLocker (зовнішнє)",
            "Фіксовані розділи"
        ],
        "APFS (macOS)": [
            "Apple",
            "Copy-on-Write (CoW)",
            "Спеціально для SSD",
            "Атомарний запис (CoW)",
            "Вбудована, миттєва",
            "Вбудоване багаторівневе",
            "Space Sharing (спільний)"
        ]
    }
    return data

def display_analysis():
    print("=== Аналіз файлових систем: Варіант 21 ===")
    print("Порівняння NTFS та APFS для настільних ОС\n")
    
    data = get_fs_data()
    df = pd.DataFrame(data)

    print(df.to_string(index=False))
    
    print("\n--- Короткий висновок ---")
    print("APFS — це сучасна CoW-система, що ідеально підходить для SSD та швидких бекапів.")
    print("NTFS — перевірена часом журнальована система, що є стандартом для екосистеми Windows.")

def detailed_info(criterion_index):
    data = get_fs_data()
    crit = data["Критерій"][criterion_index]
    ntfs_val = data["NTFS (Windows)"][criterion_index]
    apfs_val = data["APFS (macOS)"][criterion_index]
    
    print(f"\nДетальніше про '{crit}':")
    print(f" - В NTFS: {ntfs_val}. Це забезпечує стабільність на старих і нових дисках.")
    print(f" - В APFS: {apfs_val}. Це дає перевагу у швидкості та гнучкості на сучасних Mac.")

if __name__ == "__main__":
    try:
        display_analysis()
        detailed_info(4)
        
    except ImportError:
        print("Для гарного форматування таблиці встановіть pandas: pip install pandas")
        data = get_fs_data()
        for i in range(len(data["Критерій"])):
            print(f"{data['Критерій'][i]}: NTFS -> {data['NTFS (Windows)'][i]} | APFS -> {data['APFS (macOS)'][i]}")