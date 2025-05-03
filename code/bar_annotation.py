# Copyright (c) 2025 I. Brodoline, University of Twente. See LICENSE file for details.

import numpy as np

def bar_add_annotation(ax, x_pair, height: float,pvalue: float,**kwargs):
    r"""
        Annotate bar plot with singificance code.

        The significance codes are defined by the pvalue, and a line is drawn
        between the pair of bars at a specific height.

        Significance code         p-value
            ***                 [0, 0.001]
             **              (0.001, 0.01]
              \*               (0.01, 0.05]
                .               (0.05, 0.1]
                                  (0.1, 1]  

        The annotation function works also with horizontal bars without additional modifications.
        Just indicate two values as the height argument.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            The axis on which to draw the annotation.

        x_pair : float or array-like
            The x coordinates of the bars.

            Bars are often used for categorical data, i.e. string labels below
            the bars. You can provide a list of strings directly to *x*.
            ``bar_add_annotation(['A', 'B'], 3, 0.0256)``

        height : float or array_like
            The height of the bar. If two values are provided, horizontal bar plot is detected.

            Note that if *bottom* has units (e.g. datetime), *height* should be in
            units that are a difference from the value of *bottom* (e.g. timedelta).

        pvalue: float,
        The pvalue used to determine the significance code between the two bars.

            Significance code         p-value
            ***                 [0, 0.001]
             **              (0.001, 0.01]
              *               (0.01, 0.05]
              .                (0.05, 0.1]
                                  (0.1, 1]

        Other Parameters
        ----------------

        alpha: float
            Transparency of the plotted lines.

        dh: float (positive or negative)
            Height offset for the text over bar in axes coordinates (-1 to 1)
            Default: 0.05

        fontsize: int, optional
            Font size for the label
        
        hspace: float
            Horizontal offset in axes coordinates (0 to 1)
            Default: 0

        barh: float
            Bar height in axes coordinates (0 to 1)
            Default: 0.05
        
        barl: float
            Bar length in axes coordinates (0 to 1)
            Default: 0.05

        color: :mpltype:`color` or list of :mpltype:`color`, optional
            Font and Lines color.

        linewidth : float or array-like, optional
            Width of the bar edge(s). If 0, don't draw lines.
        
        fontfamily: str
            {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}
    
    """
    hspace = kwargs.pop("hspace",0)
    barh = kwargs.pop("barh",0.05)
    barl = kwargs.pop("barl",0.05)
    dh = kwargs.pop("dh",0.05)
    fontsize = kwargs.pop("fontsize",None)
    color = kwargs.pop("color",'black')
    linewidth = kwargs.pop("linewidth", 1.5)
    fontfamily = kwargs.pop("fontfamily",None)
    alpha = kwargs.pop("alpha",1)

    #Generating the text
    if(pvalue <= 0.001): text = "***"
    elif(pvalue <= 0.01): text = "**"
    elif(pvalue <= 0.05): text = "*"
    else: text = ""

    #Get the line coordinates
    if(np.size(height) > 1): #horizontal bars
        height.sort()
        hy, hx = height[0], x_pair
        ly, lx = height[1], x_pair

        ax_x0, ax_x1 = ax.get_xlim()
        dh *= (ax_x1 - ax_x0)
        barh *= (ax_x1 - ax_x0)
        barl *= (ax_x1 - ax_x0)
        hspace *= (ax_x1 - ax_x0)

        x = max(lx, hx) + barh

        barx = [x, x+barl, x+barl, x]
        bary = [hy-hspace, hy-hspace, ly+hspace, ly+hspace]
        text_pos = (x+barl+dh,(hy+ly)/2)

    else: #vertical bars
        x_pair.sort()
        lx, ly = x_pair[0], height
        rx, ry = x_pair[1], height

        ax_y0, ax_y1 = ax.get_ylim()
        dh *= (ax_y1 - ax_y0)
        barh *= (ax_y1 - ax_y0)
        barl *= (ax_y1 - ax_y0)
        hspace *= (ax_y1 - ax_y0)

        y = max(ly, ry) + barh

        barx = [lx+hspace, lx+hspace, rx-hspace, rx-hspace]
        bary = [y, y+barl, y+barl, y]
        text_pos = ((lx+rx)/2, y+barl+dh)

    ax.plot(barx, bary, c = color,linewidth = linewidth, alpha = alpha)

    kwargs2 = dict(ha='center', va='center_baseline')
    kwargs2['size'] = fontsize
    kwargs2['color'] = color
    kwargs2['fontfamily'] = fontfamily
    kwargs2['alpha'] = alpha

    ax.text(*text_pos, text, **kwargs2)