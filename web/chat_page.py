import streamlit as st

from components.chatbot import ChatBot
from components.crud import Crud

class ChatPage:
    def __init__(self, room_chat_id, conversation, url_llm, url_rename, url_delete):
        self.room_chat_id = room_chat_id
        self.conversation = conversation
        self.url_llm = url_llm
        self.url_rename = url_rename
        self.url_delete = url_delete

    def display(self):
        st.title("Mistral Chemistry Chat Bot")

        Crud(id_roomchat=self.room_chat_id,
                    url_rename=self.url_rename,
                    url_delete=self.url_delete
                    ).display()

        ChatBot(room_id=self.room_chat_id,
                conversation=self.conversation,
                url_llm=self.url_llm
                ).display()




