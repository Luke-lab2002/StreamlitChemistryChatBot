import requests
import streamlit as st

def form_request(email, password):
    return {'email': email, 'password': password}


class Login:
    def __init__(self, login_url, cookie_controller):
        self.login_url = login_url
        self.controller = cookie_controller

    def display(self):

        st.title("Đăng ký tài khoản")

        with st.form("my_form"):
            email = st.text_input("Tên đăng nhập")
            password = st.text_input("Mật khẩu", type="password")
            submitted = st.form_submit_button("Đăng nhập")
            if submitted:
                # Kiểm tra thông tin đăng nhập (thay thế bằng logic xác thực của bạn)
                login_inf = requests.post(self.login_url, data=form_request(email, password)).json()
                if login_inf["state"] == "success":
                    # st.session_state['authenticated'] =
                    # Thiết lập thời gian hết hạn cho cookie 'access_token'
                    self.controller['access_token'] = login_inf["access_token"]
                    self.controller['user_id'] = login_inf["id"]
                    self.controller.save()
                    # st.session_state["userid"] = login_inf["id"]
                    st.success("Đăng nhập thành công!")
                    st.rerun()
                else:
                    st.error("Tên đăng nhập hoặc mật khẩu không đúng.")

