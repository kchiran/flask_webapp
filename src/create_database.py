from sqlalchemy_utils import database_exists, create_database
from config import Config


def create_database_new(db_url_new):
    if not database_exists(db_url_new):
        create_database(db_url_new)
        print(f"Database created at {db_url_new}")
        return
    print(f"Database already exists at {db_url_new}")
    return


if __name__ == '__main__':
    config = Config()
    db_url = config.SQLALCHEMY_DATABASE_URI
    create_database_new(db_url)