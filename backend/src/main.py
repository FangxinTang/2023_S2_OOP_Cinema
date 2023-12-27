"""Project Root. Handles Litestar app setup"""
from backend.src.database import db_init

def main():
    db_init.init_database()
    

if __name__ == "__main__":
    main()