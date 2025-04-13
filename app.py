import streamlit as st
import numpy as np
import cv2
import plotly.graph_objects as go

st.set_page_config(page_title="TB Affected Lung - 3D Visualizer", layout="centered")
st.markdown("<h1 style='text-align: center;'>🫁 TB Affected Lung - 3D Visualizer</h1>", unsafe_allow_html=True)
st.markdown("Upload a chest X-ray image showing TB-affected areas. This tool will generate an interactive 3D simulation based on the 2D region.")

uploaded_file = st.file_uploader("Upload Chest X-ray Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    grayscale_image = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(grayscale_image, (256, 256)) 

    st.subheader("Original X-ray")
    st.image(resized_image, use_column_width=True, clamp=True)

    st.subheader("Threshold for TB Detection")
    threshold_value = st.slider("Adjust threshold value", 0, 255, 180)
    
    _, tb_mask = cv2.threshold(resized_image, threshold_value, 255, cv2.THRESH_BINARY)

    st.subheader("Simulated TB Region Mask")
    st.image(tb_mask, use_column_width=True, clamp=True)

    tb_pixel_count = np.count_nonzero(tb_mask)
    st.info(f"Detected TB-like pixels: {tb_pixel_count}")

    height_map = tb_mask.astype(float) / 255.0 * 100 
    x_coordinates, y_coordinates = np.meshgrid(np.arange(height_map.shape[1]), np.arange(height_map.shape[0]))

    fig = go.Figure(data=[
        go.Surface(
            z=height_map, x=x_coordinates, y=y_coordinates,
            colorscale='Reds', showscale=False,
            lighting=dict(ambient=0.5, diffuse=0.9, roughness=0.8),
            lightposition=dict(x=100, y=200, z=0)
        )
    ])
    
    fig.update_layout(
        title="Revolved 3D TB-Affected Lung Simulation",
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='TB Intensity',
            xaxis_visible=False,
            yaxis_visible=False,
            zaxis=dict(showgrid=False),
        ),
        margin=dict(l=0, r=0, b=0, t=40),
        height=600
    )

    st.subheader("Interactive 3D TB Region")
    st.plotly_chart(fig, use_container_width=True)
    st.success("3D TB visualization generated!")

else:
    st.warning("Please upload a chest X-ray image to get started.")
