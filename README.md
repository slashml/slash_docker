# Model to Docker
A unified way to package pre-trained models into docker files


# Model to Docker in action, or how it works

<iframe width="560" height="315"
src="https://www.youtube.com/embed/rc6ylq01D0c" 
frameborder="0" 
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>

# Installation guide

```
git clone git@github.com:slashml/slash_docker.git
cd slash_docker
pip install -e .
```

# Quickstart


```python
from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit([[2], [3], [4]], [4,6,8])

#test the model locally
lm.predict([[1024]])

```

```python
# serialize and save the model
from model_to_docker import save_model
save_model(lm, 'sklearn_linear_regression')

```

```python
# start a docker container with the previously saved model
# this will create a docker image, and start a docker container
from model_to_docker import run_model_server

# this will take a few seconds if its the first time
container = run_model_server('sklearn_linear_regression', port=5000)

```

```python
# perform inference on the locally running docker container
import requests

resp = requests.post('http://127.0.0.1:8080/v1/models/model:predict', '[[1024]]')

print(resp.json())
```

```bash
# you can also use the curl command in terminal to perform inference
curl http://127.0.0.1:8080/v1/models/model:predict -d '[[1025]]'
```

```python
# stop the docker container
from model_to_docker import stop_model_server
stop_model_server(container.id)
```


For other examples look inside the examples folder


### Supported frameworks

* Scikit-learn 
* XGBoost
* PyTorch
* Mlflow
* TensorFlow
* MLFLow
* FastAI
* HuggingFace Transformers
* Keras
* LightGBM
* ONNX
* PyCaret
* SegmentAnything

### Contact
If you run into any issues, or need a new feature, or any custom help, please feel free to reach out to us at faizank@slashml.com, support@slashml.com

### Contributing
We are actively looking for contributors. Please look at the [CONTRIBUTING.md](https://github.com/slashml/slash_docker/blob/main/CONTRIBUTING.md) guide for more details. We have a growing list of good_first_issues, you can reach us at support@slashml.com, to get started.