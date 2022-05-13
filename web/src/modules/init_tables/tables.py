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
            datetime_start      VARCHAR(30) NOT NULL,
            datetime_end        VARCHAR(50) NOT NULL,
            location            VARCHAR(50) NOT NULL,
            category            VARCHAR(50) NOT NULL,
            transaction_total   double      NOT NULL default 0.0,
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
            address         VARCHAR(50) NOT NULL,
            city            VARCHAR(50) NOT NULL,
            state           VARCHAR(50) NOT NULL,
            country         VARCHAR(50) NOT NULL,
            postal_code     VARCHAR(50) NOT NULL,
            created_at      TIMESTAMP
            );
        """)
    except:
        print("Companies table already exists. Not recreating it.")

    try:
        cursor.execute("""
            CREATE TABLE Suites (
            id                  integer AUTO_INCREMENT PRIMARY KEY,
            number_active       integer NOT NULL,
            transaction_total   double  NOT NULL,
            event_id            integer NOT NULL,
            user_id             integer NOT NULL,
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
            transaction_total   double NOT NULL,
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
            transaction_total   VARCHAR(50) NOT NULL,
            datetime_check_in   VARCHAR(50) NOT NULL,
            datetime_check_out  VARCHAR(50) NOT NULL,
            isOwner             boolean     NOT NULL,
            survey_id           integer     NOT NULL,
            suite_id            integer     NOT NULL,
            created_at          TIMESTAMP
            );
        """)
    except:
        print("Users table already exists. Not recreating it.")

    try:
        cursor.execute("""
            CREATE TABLE Employees (
            id          integer     AUTO_INCREMENT PRIMARY KEY,
            service_id  integer     NOT NULL,
            name        VARCHAR(30) NOT NULL,
            created_at  TIMESTAMP
            );
        """)
    except:
        print("Employees table already exists. Not recreating it.")

    try:
        cursor.execute("""
            CREATE TABLE RFIDLog (
            id          integer AUTO_INCREMENT PRIMARY KEY,
            user_id     integer NOT NULL,
            created_at  TIMESTAMP
            );
        """)
    except:
        print("RFIDLog table already exists. Not recreating it.")

    try:
        cursor.execute("""
            CREATE TABLE LocationLogs (
            id              integer     AUTO_INCREMENT PRIMARY KEY,
            location_log    VARCHAR(30) NOT NULL,
            rfid_id         integer     NOT NULL,
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
            user_id     integer     NOT NULL,
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