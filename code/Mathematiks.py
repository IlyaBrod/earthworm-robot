# Copyright (c) 2025 I. Brodoline, University of Twente. See LICENSE file for details.

import numpy as np
from typing import Any, List, Tuple

def fx_cone(x: float,L: float,D: float):
    y = x*D/2/L
    return y

def fx_VonKaraman(x: float,L: float,D: float):
    theta = np.arccos(1-2*x / L)
    y = D/(2*np.sqrt(np.pi)) * np.sqrt(theta - np.sin(2*theta)/2)
    return y


def frustrumIntegral(_function,x_values) -> float:
    """Calculate the surface integral of a frustrum object defined by a function.

    Args:
        _function (Any): function returning the radius of the shape for a given x value
        x_values (Vector): vector of x values to take account in the calculation

    Returns:
        float: frustrum integral
    """
    surface_integral = 0
    #S2 = 0
    #deriv = np.gradient(_function(x_values),x_values)
    for x in range(1,len(x_values)):
        r1 = (_function(x_values[x]))
        r2 = (_function(x_values[x-1]))
        segment = np.sqrt((r1-r2)**2 + (x_values[x]-x_values[x-1])**2)
        surface_integral += np.pi * segment * (r1 + r2)
        #S2 += 2*np.pi * r1 * np.sqrt(1 + deriv[x]**2) * (x_values[x]-x_values[x-1])
    
    return surface_integral

def frustrumAngle(_function,x_values) -> float:
    """Calculate the angle for a frustrum array

    Args:
        frustrum radius function (_Any_): Profile of the frustrum radius
        x_values (_vector_): positions array [x0 x1]

    Returns:
        float: array of angles or single value. Angle>0 for increase of radius,
        0 for cosntant radius, and <0 for decrease in radius
    """
    anglesList = []
    for i in range(1,len(x_values)):
        r0 = (_function(x_values[i-1]))
        r1 = (_function(x_values[i]))
        anglesList.append(np.arctan2(r1-r0 , x_values[1] - x_values[0]))
    if(len(x_values)==2):
        return anglesList[0]
    else:
        return anglesList

def rotationMatrix_xy(theta) ->  np.matrix:
    """Generate rotation matrix in the xy plane

    Args:
        theta (float): Angle in rads

    Returns:
        float: return the 
    """

    c, s = np.cos(theta), np.sin(theta)
    return np.matrix([[c, -s],[s, c]])


#Example frustrumAngle
#vec = [10,20]
#print(frustrumAngle(lambda x: vec[x],[0, 1]))


def bar_add_annotation(ax, x_pair, height,pvalue,**kwargs):
    r"""
        Annotate bar plot with singificance code.

        The significance codes are defined by the pvalue, and a line is drawn
        between the pair of bars at a specific height.

        Significance code         p-value
            ***                 [0, 0.001]
             **              (0.001, 0.01]
              *               (0.01, 0.05]
              .                (0.05, 0.1]
                                  (0.1, 1]  

        The annotation function works also with horizontal bars without additional modifications.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            The axis on which to draw the annotation.

        x_pair : float or array-like
            The x coordinates of the bars.

            Bars are often used for categorical data, i.e. string labels below
            the bars. You can provide a list of strings directly to *x*.
            ``bar_add_annotation(['A', 'B'], 3, 0.0256)``

        height : float
            The height(s) of the bars.

            Note that if *bottom* has units (e.g. datetime), *height* should be in
            units that are a difference from the value of *bottom* (e.g. timedelta).

        pvalue: float
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

        dh: float
            Height offset for the text over bar
            Default: 0.05

        fontsize: int, optional
            Font size for the label
        
        barh: float
            Bar height in axes coordinates (0 to 1)
            Default: 0.05

        color: :mpltype:`color` or list of :mpltype:`color`, optional
            Font and Lines color.

        linewidth : float or array-like, optional
            Width of the bar edge(s). If 0, don't draw lines.
        
        fontfamily: str
            {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}
    
    """
    
    barh = kwargs.pop("barh",0.05)
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
    lx, ly = x_pair[0], height
    rx, ry = x_pair[1], height

    ax_y0, ax_y1 = ax.get_ylim()
    dh *= (ax_y1 - ax_y0)
    barh *= (ax_y1 - ax_y0)

    y = max(ly, ry) + dh

    barx = [lx, lx, rx, rx]
    bary = [y, y+barh, y+barh, y]
    mid = ((lx+rx)/2, y+barh)

    ax.plot(barx, bary, c = color,linewidth = linewidth, alpha = alpha)

    kwargs2 = dict(ha='center', va='bottom')
    kwargs2['size'] = fontsize
    kwargs2['color'] = color
    kwargs2['fontfamily'] = fontfamily
    kwargs2['alpha'] = alpha

    ax.text(*mid, text, **kwargs2)