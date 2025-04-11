import streamlit as st
from scrape import scrape_website,split_dom_content,clean_body_content,extract_body_content
from parse import parse_with_groq


st.title("AI Web Scrapper")
url=st.text_input("Enter the Website URL to be Scrapped: ")

if st.button("Let's GO"):
    st.write("Doing Your Job BOSS!!")

    result=scrape_website(url)
    body_content=extract_body_content(result)
    cleaned_content=clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content",cleaned_content,height=300)


if "dom_content" in st.session_state:
    parse_description=st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the Content BOSS")

            dom_chunks=split_dom_content(st.session_state.dom_content)
            result= parse_with_groq(dom_chunks,parse_description)
            st.write(result)
