import streamlit as st
import requests
import time


def response_generator(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


class ChatBot:
    def __init__(self, room_id, conversation, url_llm):
        self.__id = room_id
        self.__conversation = conversation
        self.__url_llm = url_llm

    def request_form(self, content):
        return {
            "roomchatId": self.__id,
            "content": content,
            "role": "user"
        }

    def display(self):

        st.session_state.messages = self.__conversation
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        prompt = st.chat_input("Say something", key=self.__id)

        if prompt:
            with st.chat_message("user"):
                st.markdown(prompt)
            # Add user message to chat history

            st.session_state.messages.append({"role": "user", "content": prompt})
            response = requests.post(self.__url_llm, json=self.request_form(prompt))
            with st.chat_message("assistant"):
                rep_content = st.write_stream(response_generator(response.json()["message"]["content"]))
                st.session_state.messages.append({"role": "assistant", "content": rep_content})



if __name__ == "__main__":
    url_chatbot = "http://localhost:3000/messages/send"
    chat_history = requests.get("http://localhost:3000/messages/674a14d210793aeaaeebe213").json()
    chat_page = ChatBot(room_id=None,url_llm=url_chatbot, conversation=chat_history)
    chat_page.display()

