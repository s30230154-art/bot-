import psycopg2


class Connection:
    def _get_connection(self):
        try:
            return psycopg2.connect(
                database="A2_P26_DB",
                user="neang",
                password="123",
                host="localhost",
                port="5432"
            )
        except Exception as ex:
            print(f"Connection error: {ex}")
            return None
