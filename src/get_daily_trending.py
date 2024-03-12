import requests
import time

def fetch_trending_repos():
    """Mengambil repositori yang sedang tren."""
    url = "https://api.gitterapp.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # memastikan untuk memunculkan kesalahan jika permintaan gagal
    return response.json()

def save_as_markdown(repos):
    """Menyimpan repositori yang sedang tren sebagai file markdown."""
    today = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    with open('trending.md', 'a+', encoding='utf-8') as f:
        f.write("*********{}*********\n".format(today))
        f.write("|Nama|Stars|Deskripsi|Catatan|\n")
        f.write("|---|---|---|---|\n")
        for repo in repos:
            name = f"{repo['author']}/{repo['name']}"
            url = f"https://github.com/{name}"
            stars = f"!GitHub Repo stars"
            description = repo['description'] if repo['description'] else 'Tidak ada Deskripsi'
            f.write(f"|{name}|{stars}|{description}|-|\n")
        f.write("*********{}*********\n".format(today))

def main():
    """Fungsi utama."""
    repos = fetch_trending_repos()
    save_as_markdown(repos)

if __name__ == "__main__":
    main()
    
