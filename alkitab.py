auth = "Code by Bagasekaapr"

def load_data_list(file_path):
    with open(file_path, "r") as file:
        for_data = json.load(file)
    return for_data["tb"]

def get_url_for_kitab(data_name, data_list):
    return data_list.get(data_name)

def main():
    print(Panel(nx));print(xn)
    data_list = load_data_list("DATA/Kitab.json")
    questions = [
        inquirer.List("pilih", message="Pilih Kitab".title(), choices=list(data_list.keys()), carousel=True)
    ]
    answers = inquirer.prompt(questions, theme=BlueComposure())
    selected_data_url = get_url_for_kitab(answers["pilih"], data_list)
    if selected_data_url:
        bagian(selected_data_url)
    else:
        exit()

def bagian(kitab_name):
    data_list = load_data_list(f"DATA/{kitab_name}.json")
    questions = [
        inquirer.List("pilih", message=f"Pilih Bagian".title(), choices=list(data_list.keys()), carousel=True)
    ]
    answers = inquirer.prompt(questions, theme=BlueComposure())
    selected_data_url = get_url_for_kitab(answers["pilih"], data_list)
    clear();baca(kitab_name, selected_data_url)

def baca(kitab, angka):
    table = Table(show_header=True, header_style="white")
    table.add_column("Ayat", justify="center")
    table.add_column("Isi")
    url = f'https://alkitab.me/in-tb/{kitab}/{angka}'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
    try:
        req = requests.get(url, headers=headers)
        req.raise_for_status()
        soup = sop(req.text, 'html.parser')
        items = soup.find('div', id='the-content')
        judul = items.find('h1').text
        centered_judul = judul.center(console.width)
        print(Panel(centered_judul))
        verses = items.find_all('div', {'data-verse': True})
        for v in verses:
            try:
                ayat = v.find('span', {'class': 'vn'}).text
            except:
                ayat = ""
            try:
                isi_paragraphs = v.find_all("p")
                isi = "\n".join([p.text for p in isi_paragraphs])
            except:
                isi = ""
            table.add_row(f"{ayat}", f"{isi}\n")
        console.print(table)
        choice()
    except requests.exceptions.RequestException as e:
        print("Tidak dapat terhubung ke server:", e)

def choice():
    forward = input("Baca Kitab lainnya? [y/t]: ")
    if forward in ["Ya", "Y", "y"]:
        clear();main()
    elif forward in ["Tidak", "T", "t"]:
        exit()
    else:
        print("Pilih yang benar.\n")
        choice()

def clear():
    if "linux" in sys.platform.lower():os.system('clear')
    elif "win" in sys.platform.lower():os.system('cls')

try:
    import requests, json, inquirer, os, sys
    from rich import print
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from inquirer.themes import BlueComposure
    from bs4 import BeautifulSoup as sop
    console = Console()
    table = Table()
    welcome = "Alkitab Perjanjian Baru scrap from: [blue]alkitab.me[/]"
    nx = welcome.center(console.width)
    xn = auth.center(console.width)
    if __name__ == "__main__":
        clear()
        main()
except ModuleNotFoundError as e:
    with open('log.json', 'w') as f:
        f.write("Error: " + str(e))
except Exception as e:
    with open('log.json', 'w') as f:
        f.write("Error: " + str(e))
