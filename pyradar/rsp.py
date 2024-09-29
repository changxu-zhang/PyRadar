#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024-09-27
# @Author  : Zhaoze Wang
# @Author  : Changxu Zhang
# @Site    : https://github.com/Wangzhaoze/PyRadar
# @File    : rsp.py
# @IDE     : vscode

"""Radar Signal Processing."""

import numpy as np
from scipy import fft

def range_fft(adc_cube) -> np.ndarray:
    """
    Perform a Fast Fourier Transform (FFT) along the range dimension of the input ADC cube.

    Args:
        adc_cube (np.ndarray): A 3D numpy array representing the ADC (Analog-to-Digital Converter) data.
                          The data dimensions are typically organized as [antennas, chirps, samples].

    Returns:
        np.ndarray: The transformed data after performing FFT along the range dimension (3rd axis).
                The output will be of the same shape as the input, with the range dimension transformed into the frequency domain.

    Raises:
        ValueError: If the input is not a numpy array or if it does not have exactly three dimensions.
    """
    # Check if input is a numpy array
    if not isinstance(adc_cube, np.ndarray):
        raise ValueError('Input must be a numpy array.')

    # Check if the input array has three dimensions
    if adc_cube.ndim != 3:
        raise ValueError('Input array must have exactly three dimensions.')

    # Perform FFT along the third axis (range dimension)
    return fft.fft(adc_cube, axis=2)
