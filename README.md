# 3D-Reveal-of-TB-Rotational-View-from-a-Chest-X-ray
# TB Affected Lung - 3D Visualizer

This is a Streamlit-based web application that allows users to upload a **chest X-ray image** showing **Tuberculosis (TB)-affected regions**, and generates an **interactive 3D visualization** of the affected area based on pixel intensity.

## Features

- Upload chest X-ray images (JPG, PNG, JPEG)
- Adjustable threshold to detect TB-like regions
- Visual display of:
  - Original grayscale X-ray
  - Detected TB region mask
- Interactive 3D surface plot of the TB-affected region using Plotly
- Pixel-based intensity mapping to simulate TB region depth

## How It Works

1. Upload a 2D chest X-ray image.
2. Apply a threshold to highlight potential TB-affected areas.
3. Convert the thresholded binary mask into a height map.
4. Visualize the height map as a 3D surface using `plotly.graph_objects`.


## Dependencies

Make sure to install the following Python libraries:

```bash
pip install streamlit opencv-python-headless numpy plotly
