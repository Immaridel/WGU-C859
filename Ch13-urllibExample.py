import urllib.request


def search(terms):
    """Do a fictional web engine search and return the results"""
    html = _send_request(terms)
    results = _get_results(html)
    return results


def _send_request(terms):
    """Send search to fictional web search engine and receive HTML response"""
    terms = terms.replace(' ', '%20')  # replace spaces

    url = 'http://www.search.fake.zybooks.com/search?q=' + terms
    info = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=info)

    response = urllib.request.urlopen(req)
    html = str(response.read())
    return html


def _get_results(html):
    """
    Finds the links returned in 1st page of results.
    """
    start_tag = '<cite>'  # start of results
    end_tag = '</cite>'  # Results end with this tag
    links = []  # list of result links

    start_tag_loc = html.find(start_tag)  # find 1st link

    while start_tag_loc > -1:
        link_start = start_tag_loc + len(start_tag)
        link_end = html.find(end_tag, link_start)
        links.append(html[link_start:link_end])
        start_tag_loc = html.find(start_tag, link_end)

    return links

if __name__ == "__main__":

    search_term = input('Enter search terms: ')
    result = search(search_term)

    print('Found {} links:'.format(len(result)))
    for link in result:
        print(' ', link)