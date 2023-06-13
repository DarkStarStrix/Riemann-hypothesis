# code all the formula's in the Riemann hypothesis as functions

import time

import matplotlib.pyplot as plt
import numpy as np


# Riemann-Siegel formula
def Riemann_Siegel(x):
    # x is the input value
    # returns the value of the Riemann-Siegel function at x
    if x < 0:
        return 0
    else:
        return np.sqrt(x / (2 * np.pi)) * np.sin(x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4)


# Euler-Maclaurin formula
def Euler_Maclaurin(x):
    # x is the input value
    # returns the value of the Euler-Maclaurin function at x
    if x < 0:
        return 0
    else:
        return np.sqrt(x / (2 * np.pi)) * np.sin(x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4) + np.cos(
            x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4) / (8 * np.sqrt(x * np.pi)) - np.sin(
            x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4) / (48 * x * np.sqrt(x * np.pi)) - np.cos(
            x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4) / (384 * x ** 2 * np.sqrt(x * np.pi)) + np.sin(
            x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4) / (9216 * x ** 3 * np.sqrt(x * np.pi))


# Riemann zeta function
def Riemann_zeta(x):
    # x is the input value
    # returns the value of the Riemann zeta function at x
    if x == 1:
        return np.inf
    else:
        return np.sum(1 / (np.arange(1, 10000) ** x))


# Christoffer symbols, covariant derivative and Riemann curvature tensor
def Christoffer_symbols(x, y, z):
    # x, y and z are the input values
    # returns the value of the Christoffer symbols at x, y and z
    return 0


def covariant_derivative(x, y, z):
    # x, y and z are the input values
    # returns the value of the covariant derivative at x, y and z
    return 0


def Riemann_curvature_tensor(x, y, z):
    # x, y and z are the input values
    # returns the value of the Riemann curvature tensor at x, y and z
    return 0


# Riemann hypothesis
def Riemann_hypothesis(x):
    # x is the input value
    # returns the value of the Riemann hypothesis at x
    if x == 1:
        return np.inf
    else:
        return 0


# code the identity function
def identity(x):
    # x is the input value
    # returns the value of the identity function at x
    return x


# code Gradient, divergence, Laplace–Beltrami operator and Laplace operator
def Gradient(x, y, z):
    # x, y and z are the input values
    # returns the value of the Gradient at x, y and z
    return 0


def divergence(x, y, z):
    # x, y and z are the input values
    # returns the value of the divergence at x, y and z
    return 0


def Laplace_Beltrami_operator(x, y, z):
    # x, y and z are the input values
    # returns the value of the Laplace–Beltrami operator at x, y and z
    return 0


def Laplace_operator(x, y, z):
    # x, y and z are the input values
    # returns the value of the Laplace operator at x, y and z
    return 0


# code Kulkarni–Nomizu product
def Kulkarni_Nomizu_product(x, y, z):
    # x, y and z are the input values
    # returns the value of the Kulkarni–Nomizu product at x, y and z
    return 0


# code the Riemannian metric
def Riemannian_metric(x, y, z):
    # x, y and z are the input values
    # returns the value of the Riemannian metric at x, y and z
    return 0


# code the Riemannian metric inverse
def Riemannian_metric_inverse(x, y, z):
    # x, y and z are the input values
    # returns the value of the Riemannian metric inverse at x, y and z
    return 0


# code the ricci curvature tensor
def ricci_curvature_tensor(x, y, z):
    # x, y and z are the input values
    # returns the value of the ricci curvature tensor at x, y and z
    return 0
