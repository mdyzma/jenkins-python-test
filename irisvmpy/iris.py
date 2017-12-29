from __future__ import print_function
from sklearn import svm, datasets
import click

import time

# import some data to play with
iris = datasets.load_iris()

X = iris.data[:, :2] # we only take the first two features. We could
 # avoid this ugly slicing by using a two-dim dataset
y = iris.target


svc = svm.SVC(kernel='linear', C=1,gamma='auto').fit(X, y)

species = 'Iris setosa'

dimens = ['Petal Length' , 'Petal Width' , 'Sepal Length' , 'Sepal Width']

@click.command()
@click.argument('dimensions', nargs=4, type=float)
# @click.option('--petal-width', '-pw', help='Unknown Iris Petal Width.', type=float)
# @click.option('--sepal-lenght', '-sl', help='Unknown Iris Sepal Lenght.', type=float)
# @click.option('--sepal-width', '-sw', help='Unknown Iris Sepal Width.', type=float)
# def cli(petal_lenght, petal_width, sepal_lenght, sepal_width):
def cli(dimensions):
	click.echo("Iris Flower classifier\n")

	click.echo("Calculating result...")
	time.sleep(1)
	results = zip(dimens, dimensions)
	click.echo("Input data:")
	for i,j in results:
		click.echo("{:12} -> {}".format(i, j))
	# click.echo("Your Petal Lenght is: {}".format(petal_lenght))
	# click.echo("Your Petal Width  is: {}".format(petal_width))
	# click.echo("Your Sepal Lenght is: {}".format(sepal_lenght))
	# click.echo("Your Sepal Width  is: {}".format(sepal_width))
	click.echo()
	click.echo("Your flower seems to be fine example of:")
	click.secho("{}".format(species), fg='green', bold=True)
# [Petal Length , Petal Width , Sepal Length , Sepal width]

if __name__ == "__main__":
	cli()