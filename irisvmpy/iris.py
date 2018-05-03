#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Simple Iris data set classifier based on Support Vector Machines algorithm.
"""

from __future__ import print_function
import time
from sklearn import svm, datasets
import click



# import some data to play with
iris = datasets.load_iris()

X = iris.data[:, :2]  # we only take the first two features. We could
# avoid this ugly slicing by using a two-dim dataset
y = iris.target


svc = svm.SVC(kernel='rbf', C=1, gamma=0.7).fit(X, y)

dimm_names = ['Petal Length', 'Petal Width', 'Sepal Length', 'Sepal Width']


@click.command()
@click.argument('dimensions', nargs=4, type=float)
def cli(dimensions):
    """Basic command line interface.

    Arguments:
    dimensions {list} -- list of flower dimensions: PL, PW, SL, SW
    """
    click.echo("Iris Flower classifier\n")

    click.echo("Calculating result...")
    time.sleep(1)
    results = zip(dimm_names, dimensions)
    click.echo("Input data:")
    for i, j in results:
        click.echo("{:12} -> {}".format(i, j))

    click.echo()
    click.echo("Your flower seems to be fine example of:")
    click.secho("{}".format("species"), fg='green', bold=True)


if __name__ == "__main__":
    cli()
