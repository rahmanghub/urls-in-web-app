try:
    from bs4 import BeautifulSoup
    import requests
    import re
    from tabulate import tabulate
    import pyfiglet
except:
    print('Install all the requirements')
else:
    try:
        nme = [['Abdul Rahman M - https://www.linkedin.com/in/abdul-rahman-m-660158206/']]
        print(tabulate([[pyfiglet.figlet_format("URLs-IN-WEB")],*nme], tablefmt='grid',stralign='center'))
    except:
        print('URLs-IN-WEB')
    try:
        url = input("Enter the URL: ")
    except:
        print("You cant't proceed without url")
    else:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        try:
            req = requests.get(url,headers=headers)
        except:
            print('Enter valid url')
        else:
            try:
                soup = BeautifulSoup(req.text, "lxml")
                url_pattern = r"https?://\S+|ftp://\S+"
                for link in soup.find_all('a'):
                    url = str(link.get('href'))
                    if re.match(url_pattern, url):
                        print(f"URL: {url}")
            except:
                print('Unexpected Error Occured')
