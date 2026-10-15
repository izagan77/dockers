import os
import pandas as pd
import psycopg2


def export_postgres_to_csv():
    # Database configuration attributes
    db_config = {
        "host": "local-postgres",  # 'localhost' since port 5432 is mapped directly to Windows host environment
        "database": "postgres",
        "user": "postgres",
        "password": "welcome2",
        "port": "5432",
    }

    output_filename = "exported_data.csv"
    query = "SELECT product_name FROM development.products;"

    try:
        print("Connecting to local-postgres container...")
        connection = psycopg2.connect(**db_config)

        print("Executing target selection query...")
        df = pd.read_sql_query(query, connection)

        # Spool data down to filesystem target
        df.to_csv(output_filename, index=False)
        print(
            f"Successfully extracted {len(df)} records! Data dumped into '{output_filename}'."
        )

    except Exception as error:
        print(f"Extraction execution failed: {error}")

    finally:
        if "connection" in locals() and connection:
            connection.close()
            print("Database channel closed gracefully.")


if __name__ == "__main__":
    export_postgres_to_csv()