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

[//]: # (TODO: add more parameters to TextOverlay)

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

#### Contrast

Receives the input and returns it with a contrast applied.

```yaml
algorithms:
  - name: "Contrast"
    parameters:
      - name: "gain"
        value: 1.5
```

#### Brightness

Receives the input and returns it with a brightness applied.

```yaml
algorithms:
  - name: "Brightness"
    parameters:
      - name: "bias"
        value: 1.5
```

#### Gamma Correction

Receives the input and returns it with a gamma correction applied.

```yaml
algorithms:
  - name: "GammaCorrection"
    parameters:
      - name: "gamma"
        value: 1.5
```

### Filters

#### Gaussian Blur

Applies a Gaussian blur to the input image. The `size` parameter is the kernel size

```yaml
algorithms:
  - name: "GaussianBlur"
    parameters:
      - name: "size"
        value: 5
```

#### Box Filter

Applies a box filter to the input image. The `size` parameter is the kernel size

```yaml
algorithms:
  - name: "BoxFilter"
    parameters:
      - name: "size"
        value: 5
```

### Geometric Transformation

#### Flip

Flips the input image.

```yaml
algorithms:
  - name: "Flip"
    parameters:
      - name: "vertical"
        value: true
      - name: "horizontal"
        value: false
```

> Default values:
> - vertical: False
> - horizontal: False

#### Translation

Translates the input image. Parameters are in pixels.

```yaml
algorithms:
  - name: "Translation"
    parameters:
      - name: "x"
        value: 10
      - name: "y"
        value: 10
```

> Default values:
> - x: 0
> - y: 0

#### Rotation

Rotates the input image by a given angle in degrees around a center point.

```yaml
algorithms:
  - name: "Rotation"
    parameters:
      - name: "angle"
        value: 90
      - name: center
        value:
          x: 0.5
          y: 0.5
```

> Default values:
> - angle: 0
> - center: "image center"

#### Shearing

Shears the input image.

```yaml
algorithms:
  - name: "Shearing"
    parameters:
      - name: "x"
        value: 0.5
      - name: "y"
        value: 0.5
```

> Default values:
> - x: 0
> - y: 0

#### Scaling

Scales the input image. The image dimension will remain the same, but the content will be scaled

```yaml
algorithms:
  - name: "Scaling"
    parameters:
      - name: "x"
        value: 0.5
      - name: "y"
        value: 0.5
```

> Default values:
> - x: 1
> - y: 1

#### Resizing

Resizes the input image by a resize factor. The image dimension will change.

```yaml 
algorithms:
  - name: "Resizing"
    parameters:
      - name: "x"
        value: 100
      - name: "y"
        value: 100
```

> Default values:
> - x: 1
> - y: 1
