from typing import Tuple

import requests
from bs4 import BeautifulSoup


def get_html(url: str) -> BeautifulSoup:
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    
    return soup


def get_lyrics(lyrics_url: str) -> Tuple[str, str]:
    """Get the lyrics information from url.
    :param lurics_url: URL of the lyrics site. 
    :return: Song name and lyrics.
    :rtype: tuple(str, str)
    """

    error_info = ("", "歌詞情報を取得できません。")

    # Determine lyric sites by URL
    # TODO: Make other lyrics sites options.
    if "uta-net.com" in lyrics_url:
        site = "uta-net"
    else:
        return error_info

    try:
        soup = get_html(url=lyrics_url)

        meta_info = soup.find("meta", attrs={"name": "keywords"})["content"]
        song_name = meta_info.split(",")[1]

        kashi = soup.find(id="kashi_area")
    except:
        return error_info

    # Replace newline code.
    for section in kashi.select("br"):
        section.replace_with("\n")

    return song_name, kashi.text
