from bs4 import BeautifulSoup


def get_info_from_html(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.findAll('p')[0].text

