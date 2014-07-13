'''
Created on Jun 19, 2014

@author: Milind
'''
def get_page(url):
    try: 
        import urllib.request
        return str(urllib.request.urlopen(url).read())
#         resource = urllib.request.urlopen(url)
#         content =  resource.read().decode(resource.headers.get_content_charset())
#         return content
        
    except:
        return "Error"

# print (get_page("http://www.yahoo.com"))

