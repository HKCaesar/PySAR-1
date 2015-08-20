"""
Signal (:mod:`pysar.signal`)
============================

1D and 2D signal processing routines

.. currentmodule:: pysar.signal

Functions
---------

Boxcar filters (:mod:`pysar.signal.boxfilter`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :toctree: generated/

   boxcar1d          1D filter
   boxcar2d          2D filter

Median filters (:mod:`pysar.signal.medfilter`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :toctree: generated/

   medfilt2d         2D median filter

Butterworth filters (:mod:`pysar.signal.butters`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :toctree: generated/

   butter            General Butterworth filter
   bandpass          Bandpass Butterworth filter
   lowpass           Lowpass Butterworth filter
   highpass          Highpass Butterworth filter   

Specialty filters (:mod:`pysar.signal.special`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autosummary::
   :toctree: generated/

   taper             1D cosine taper
   conefilter2d      2D cone-shaped filter 

Scripts
-------

None
"""

import sys,os
import numpy as np

import boxfilter
import medfilter
import butters
import special
 
__all__ = ['boxfilter','medfilter','butters','special']

from boxfilter import *
from medfilter import *
from butters import *
from special import *   
