# Question Generation App

This is a simple Streamlit-based web application that generates questions based on the provided context and answer using a pre-trained T5 model.

## How to Use

1. Ensure you have the necessary Python packages installed. You can install them using the following commands:
   ```bash
   pip install streamlit transformers
   ```

2. Clone or download the repository to your local machine.

3. Open a terminal and navigate to the directory containing the app's files.

4. Run the app using the following command:
   ```bash
   streamlit run app.py
   ```

5. The app will open in your web browser, allowing you to generate questions from the provided context and answer.
6. ![Screenshot 1]([https://github.com/rania-hossam/ST_GYWALKER_APP/blob/main/images/6.png](https://github.com/rania-hossam/Question_Generation_App/blob/master/images/Screenshot%20(85).png))


## App Usage

1. **Title**: The app title "Question Generation App" is displayed at the top.

2. **Enter Context**: In the text area provided, enter the context for which you want to generate a question.

3. **Enter Answer**: In the text input box, enter the answer related to the context.

4. **Generate Question**: Click the "Generate Question" button to generate a question based on the provided context and answer.

5. **Generated Question**: The generated question will be displayed below the button if both context and answer are provided. If either field is empty, a message will prompt you to enter both context and answer.

## Model and Tokenizer

This app uses the Hugging Face Transformers library to load the T5 model and tokenizer. You can customize the model and tokenizer paths by modifying the `model_path` and `tokenizer_path` variables in the code.

## Important Note

Make sure to have the T5 model and tokenizer files available locally and set the correct paths in the code. The provided paths in this README are examples and should be updated to match the actual paths on your machine. Additionally, ensure that your Python environment has the required dependencies installed.

For more information about the Transformers library and T5 model, you can visit the [Hugging Face Transformers documentation](https://huggingface.co/transformers/).
