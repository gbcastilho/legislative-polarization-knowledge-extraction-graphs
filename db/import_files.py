import os
import httpx
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

output_path = os.getenv("LEGISLATIVE_FILES_OUTPUT_PATH")
assert (
    output_path is not None
), "Variable 'LEGISLATIVE_FILES_OUTPUT_PATH' must be defined"

years_list = os.getenv("IMPORTING_YEARS")
assert years_list is not None, "Variable 'IMPORTING_YEARS' must be defined"

years = years_list.split(",")

# Initialize path manager
p = Path(f"./{output_path}")

CHAMBER_FILES_URL = "https://dadosabertos.camara.leg.br/arquivos"


def download_data_and_write_file(download_url: str, output_file_path: Path):
    with output_file_path.open("wb") as f:
        with httpx.stream("GET", download_url) as r:
            for data in r.iter_bytes():
                f.write(data)


def import_deputies_data():
    print("Importando dados dos deputados...")

    deputies = "deputados"

    deputies_file = p / f"{deputies}.csv"
    download_url = f"{CHAMBER_FILES_URL}/{deputies}/csv/{deputies}.csv"

    download_data_and_write_file(
        download_url=download_url,
        output_file_path=deputies_file,
    )

    print("Dados dos deputados importados!")


def import_theme_propositions_data():
    print("Importando dados dos temas das proposições...")

    theme_propositions = "proposicoesTemas"

    for year in years:
        theme_propositions_file = p / f"{theme_propositions}-{year}.csv"
        download_url = f"{CHAMBER_FILES_URL}/{theme_propositions}/csv/{theme_propositions}-{year}.csv"

        download_data_and_write_file(
            download_url=download_url,
            output_file_path=theme_propositions_file,
        )

    print("Dados dos temas das proposições importados!")


def import_deputies_votes_data():
    print("Importando dados das votações dos deputados...")

    deputies_votes = "votacoesVotos"

    for year in years:
        deputies_votes_file = p / f"{deputies_votes}-{year}.csv"
        download_url = (
            f"{CHAMBER_FILES_URL}/{deputies_votes}/csv/{deputies_votes}-{year}.csv"
        )

        download_data_and_write_file(
            download_url=download_url,
            output_file_path=deputies_votes_file,
        )

    print("Dados das votações dos deputados importados!")


def import_object_polls_data():
    print("Importando dados dos objetos das votações...")

    object_polls = "votacoesObjetos"

    for year in years:
        object_polls_file = p / f"{object_polls}-{year}.csv"
        download_url = (
            f"{CHAMBER_FILES_URL}/{object_polls}/csv/{object_polls}-{year}.csv"
        )

        download_data_and_write_file(
            download_url=download_url,
            output_file_path=object_polls_file,
        )

    print("Dados dos objetos das votações importados!")


def main():
    import_deputies_data()
    import_theme_propositions_data()
    import_deputies_votes_data()
    import_object_polls_data()


if __name__ == "__main__":
    main()
