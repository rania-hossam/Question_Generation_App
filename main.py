import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the model and tokenizer
model = T5ForConditionalGeneration.from_pretrained('C:\\Users\\rania\\Downloads\\Question_Generation_APP\\TF_MODEL')
tokenizer = T5Tokenizer.from_pretrained('C:\\Users\\rania\\Downloads\\Question_Generation_APP\\TF_TOKENIZER')

# Function to generate a question
def generate_question(context, answer):
    input_text = "answer: " + answer + " context: " + context
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    question_ids = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)
    question = tokenizer.decode(question_ids[0], skip_special_tokens=True)
    return "Generated Question: " + question

# Streamlit app
st.title("Question Generation App")

context = st.text_area("Enter context:", "")
answer = st.text_input("Enter answer:", "")

if st.button("Generate Question"):
    if context and answer:
        question = generate_question(context, answer)
        st.write(question)
    else:
        st.write("Please enter both context and answer.")
