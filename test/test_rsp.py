#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2024-09-27
# @Author  : Zhaoze Wang
# @Site    : https://github.com/Wangzhaoze/PyRadar
# @File    : test_rsp.py
# @IDE     : vscode

import unittest
import numpy as np
from scipy.fft import fft
from pyradar.rsp import range_fft  # Update this import based on your actual module name

class TestRangeFFT(unittest.TestCase):

    def test_range_fft_valid_input(self):
        """
        Test case for performing FFT with a valid 3D numpy array input.
        """
        adc_cube = np.random.rand(2, 4, 8)  # Example dimensions: [antennas, chirps, samples]
        fft_result = range_fft(adc_cube)

        # Manually calculate the expected result using scipy's fft
        expected_result = fft(adc_cube, axis=2)

        # Check if the function output matches the expected result
        np.testing.assert_array_almost_equal(fft_result, expected_result, decimal=6, 
                                             err_msg="The FFT result does not match the expected output")

        # Verify the output shape
        self.assertEqual(fft_result.shape, adc_cube.shape, 
                         "The output shape of the FFT is incorrect")

    def test_range_fft_invalid_type(self):
        """
        Test case to check if ValueError is raised when input is not a numpy array.
        """
        with self.assertRaises(ValueError) as context:
            range_fft([[1, 2], [3, 4]])  # Passing a list instead of a numpy array
        
        self.assertEqual(str(context.exception), "Input must be a numpy array.")

    def test_range_fft_invalid_dimension(self):
        """
        Test case to check if ValueError is raised when input does not have three dimensions.
        """
        invalid_shapes = [
            np.random.rand(4, 5),          # 2D array
            np.random.rand(2, 3, 4, 5),    # 4D array
            np.random.rand(2),              # 1D array
        ]

        for invalid_input in invalid_shapes:
            with self.assertRaises(ValueError) as context:
                range_fft(invalid_input)
            self.assertEqual(str(context.exception), "Input array must have exactly three dimensions.")

if __name__ == '__main__':
    unittest.main()
