# ChatIITK - An Advanced RAG ChatBot for IITK Junta

Developed by BCS under its Summer Project - Lluminating Language

## Environment Setup

The app is still in prototyping stage so before running, create a separate virtual environment, so that there are no conflicts.
```
conda create -n ChatIITK python=3.10.0
conda activate ChatIITK
```

After successfully creating a virtual env, install all the requirement for the project

```
pip install -r requirements.txt
```

## Inference
Before start inferencing, we need to ingest our data into our VectorDB(ChromaDB in this case).

You can change the device type to cpu or mps if you don't want access to GPU, by default it will run on best available compute (mps or gpu) otherwise cpu

```
python ingest.py --device_type gpu
```
After the ingestion of data is complete you can see, local vectorDB files in the `DB` folder, Now:

- To start the Terminal interface run `python run_ChatIITK.py`
- To start the Streamlit UI run `streamlit run ChatIITK_UI.py`
