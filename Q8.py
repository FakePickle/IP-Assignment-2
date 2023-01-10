def text_extracter():
    urls = []
    importance_url = []
    url_text = []
    with open("/home/fakepickle/Downloads/Python programs/College/IP Assignment 2/pages.txt",'r') as urls_file:
        for line in urls_file:
            url_and_importance,url = line.split(': ')
            main_url,init_importance = url_and_importance.split(', ')
            urls.append(main_url)
            importance_url.append(init_importance)
            url_text.append(url)
    return urls,importance_url,url_text

def url_extracter(urls,url_text):
    url_extracted = []
    for i in url_text:
        url = []
        for j in urls:
            if j in i:
                url.append(j)
        url_extracted.append(url)
    return url_extracted

def dictionary_making(urls,importance_url,url_extracted):
    x = len(urls)
    page_dict = {}
    for i in range(x):
        page_dict[urls[i]] = {
            'Init Importance': float(importance_url[i]),
            'Importance': 0.0,
            'Url': url_extracted[i]
        }
    return page_dict

def calculate_importance(pages_dict):
    for main_url,url_data in pages_dict.items():
        for url in url_data['Url']:
            pages_dict[url]['Importance'] += url_data['Init Importance']/len(url_data['Url'])

def sorting_dictionary(pages_dict):
    sorted_dictionary = sorted(pages_dict.items(), key=lambda x: x[1]['Importance'], reverse=True)
    return sorted_dictionary

def top_pages(sorted_dictionary):
    N = 10
    for url,url_data in sorted_dictionary[:N]:
        print(url+': '+str(url_data['Importance']))

if __name__ == "__main__":
    urls,init_importance,url_text = text_extracter()
    extracted_url = url_extracter(urls,url_text)
    page_dict = dictionary_making(urls,init_importance,extracted_url)
    calculate_importance(page_dict)
    sorted_dictionary = sorting_dictionary(page_dict)
    top_pages(sorted_dictionary)