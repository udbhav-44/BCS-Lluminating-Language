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
python ingest.py --device_type cuda 
```
After the ingestion of data is complete you can see, local vectorDB files in the `DB` folder, Now:

- To start the Terminal interface run `python run_ChatIITK.py`
    - Additional Flags with `run_ChatIITK.py`
    1. `--device_type cuda(or mps or cpu)` : You can select the compute on which you want to run the model.
    2. `--save_qa` : You can store user question and model responsesinto a csv file. This file will be stored as `/local_chat_history/qa_log.csv` 
    3. `--use_history or -h` : You can enable chat history. This is disable by default. You can enable it by using the `--use_history or -h` flag.
    4. `--show_sources` : To show, which chunks are being retrieved from your retriever. By default, it will show 4 different sources/chunks. You can change the number of sources/chunks
    5. `--help` : To get help on these flags.


- To start the Streamlit UI run `streamlit run ChatIITK_UI.py`

## How to select Different Embedding model and LLM:

- To select different model, you can specify them in `constants.py` 
- Change the `MODEL_ID` and `MODEL_BASENAME`. If you are using a quantized model (GGML, GPTQ, GGUF), you will need to provide `MODEL_BASENAME`. For unquantized models, set `MODEL_BASENAME` to `NONE`
- Refer to the examples in the `constant.py` file and check the HuggingFace Hub for more models.


