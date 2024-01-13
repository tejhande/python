import webbrowser as wb

def webauto():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    urls = ( 
        "stackoverflow",
        "gmail.com",
        "udemy.com")
    

    for url in urls:
         print("Opening:"+url)
         wb.get(chrome_path).open(url)


webauto()
    