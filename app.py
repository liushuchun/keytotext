import streamlit as st
from streamlit_tags import st_tags
from keytotext import pipeline
import re

st.set_page_config(
    page_title="Text Generation Using Keywords",
    layout="wide",
    initial_sidebar_state="expanded", )


@st.cache(suppress_st_warning=True, ttl=1000)
def generate(keywords, model="k2t"):
    nlp = pipeline(model)
    return nlp(keywords)


def display():
    st.write('# Keytotext UI')
    st.sidebar.markdown(
        '''
        ## Keytotext
        *For additional questions and inquiries, please contact **Gagan Bhatia** via [LinkedIn](
        https://www.linkedin.com/in/gbhatia30/) or [Github](https://github.com/gagan3012).*
        ''')
    st.sidebar.write('## Options:')

    top_p = st.sidebar.slider(label='Top k', min_value=0.0, max_value=40.0, value=1.0, step=1.0)
    temp = st.sidebar.slider(label='Temperature', min_value=0.1, max_value=1.0, value=1.0, step=0.05)
    st.sidebar.markdown(
        '''
        `Number of Keywords:` number of keywords given\n
        `Temperature:` Float value controlling randomness in boltzmann distribution. Lower temperature results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive. Higher temperature results in more random completions.\n
        `Top k:` Integer value controlling diversity. 1 means only 1 word is considered for each step (token), resulting in deterministic completions, while 40 means 40 words are considered at each step. 0 (default) is a special setting meaning no restrictions. 40 generally is a good value.
        ''')

    keywords = st_tags(
        label='## Enter Keywords:',
        text='Press enter to add more',
        value=['India', 'wedding', 'Food'],
        maxtags=4,
        key='1')
    if st.button("Get Answer"):
        text = generate(keywords)
        st.write("# Generated Sentence:")
        st.write("## {}".format(text))


if __name__ == '__main__':
    display()
