from pathlib import Path
BASE=Path(__file__).resolve().parent.parent
STATIC_DIR=BASE/"static"
DATA_DIR=BASE/"data"
DB_PATH=BASE/"medimind.db"
CSV_PATH=DATA_DIR/"health_faq.csv"
