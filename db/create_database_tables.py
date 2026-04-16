import os
import duckdb

from dotenv import load_dotenv

load_dotenv()

data_path = os.getenv("LEGISLATIVE_FILES_OUTPUT_PATH")
assert data_path is not None, "Variable 'LEGISLATIVE_FILES_OUTPUT_PATH' must be defined"

duckdb_path = os.getenv("DUCKDB_PATH")
assert duckdb_path is not None, "Variable 'DUCKDB_PATH' must be defined"

con = duckdb.connect(duckdb_path)


def create_deputies_table():
    deputies_files_path = f"./{data_path}/deputados.csv"

    con.execute("DROP TABLE IF EXISTS deputados;")

    con.execute(
        f"CREATE TABLE deputados AS SELECT * FROM read_csv('{deputies_files_path}');"
    )

    print("Tabela 'deputados' criada!")
    con.sql("DESCRIBE deputados;").show()


def create_theme_prepositions_table():
    theme_prepositions_files_path = f"./{data_path}/proposicoesTemas*.csv"

    con.execute("DROP TABLE IF EXISTS proposicoesTemas;")

    con.execute(
        f"CREATE TABLE proposicoesTemas AS SELECT * FROM read_csv('{theme_prepositions_files_path}');"
    )

    # Converts proposicao URI into ID
    con.sql("ALTER TABLE proposicoesTemas ADD COLUMN proposicao_id BIGINT;")
    con.execute(
        "UPDATE proposicoesTemas SET proposicao_id = regexp_extract(uriProposicao, '(\\d+)$') "
    )

    print("Tabela 'proposicoesTemas' criada!")
    con.sql("DESCRIBE proposicoesTemas;").show()


def create_deputies_votes_table():
    deputies_votes_files_path = f"./{data_path}/votacoesVotos*.csv"

    con.execute("DROP TABLE IF EXISTS votacoesVotos;")

    con.execute(
        f"CREATE TABLE votacoesVotos AS SELECT * FROM read_csv('{deputies_votes_files_path}');"
    )

    print("Tabela 'votacoesVotos' criada!")
    con.sql("DESCRIBE votacoesVotos;").show()


def create_object_polls_table():
    object_polls_files_path = f"./{data_path}/votacoesObjetos*.csv"

    con.execute("DROP TABLE IF EXISTS votacoesObjetos;")

    con.execute(
        f"CREATE TABLE votacoesObjetos AS SELECT * FROM read_csv('{object_polls_files_path}');"
    )

    print("Tabela 'votacoesObjetos' criada!")
    con.sql("DESCRIBE votacoesObjetos;").show()


def main():
    create_deputies_table()
    create_theme_prepositions_table()
    create_deputies_votes_table()
    create_object_polls_table()


if __name__ == "__main__":
    main()
