import pip._internal
import bs4
import xpath
if __name__ == '__main__':
    print(pip._internal.pep425tags.get_supported())
    soup = bs4.BeautifulSoup('<p>Hello</p>','lxml')
    print(soup.p.string)