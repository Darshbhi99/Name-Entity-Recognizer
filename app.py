import spacy
import spacy_streamlit as spt
import streamlit as st
nlp = spacy.load("en_core_web_sm")

def main():
    st.title('Name Entity Recognitions(NER) App')
    menu =  ['HOME', 'NER']
    choice = st.sidebar.selectbox('menu', menu)
    if choice == 'HOME':
        st.subheader('Word Tokenization')
        raw_text = st.text_area('Text to Tokenize', 'Enter Text Here')
        doc = nlp(raw_text)
        if st.button('Tokenize'):
            spt.visualize_tokens(doc)
    elif choice == 'NER':
        st.subheader('Name Entity Recognitions')
        raw_text = st.text_area('Text to Tokenize', 'Enter Text Here')
        doc = nlp(raw_text)
        spt.visualize_ner(doc)


if __name__ == '__main__':
    main()