# python3-wappalyzer
=================

Python driver for [Wappalyzer][], a web application
detection utility.

    >>> from Wappalyzer import Wappalyzer, WebPage
    >>> wappalyzer = Wappalyzer.latest()
    >>> webpage = WebPage.new_from_url('http://example.com')
    >>> wappalyzer.analyze(webpage)
    set([u'EdgeCast'])
or 

    >>> from Wappalyzer import Wappalyzer, WebPage
    >>> wappalyzer = Wappalyzer.latest()
    >>> webpage = WebPage.new_from_response(response) #here you can provide a requests response object
    >>> apps = wappalyzer.analyze(webpage) 
     set([u'EdgeCast'])
[Wappalyzer]: http://wappalyzer.com/
