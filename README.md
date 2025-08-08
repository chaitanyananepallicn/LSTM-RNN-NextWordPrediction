# Shakespearean Text Generator (LSTM & Streamlit)

This project uses a Long Short-Term Memory (LSTM) Recurrent Neural Network (RNN) to generate new text in the style of William Shakespeare. The model is trained on the full text of "Hamlet" and is served through an interactive web application built with Streamlit.



***

## ## Live Application

**You can access a live deployed demo here:**
[**➡️ Live Shakespeare AI App**](https://lstm-rnn-nextwordprediction.onrender.com) ***

## ## Features

* **AI-Powered Text Generation**: Provide a starting phrase ("seed text") and let the model generate the text that follows.
* **Shakespearean Style**: The generated text mimics the vocabulary, style, and structure found in "Hamlet".
* **Customizable Output Length**: Specify how many words you want the model to generate.
* **Interactive UI**: A simple and clean web interface built with Streamlit to easily interact with the trained model.

***

## ## Tech Stack

* **Core Language**: Python
* **Deep Learning**: TensorFlow / Keras
* **Web Framework**: Streamlit
* **NLP Toolkit**: NLTK (for the dataset)
* **Numerical Operations**: NumPy

***

## ## Dataset

This model was trained on the classic "Hamlet" text by William Shakespeare, which is included in the **NLTK `gutenberg` corpus**. The entire play is used to teach the model the patterns of Shakespearean English.

***

## ## Getting Started

To run this project on your local machine, follow these steps.

### ### Prerequisites

Make sure you have Python 3.8+ and pip installed on your system.

### ### Installation & Usage

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/chaitanyananepallicn/LSTM-RNN-NextWordPrediction.git
    cd shakespeare-text-generator
    ```

2.  **Create and Activate a Virtual Environment**
    * **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Create a `requirements.txt` file**
    * Create a file named `requirements.txt` and add the following lines:
        ```
        tensorflow
        streamlit
        nltk
        numpy
        ```

4.  **Install the Required Libraries**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Download NLTK Data**
    * Run Python and download the `gutenberg` corpus. You only need to do this once.
    ```python
    import nltk
    nltk.download('gutenberg')
    ```

6.  **Train the Model (If necessary)**
    * If a `train.py` script is included, run it to train the LSTM model and save the weights. This may take a significant amount of time.
    ```bash
    python train.py
    ```

7.  **Run the Streamlit Application**
    ```bash
    streamlit run app.py
    ```
    * After running the command, open your web browser and navigate to the local URL provided (usually `http://localhost:8501`).
