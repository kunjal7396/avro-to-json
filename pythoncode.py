import streamlit as st
import fastavro
import json
import os

from utils import convert_avro_to_json

st.title("AVRO to JSON Converter")

uploaded_file = st.file_uploader("Upload an AVRO file", type=["avro"])

if uploaded_file:
    st.write("File uploaded successfully!")

    output_json = convert_avro_to_json(uploaded_file)
    
    st.subheader("Converted JSON Data")
    st.json(output_json)

    st.download_button(
        label="Download JSON File",
        data=json.dumps(output_json, indent=2),
        file_name="converted.json",
        mime="application/json",
    )
