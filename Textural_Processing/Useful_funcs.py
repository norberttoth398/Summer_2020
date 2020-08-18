#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:42:01 2020

@author: norbert
"""


def split_at(string, char, n):
    """
    Splits string into two at the nth occurence of the character specified.
    
    Input
    ------------------------------------
    string - string to be split into two
    char - character to split at
    n - the occurrence of character at which splitting should occur.
    
    Returns
    -------------------------------------
    The two ends of the string split at the specified position.
    """
    words = string.split(char)
    return char.join(words[:n]), char.join(words[n:])

def best_fit(X, Y):
    """
    Computes line of best fit for the data passed to it.
    
    Inputs
    --------------------------------------------
    X,Y - the list of coordinates of data points in cartesian space.
    
    Returns
    ---------------------------------------------
    a,b - coefficients of equation of the form y=a*x+b.
    """

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = float(sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar)
    denum = float(sum([xi**2 for xi in X]) - n * xbar**2)

    a = numer / denum
    b = ybar - a * xbar


    return a, b, fit
