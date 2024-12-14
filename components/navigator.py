import streamlit as st
import requests

def form_request(name, user_id):
     return {'name': name, 'userId': user_id}


class Navigator:
    def __init__(self ,list_pages=None, url_create_room_chat=None, user_id=None, login_url=None):
        self.list_pages = list_pages
        self.url_create_room_chat =url_create_room_chat
        self.user_id = user_id
        self.login_url = login_url

    def create_room_chat(self, name, user_id):
        requests.post(self.url_create_room_chat, form_request(name, user_id))
        st.rerun()

    @st.dialog("create room chat")
    def modal(self, user_id):
        st.write("Create room chat")
        reason = st.text_input("name")
        if st.button("create"):
            self.create_room_chat(name=reason, user_id=user_id)
            st.rerun()

    def display(self, cookies):
        if st.sidebar.button('Create Room Chat'):
            self.modal(self.user_id)
        if st.sidebar.button('Logout'):
            cookies.clear()
            cookies.save()
            st.rerun()

        pg = st.navigation(self.list_pages)

        return pg


