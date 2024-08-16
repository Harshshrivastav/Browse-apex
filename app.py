# V_1

# import streamlit as st
# from langchain_groq import ChatGroq
# from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
# from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
# from langchain.agents import initialize_agent,AgentType
# from langchain.callbacks import StreamlitCallbackHandler
# import os
# from dotenv import load_dotenv

# ## Arxiv and wikipedia Tools
# arxiv_wrapper=ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
# arxiv=ArxivQueryRun(api_wrapper=arxiv_wrapper)

# api_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=200)
# wiki=WikipediaQueryRun(api_wrapper=api_wrapper)

# search=DuckDuckGoSearchRun(name="Search")


# st.title("🔎 LangChain - Chat with search")
# """
# In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
# Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
# """

# ## Sidebar for settings
# st.sidebar.title("Settings")
# api_key=st.sidebar.text_input("Enter your Groq API Key:",type="password")

# if "messages" not in st.session_state:
#     st.session_state["messages"]=[
#         {"role":"assisstant","content":"Hi,I'm a chatbot who can search the web. How can I help you?"}
#     ]

# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg['content'])

# if prompt:=st.chat_input(placeholder="What is machine learning?"):
#     st.session_state.messages.append({"role":"user","content":prompt})
#     st.chat_message("user").write(prompt)

#     llm=ChatGroq(groq_api_key=api_key,model_name="Llama3-8b-8192",streaming=True)
#     tools=[search,arxiv,wiki]

#     search_agent=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handling_parsing_errors=True)

#     with st.chat_message("assistant"):
#         st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
#         response=search_agent.run(st.session_state.messages,callbacks=[st_cb])
#         st.session_state.messages.append({'role':'assistant',"content":response})
#         st.write(response)

# V-2

# import streamlit as st
# from langchain_groq import ChatGroq
# from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
# from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
# from langchain.agents import initialize_agent, AgentType
# from langchain.callbacks import StreamlitCallbackHandler


# st.set_page_config(
#     page_title="Browse APEX",
#     page_icon="🔎",
#     layout="centered",
# )
# ## Custom CSS for hover effects and background
# st.markdown(
#     """
#     <style>
#     .custom-title {
#         background-color: #2b6777;
#         padding: 20px;
#         border-radius: 8px;
#         text-align: center;
#         color: white;
#         margin-bottom: 25px;
#     }

#     .sidebar .stTextInput input {
#         border: 1px solid #2b6777;
#         border-radius: 8px;
#     }

#     .sidebar .stTextInput input:hover {
#         background-color: #FFF9E3; /* Light lemon yellow hover */
#         transition: background-color 0.3s ease-in-out;
#     }

#     .st-chat-message {
#         border-radius: 15px;
#         padding: 15px;
#         margin-bottom: 10px;
#     }

#     .st-chat-message:hover {
#         background-color: #FFF9E3; /* Light lemon yellow hover */
#         transition: background-color 0.3s ease-in-out;
#     }

#     .st-button button {
#         background-color: #2b6777;
#         color: white;
#         border-radius: 8px;
#     }

#     .st-button button:hover {
#         background-color: #FFF9E3; /* Light lemon yellow hover */
#         color: #2b6777;
#         transition: background-color 0.3s ease-in-out;
#     }
#     </style>
#     """, unsafe_allow_html=True
# )

# ## Arxiv and Wikipedia Tools
# arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
# arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

# api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
# wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

# search = DuckDuckGoSearchRun(name="Search")

# ## Page Title and Header
# st.markdown("<div class='custom-title'><h1>🔎Browse with APEX</h1></div>", unsafe_allow_html=True)
# st.write("""
#         lets explore!
# """)

# ## Sidebar for settings
# st.sidebar.title("Settings")
# api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

# ## Session State for chat history
# if "messages" not in st.session_state:
#     st.session_state["messages"] = [
#         {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
#     ]

# ## Display chat history
# for msg in st.session_state["messages"]:
#     st.chat_message(msg["role"]).write(msg["content"])

# ## Input for new user prompt
# if prompt := st.chat_input(placeholder="What is machine learning?"):
#     st.session_state["messages"].append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)

#     ## LLM setup using Groq
#     llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)
#     tools = [search, arxiv, wiki]

#     ## Initialize the agent
#     search_agent = initialize_agent(
#         tools=tools,
#         llm=llm,
#         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#         handling_parsing_errors=True
#     )

#     ## Handle response and callback
#     with st.chat_message("assistant"):
#         st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
#         response = search_agent.run(st.session_state["messages"], callbacks=[st_cb])

#         ## Append and display assistant's response
#         st.session_state["messages"].append({"role": "assistant", "content": response})
#         st.write(response)


# V-3

import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler

# Streamlit page config with updated name and icon
st.set_page_config(
    page_title="Browse APEX",
    page_icon="🔎",
    layout="centered"
)

# Custom Title and description with CSS and hover effects
st.markdown(
    """
    <style>
    .container {
        background-image: url("https://cdn.pixabay.com/animation/2023/06/26/03/02/03-02-03-917_512.gif");
        background-size: cover;
        margin: 0;
        padding: 50px;
        border-radius: 5px;
        border: 1px solid #ddd;
        position: relative;
        overflow: hidden;
    }

    .container::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 0;
        height: 100%;
        background-color: #64CCC5;
        transition: width 0.5s ease;
        z-index: 0;
    }

    .container:hover::before {
        width: 100%;
    }

    .container h4,
    .container p {
        position: relative;
        z-index: 1;
        color: #fff;
        transition: color 0.5s ease;
    }

    .container:hover h4,
    .container:hover p {
        color: #000;
    }
    </style>

    <div class="container">
        <h4>🔎 Browse APEX</h4>
        <p>Explore web content with advanced AI-powered tools.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

# Arxiv and Wikipedia Tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200))
search = DuckDuckGoSearchRun(name="Search")

# Initialize chat messages in session state
if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}]

# Chat history block in the sidebar
st.sidebar.subheader("Chat History")
with st.sidebar.expander("View Browse history"):
    for msg in st.session_state.messages:
        if msg["role"] == "assistant":
            st.markdown(f"**Assistant**: {msg['content']}")
        else:
            st.markdown(f"**User**: {msg['content']}")

# Input for new user prompt
if prompt := st.chat_input(placeholder="What would you like to search for?"):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # LLM setup using Groq
    if api_key:
        llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)
        tools = [search, arxiv, wiki]

        # Initialize the agent
        search_agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            handling_parsing_errors=True
        )

        # Handle response and callback
        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            try:
                response = search_agent.run(prompt, callbacks=[st_cb])
            except Exception as e:
                response = f"An error occurred: {str(e)}"

            # Append and display assistant's response
            st.session_state["messages"].append({"role": "assistant", "content": response})
            st.write(response)
    else:
        st.warning("Please provide the Groq API key.")
