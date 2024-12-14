import requests
import streamlit as st

def form_request(email, password):
    return {'email': email, 'password': password}


class Login:
    def __init__(self, login_url, cookie_controller):
        self.login_url = login_url
        self.controller = cookie_controller


    def login(self, email, password):
        login_inf = requests.post(self.login_url, data=form_request(email, password)).json()
        if login_inf["state"] == "success":
            self.controller['access_token'] = login_inf["access_token"]
            self.controller['user_id'] = login_inf["id"]
            self.controller.save()

            st.success("Login Successful")
            st.rerun()
        else:
            st.error("Login Failed")

    @st.dialog("register")
    def register(self):
        st.write("Register")
        if st.button("submit"):
            st.rerun()


    def display(self):

        _,center,_ = st.columns(3)
        center.header("H2SO4.ai")
        center.image("icons/flask.png", width=100)

        st.title("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        left, mid = st.columns(2)
        if left.button("Login", use_container_width=True):
            self.login(email, password)


        if mid.button("Register", use_container_width=True):
            self.register()
