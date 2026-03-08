import psycopg2

def load_csv_to_db(csv_path: str, table_name: str, conn_params: dict):
    """
    Load CSV data into warehouse table.
    """
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()
    # TODO: implement COPY or INSERT logic
    conn.commit()
    cur.close()
    conn.close()
