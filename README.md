# Augmentation System

## Project Setup

### Prerequisites

```shell
pip install -r requirements.txt
```

### How to run

```shell
python main.py
```

#### Tests

```shell
python -m unittest
```

## Algorithms

> For multiple examples see [examples](examples) and [test_data](test/test_augmentation/test_data) folders.

### Miscellaneous

#### Identity

Receives the input and returns it.

```yaml
algorithms:
  - name: "Identity"
```

#### Clip

Clips the input image between a minimum and maximum value.

```yaml
algorithms:
  - name: "Clip"
    parameters:
      - name: "min"
        value: 0.0
      - name: "max"
        value: 255.0  
```

#### Text Overlay

Receives the input and returns it with a text overlay.

```yaml
algorithms:
  - name: "TextOverlay"
    parameters:
      - name: "text"
        value: "Hello World"
```

#### Greyscale

Receives the input and returns it in greyscale.

```yaml
algorithms:
  - name: "Greyscale"
```

#### Composite

Receives a list of algorithms and applies them sequentially.

```yaml
algorithms:
  - name: "Composite"
    parameters:
      - name: "algorithms"
        value:
          - name: "Flip"
            parameters:
              - name: "axis"
                value: "X"
          - name: "Rotate"
            parameters:
              - name: "angleX"
                value: 45
```

### Pixel Transformation

### Contrast

Receives the input and returns it with a contrast applied.

```yaml
algorithms:
  - name: "Contrast"
    parameters:
      - name: "gain"
        value: 1.5
```

### Brightness

Receives the input and returns it with a brightness applied.

```yaml
algorithms:
  - name: "Brightness"
    parameters:
      - name: "bias"
        value: 1.5
```

### Geometric Transformation

#### Rotate

Rotates the input image by a given angle.

[//]: # (TODO: Describe the parameters in more details)

```yaml
algorithms:
  - name: "Rotate"
    parameters:
      angleX: 90
```

### Flip

Flips the input image.

[//]: # (TODO: Describe the parameters in more details)

```yaml
algorithms:
  - name: "Flip"
    parameters:
      axis: "X"
```

[//]: # (TODO: add more parameters to TextOverlay)

[//]: # (### Blur)

[//]: # (### Gamma Correction)

[//]: # (### Histogram Equalization)
