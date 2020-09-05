from ..site_base import SiteBase
from ..gazelle import Gazelle

# auto_sign_in

URL = 'https://dicmusic.club/'
SUCCEED_REGEX = '积分 \\(.*?\\)'


# iyuu_auto_reseed
# dicmusic:
#   authkey: ‘{ authkey }’
#   torrent_pass: '{ torrent_pass }'

class MainClass(Gazelle):
    @staticmethod
    def build_sign_in(entry, config):
        SiteBase.build_sign_in_entry(entry, config, URL, SUCCEED_REGEX)

    @staticmethod
    def build_reseed_entry(entry, base_url, site, passkey, torrent_id):
        download_page = site['download_page'].format(torrent_id=torrent_id,
                                                     authkey=passkey['authkey'],
                                                     torrent_pass=passkey['torrent_pass'])
        entry['url'] = 'https://{}/{}'.format(base_url, download_page)

    def build_selector(self):
        selector = super(MainClass, self).build_selector()
        selector['details_content']['details_bar'] = None
        selector['details']['seeding'] = None
        selector['details']['leeching'] = None
        return selector
