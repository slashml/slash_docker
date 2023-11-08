# Model to Docker
A unified way to package pre-trained models into docker files

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

```

```python
from model_to_docker import save_model
save_model(lm, 'sklearn_linear_regression')

```

```python
from model_to_docker import run_model_server

container = run_model_server('sklearn_linear_regression', port=5000)

```

```python
from model_to_docker import stop_model_server
stop_model_server(container.id)
```


For other examples look inside the examples folder