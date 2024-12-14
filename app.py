import requests
import streamlit as st
from st_cookies_manager import CookieManager
from web.login import Login
from web.chat_page import ChatPage
from components.navigator import Navigator
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv('BACKEND_API')
URL_LLM = URL + "messages/send"
URL_CRUD_ROOM_CHAT= URL + "roomchat/"
URL_LIST_CONVERSATION = URL + "messages/"
URL_ROOM_CHAT = URL + "roomchat/"
URL_LOGIN = URL + "login/"

home_page = st.Page("web/read.py", title="Home")

controller = CookieManager()

if not controller.ready():
    st.stop()


def list_page():
    list_room_chat = [home_page]
    for conversation in list_room_json:
        conversation_json = requests.get(URL_LIST_CONVERSATION  + conversation["_id"]).json()
        chatbot = ChatPage(room_chat_id=conversation["_id"],
                           conversation=conversation_json,
                           url_llm=URL_LLM,
                           url_rename=URL_CRUD_ROOM_CHAT,
                           url_delete=URL_CRUD_ROOM_CHAT
                           )
        list_room_chat.append(st.Page(chatbot.display, title=conversation["name"], url_path=conversation["_id"]))

    return list_room_chat



if controller.get('access_token') is not None:
    list_roomchat_api = URL_ROOM_CHAT + "userid/" +  controller.get('user_id')
    list_room_json = requests.get(list_roomchat_api).json()


    Navigator(list_pages=list_page(),
              url_create_room_chat= URL_ROOM_CHAT + "create-roomchat",
              user_id=controller.get('user_id'),
              ).display(cookies=controller).run()


if controller.get('access_token') is None:
    Login(URL_LOGIN, controller).display()