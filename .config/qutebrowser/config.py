config.load_autoconfig(False)
config.source('nord-qutebrowser.py')    # NORD colours
# config.bind('d','scroll-page 0 0.5')

# a fix for https://github.com/qutebrowser/qutebrowser/issues/5634
c.qt.workarounds.remove_service_workers = True

c.auto_save.session = True              # this or `:wq`|`:quit --save`
c.content.blocking.method = 'auto'      # auto|adblock|hosts|both
c.tabs.position = 'right'               # bottom|left|right|top
c.tabs.show = 'never'                   # always|never|multiple|switching
c.tabs.show_switching_delay = 2000      # ms

c.input.insert_mode.auto_load = True        # enter editable element after loading the page
c.input.insert_mode.leave_on_load = True    # leave when starting a new page load

c.zoom.default = '115%' # because of 4k monitor

c.url.searchengines = {
        'DEFAULT': 'https://duckduckgo.com/?q={}',
        'g': 'https://google.com/search?q={}',
        'tb': 'https://s.taobao.com/search?q={}',
        'so': 'https://stackoverflow.com/search?q={}',
        'wa': 'https://wiki.archlinux.org/?search={}',
        'aur': 'https://aur.archlinux.org/packages/?O=0&SeB=nd&K={}&outdated=&SB=p&SO=d&PP=50&do_Search=Go'
        }

# open url in firefox
c.aliases = {'ffo': 'spawn firefox -url {url}'}
config.bind(',ffo', 'spawn firefox -url {url}', mode='normal')

# open url in mpv for video playing
c.aliases = {'mpv': 'spawn mpv {url}'}
config.bind(',mpv', 'spawn mpv {url}', mode='normal')

# Minimise fingerprint
c.content.headers.user_agent = 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}'
c.content.headers.accept_language = 'en-GB,en;q=0.5'
c.content.headers.custom = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
