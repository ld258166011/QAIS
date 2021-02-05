
AUTOMATION_PARAMS = {
#    Website                Domain Name          Search Box                    Click
    'google':    {'base': ['www.google.com',    '//*[@name="q"]',              False]},
    'tmall':     {'base': ['www.tmall.com',     '//*[@title="请输入搜索文字"]', False]},
    'facebook':  {'base': ['www.facebook.com',  '//*[@type="search"]',         True], 'login': ['USERNAME', 'PASSWORD']},
    'baidu':     {'base': ['www.baidu.com',     '//*[@id="kw"]',               False]},
    'yahoo':     {'base': ['www.yahoo.com',     '//*[@name="p"]',              False]},
    'wikipedia': {'base': ['www.wikipedia.org', '//*[@name="search"]',         False]},
    'csdn':      {'base': ['www.csdn.net',      '//*[@id="toolber-keyword"]',  True]},
    'twitch':    {'base': ['www.twitch.tv',     '//*[@type="search"]',         True], 'pause': '//*[@data-a-player-state="playing"]'},
    'bing':      {'base': ['www.bing.com',      '//*[@name="q"]',              False]}
}

class Website:
    '''
    Website parameters.
    '''
    website = ''

    def __init__(self, website):
        self.website = website.lower()
        if self.website not in AUTOMATION_PARAMS:
            raise Exception('Website not supported')
        
        params = AUTOMATION_PARAMS[self.website]
        # Basic params
        self.domain = params['base'][0]
        self.box = params['base'][1]
        self.click = params['base'][2]

        # Special params
        if 'login' in params:
            self.user = params['login'][0]
            self.password = params['login'][1]
        if 'pause' in params:
            self.pause = params['pause']

