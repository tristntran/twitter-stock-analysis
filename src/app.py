import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# This bit initializes the model
client = OpenAI()
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system",
                                  "system": 
"""
You are a bot whose job is to instruct about the reddit wallstreet bets forum
Only answer questions based off of this.
You will be provided information regarding the forum and
relevant posts based on semantic search query. These will be injected via RAG.

You will be punished if you use any information that you have not been provided.
"""}]
    
def rag_search(prompt: str):
    """Funciton that uses a chroma db to get relevant information
    """
    return prompt

# this is the main chat loop
if prompt := st.chat_input("Ask me about the market."):
    # takes in the user prompt here here is where we can inject the
    # RAG enhanced search info.
    boosted_prompt = rag_search(prompt)
    st.session_state.messages.append({"role": "user",
                                      "content": boosted_prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            print(e.args[0])
            st.session_state.max_messages = len(st.session_state.messages)
            rate_limit_message = """
                Oops! Sorry, I can't talk now. Too many people have used
                this service recently.
            """
            st.session_state.messages.append(
                {"role": "assistant", "content": rate_limit_message}
            )
            st.rerun()
