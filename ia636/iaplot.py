# -*- encoding: utf-8 -*-
# Module iaplot

def iaplot(Ylist, Xlist = [], arrows_list = [],text_list = [], ylabel='y', xlabel='x', title='',colors = 'rgbmycrgbm',shapes = '----------', axis = 'tight'):
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import ia636

    if isinstance(Ylist, np.ndarray):
        Ylist = [Ylist]
    if  Xlist == []:
       Xlist = [np.arange(len(i)) for i in Ylist]
    if isinstance(Xlist, np.ndarray):
        Xlist = [Xlist]

    fig = plt.figure()
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    for x,y, c,s in zip(Xlist, Ylist,colors[:len(Xlist)],shapes[:len(Xlist)]):
        plt.plot(x,y, c+s,markersize=9)

    for arrow in arrows_list:
        plt.arrow(arrow[0], arrow[1], arrow[2], arrow[3], fc="k", ec="k", head_width=0.15, head_length=0.2 )

    for text in text_list:
        plt.annotate(text[0],xy=(text[1], text[2]), xycoords='data',xytext=(text[1], text[2]), textcoords='data',)
    plt.grid()
    plt.axis(axis)
    return ia636.iafig2img(fig)

