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

### Identity

Receives the input and returns it.

```yaml
algorithms:
  - name: "Identity"
```

### Composite

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

### Rotate

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

[//]: # (### Text Overlay)

[//]: # (### Contrast)

[//]: # (> Gain, Bias)

[//]: # (### Blur)

[//]: # (### Gamma Correction)

[//]: # (### Histogram Equalization)
