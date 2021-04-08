
try:
    from websites import Website
    from automator import Automator
    from sniffer import Sniffer
except:
    from .websites import Website
    from .automator import Automator
    from .sniffer import Sniffer


def QAIS(website, query, chinese, bigrams, browser, click, iface, fname):
    '''
    Query Automation in Incremental Search.
    '''
    # Get website params
    website = Website(website)

    # Create automator
    auto = Automator(query, chinese, bigrams)

    # Create sniffer
    sniffer = Sniffer()

    # Start capture process
    sniffer.start(iface, fname)

    # Open browser
    auto.open_browser(browser)

    # Get website
    auto.get_website('https://%s' % website.domain)

    # Login if needed
    if hasattr(website, 'user'):
        if chinese:
            auto.switch_ime()
        auto.user_login(website.user, website.password)
    
    # Pause vedio if needed
    if hasattr(website, 'pause'):
        exists = auto.wait_element(website.pause)
        if exists:
            auto.click_once(website.pause)
    
    # Wait until the search box is ready
    exists = auto.wait_element(website.box)

    # Click once on the search box (or search icon)
    if click or website.click:
        if exists:
            auto.click_once(website.box)
        # Switch IME for Chinese
        if hasattr(website, 'user') and chinese:
            auto.switch_ime()
    
    # Type query in the search box
    auto.type_query()
    
    # Close browser
    auto.close_browser()

    # Stop capture process
    sniffer.stop(iface)
