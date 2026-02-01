from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import streamlit as st

# Load translator model and tokenizer
translator_model_name = "Helsinki-NLP/opus-mt-en-fr"
translator_tokenizer = AutoTokenizer.from_pretrained(translator_model_name)
translator_model = AutoModelForSeq2SeqLM.from_pretrained(translator_model_name)

# Input text
text_to_translate = "How are you"

# Tokenize input and generate translation
inputs = translator_tokenizer(text_to_translate, return_tensors="pt")
translated_ids = translator_model.generate(**inputs)
translated_text = translator_tokenizer.decode(translated_ids[0], skip_special_tokens=True)

print("\nTranslation (English to French):")
print(translated_text)



st.title("Spam Detection System")
def spamdetection():
    user = st.text_area("Enter any Message or Email: ")
    if len(user) < 1:
        st.write("  ")
    else:
        sample = user
        data = cv.transform([sample]).toarray()
        a = clf.predict(data)
        st.title(a)
spamdetection()