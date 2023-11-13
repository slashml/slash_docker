## Contributing

Slash_Docker is created at [slashml](https://slashml.co), but as an open and living project eagerly accepts contributions of all kinds from the broader developer community. Please note that all participation with slash_docker falls under our [code of conduct](CODE_OF_CONDUCT.md).


You can perform one of the following tasks:

* For bugs and feature requests, file an issue.
* For changes and updates, create a pull request.

## Local development

To get started contributing to the library, all you have to do is clone this repository!

### Setup

Git clone this repo `git clone git@github.com:slashml/slash_docker.git`. Then `cd` into `slash_docker`.


Then install the dependencies with:
```
pip install -r requirements.txt
```


### Release

When releasing a version of the library with user-facing changes, be sure to update the [changelog](docs/CHANGELOG.md) with an overview of the changes, along with updating any relevant documentation. Feel free to tag @philipkiely-baseten to write or review any changelog or docs updates.
To release a new version of the library.

1. Create a PR changing the `pyproject.toml` version
2. Merge the PR, github actions will auto deploy if it detects the change

#### Manual Release

1. Create a tag on a commit `git tag -a -m "vX.X.X" vX.X.X
2. Push the tag  `git push -u origin vX.X.X`

## Documentation

To learn about Truss see the [official documentation](https://truss.baseten.co).

Contributions to documentation are very welcome! Simply edit the appropriate markdown files in the `docs/` folder and make a pull request. For larger changes, tutorials, or any questions please contact [philip.kiely@baseten.co](mailto:philip.kiely@baseten.co)

## Contributors

Truss was made possible by:

[Baseten Labs, Inc](http://baseten.co)
* Phil Howes
* Alex Gillmor
* Pankaj Gupta
* Philip Kiely
* Nish Singaraju
* Abu Qadar
* and users like you!
