'''
Created on May 24, 2014

@author: Milind
'''
# The crawl_web procedure to take a second parameter,
# max_depth, that limits the depth of the search.  We can 
# define the depth of a page as the number of links that must
# be followed to reach that page starting from the seed page,
# that is, the length of the shortest path from the seed to
# the page.  No pages whose depth exceeds max_depth should be
# included in the crawl.  
# 
# For example, if max_depth is 0, the only page that will
# be crawled is the seed page. If max_depth is 1, the pages
# that should be crawled are the seed page and every page that 
# it links to directly. If max_depth is 2, the crawl should 
# also include all pages that are linked to by these pages.
#
# Note that the pages in the crawl may be in any order.
#


import getpage as getpage


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page, depth):
    links = []
    myData = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            myData = [url, depth]
            links.append(myData)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed,max_depth):
    tocrawl = [[seed, 0]]
    crawled = []
    myData = []
    while tocrawl:
        myData = tocrawl.pop()
        if myData[1] < max_depth + 1:
            union(tocrawl, get_all_links(getpage.get_page(myData[0]), myData[1]+1))
            if myData[0] not in crawled:          
                crawled.append(myData[0])            
       
    return crawled

print (crawl_web("http://www.google.com",1))
# print (crawl_web("http://www.udacity.com/cs101x/index.html",1))
#>>> ['http://www.udacity.com/cs101x/index.html']

#print (crawl_web("http://www.udacity.com/cs101x/index.html",1))
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html']

# print (crawl_web("http://www.udacity.com/cs101x/index.html",50))
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html',
#>>> 'http://www.udacity.com/cs101x/kicking.html']

#print (crawl_web("http://top.contributors/forbiddenvoid.html",2))
#>>> ['http://top.contributors/forbiddenvoid.html',
#>>> 'http://top.contributors/graemeblake.html',
#>>> 'http://top.contributors/angel.html',
#>>> 'http://top.contributors/dreyescat.html',
#>>> 'http://top.contributors/johang.html',
#>>> 'http://top.contributors/charlzz.html']

# print (crawl_web("A1",3))
#>>> ['A1', 'C1', 'B1', 'E1', 'D1', 'F1']
# (May be in any order)
