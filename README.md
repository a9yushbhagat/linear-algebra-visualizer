# Linear Algebra Visualizer

A Python project that visualizes how 2D linear transformations affect vectors and shapes while also calculating important matrix properties such as determinant, trace, eigenvalues, and eigenvectors.

## Project Overview

The project uses a 2x2 matrix to transform vectors in two-dimensional space.

It begins with a unit square and applies a linear transformation to each of its vertices. The transformed square is then plotted together with the original square so the effect of the matrix can be seen visually.

The program also calculates the matrix's eigenvalues and eigenvectors and displays the eigenvector directions on the graph.

## Features

- Represents 2D vectors and 2x2 matrices
- Performs matrix-vector multiplication
- Transforms the unit square
- Calculates matrix trace
- Calculates determinant
- Computes real eigenvalues
- Computes corresponding eigenvectors
- Visualizes the original and transformed square
- Displays eigenvector directions

## Main File

- `linear_transform_visualizer.py` — contains the matrix calculations, vector transformations, eigenvalue/eigenvector calculations, and visualization

## Core Mathematics

For a matrix

**A = [[a, b], [c, d]]**

and a vector

**v = (x, y)**

the transformed vector is:

**Av = (ax + by, cx + dy)**

The program applies this transformation to the vertices of the unit square.

## Determinant and Trace

For a 2x2 matrix:

**det(A) = ad - bc**

and

**trace(A) = a + d**

These values are also used when calculating the eigenvalues.

## Eigenvalues

The eigenvalues are found using the characteristic equation:

**λ² - trace(A)λ + det(A) = 0**

The program solves this quadratic equation to calculate the real eigenvalues of the matrix.

## Eigenvectors

For each eigenvalue λ, an eigenvector satisfies:

**(A - λI)v = 0**

The program calculates an eigenvector corresponding to each real eigenvalue and displays its direction on the visualization.

## Visualization

The graph shows:

- the original unit square
- the transformed unit square
- the directions of the eigenvectors

This makes it easier to see how a matrix changes space and why eigenvectors are special directions under a linear transformation.

## Technologies and Concepts

- Python
- Python 3
- Linear algebra
- Matrices
- Vectors
- Matrix transformations
- Determinants
- Eigenvalues
- Eigenvectors
- Matplotlib

## Status

**Completed**

This project was created to connect linear algebra calculations with a visual representation of how matrices transform two-dimensional space.
