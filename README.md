# Augmentation System

## Project Setup

### Prerequisites

### Installation

### How to run

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
      algorithms:
        - name: "Flip"
          parameters:
            axis: "X"
        - name: "Rotate"
          parameters:
            angleX: 45
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
