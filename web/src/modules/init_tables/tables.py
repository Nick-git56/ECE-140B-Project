"""
"""
def create_tables(cursor):
    try:
        cursor.execute("""
            CREATE TABLE Customers (
            id          integer     AUTO_INCREMENT PRIMARY KEY,
            first_name  VARCHAR(30) NOT NULL,
            last_name   VARCHAR(30) NOT NULL,
            email       VARCHAR(50) NOT NULL,
            username    VARCHAR(50) NOT NULL,
            password    VARCHAR(50) NOT NULL,
            company_id  integer     NOT NULL,
            created_at  TIMESTAMP
            );
        """)
    except:
        print("Customers table already exists. Not recreating it.")

    try:
        cursor.execute("""
            CREATE TABLE Events (
            id                  integer     AUTO_INCREMENT PRIMARY KEY,
            name                VARCHAR(30) NOT NULL,
            datetime_start      VARCHAR(70) NOT NULL,
            datetime_end        VARCHAR(70) NOT NULL,
            street_address         VARCHAR(50) NOT NULL,
            city                VARCHAR(50) NOT NULL,
            state               VARCHAR(50) NOT NULL,
            country             VARCHAR(50) NOT NULL,
            postal_code         VARCHAR(50) NOT NULL,
            category            VARCHAR(50) NOT NULL,
            customer_id         integer     NOT NULL,
            created_at          TIMESTAMP
            );
        """)
    except:
        print("Events table already exists. Not recreating it.")

    try:
        cursor.execute("""
            CREATE TABLE Companies (
            id              integer     AUTO_INCREMENT PRIMARY KEY,
            name            VARCHAR(30) NOT NULL,
            payment         VARCHAR(50) NOT NULL,
            phone_number    VARCHAR(50) NOT NULL,
            street_address         VARCHAR(50) NOT NULL,
            city            VARCHAR(50) NOT NULL,
            state           VARCHAR(50) NOT NULL,
            country         VARCHAR(50) NOT NULL,
            postal_code     VARCHAR(50) NOT NULL,
            company_code    VARCHAR(50) NOT NULL,
            created_at      TIMESTAMP
            );
        """)
    except:
        print("Companies table already exists. Not recreating it.")

    try:
        cursor.execute("""
            CREATE TABLE Suites (
            id                  integer AUTO_INCREMENT PRIMARY KEY,
            name                VARCHAR(50) NOT NULL,
            number_active       integer NOT NULL,
            event_id            integer NOT NULL,
            created_at          TIMESTAMP
            );
        """)
    except:
        print("Suites table already exists. Not recreating it.")

    try:
        cursor.execute("""
            CREATE TABLE Services (
            id                  integer AUTO_INCREMENT PRIMARY KEY,
            name                VARCHAR(30) NOT NULL,
            event_id            integer NOT NULL,
            created_at          TIMESTAMP
            );
        """)
    except:
        print("Services table already exists. Not recreating it.")

    try:
        cursor.execute("""
            CREATE TABLE Users (
            id                  integer     AUTO_INCREMENT PRIMARY KEY,
            first_name          VARCHAR(30) NOT NULL,
            last_name           VARCHAR(30) NOT NULL,
            phone_number        VARCHAR(30) NOT NULL,
            email               VARCHAR(50) NOT NULL,
            username            VARCHAR(50) NOT NULL,
            password            VARCHAR(50) NOT NULL,
            payment             VARCHAR(50) NOT NULL,
            datetime_check_in   VARCHAR(50),
            datetime_check_out  VARCHAR(50),
            isOwner             boolean,
            survey_id           integer,
            suite_id            integer,
            rfid_id             VARCHAR(50),
            mac_address         VARCHAR(50),
            created_at          TIMESTAMP
            );
        """)
    except:
        print("Users table already exists. Not recreating it.")

    try:
        cursor.execute("""
            CREATE TABLE Employees (
            id          integer     AUTO_INCREMENT PRIMARY KEY,
            first_name        VARCHAR(30) NOT NULL,
            last_name        VARCHAR(30) NOT NULL,
            badge_id        VARCHAR(30) NOT NULL,
            service_id  integer,
            created_at  TIMESTAMP
            );
        """)
    except:
        print("Employees table already exists. Not recreating it.")

    try:
        cursor.execute("""
            CREATE TABLE LocationLogs (
            id              integer     AUTO_INCREMENT PRIMARY KEY,
            location_log    VARCHAR(50) NOT NULL,
            mac_address     VARCHAR(50) NOT NULL,
            created_at  TIMESTAMP
            );
        """)
    except:
        print("LocationLog table already exists. Not recreating it.")

    try:
        cursor.execute("""
            CREATE TABLE Transactions (
            id          integer     AUTO_INCREMENT PRIMARY KEY,
            timestamp   VARCHAR(50) NOT NULL,
            product_id  integer     NOT NULL,
            rfid_id     varchar(50) NOT NULL,
            created_at  TIMESTAMP
            );
        """)
    except:
        print("Transactions table already exists. Not recreating it.")

    try:
        cursor.execute("""
            CREATE TABLE Surveys (
            id              integer     AUTO_INCREMENT PRIMARY KEY,
            favorite_food   VARCHAR(50) NOT NULL,
            favorite_drink  VARCHAR(50) NOT NULL,
            created_at      TIMESTAMP
            );
        """)
    except:
        print("Surveys table already exists. Not recreating it.")

    try:
        cursor.execute("""
            CREATE TABLE Products (
            id          integer     AUTO_INCREMENT PRIMARY KEY,
            name        VARCHAR(50) NOT NULL,
            price       double      NOT NULL,
            service_id  integer     NOT NULL,
            created_at  TIMESTAMP
            );
        """)
    except:
        print("Products table already exists. Not recreating it.")