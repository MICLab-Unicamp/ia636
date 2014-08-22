# -*- encoding: utf-8 -*-
# Module iareadurl

def iareadurl(url):
    from StringIO import StringIO
    import urllib
    import PIL
    import adpil

    file = StringIO(urllib.urlopen(url).read())
    img = PIL.Image.open(file)
    return adpil.pil2array(img)

