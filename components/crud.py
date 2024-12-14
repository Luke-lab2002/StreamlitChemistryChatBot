import streamlit as st
import requests


def form_request(name):
    return {'name': name}

class Crud:
    def __init__(self, id_roomchat ,url_rename, url_delete):
        self.url_rename = str(url_rename + id_roomchat)
        self.url_delete = str(url_delete + id_roomchat)

    def rename_roomchat(self, name):
        requests.put(self.url_rename, form_request(name))
        st.rerun()

    def delete_roomchat(self):
        requests.delete(self.url_delete)
        st.rerun()

    @st.dialog("Rename room chat")
    def rename(self):
        st.write("Rename room chat")
        reason = st.text_input("name")
        if st.button("rename"):
            self.rename_roomchat(name=reason)
            st.rerun()

    @st.dialog("Delete room chat")
    def delete(self):
        st.write("Are you sure ?")
        if st.button("delete"):
            self.delete_roomchat()
            st.rerun()



    def display(self):
        left, middle = st.columns(2)
        if left.button("Rename", use_container_width=True):
            self.rename()
        if middle.button("Delete", use_container_width=True):
            self.delete()


# url1 = "http://localhost:3000/roomchat/"
# url2 = "http://localhost:3000/roomchat/"
# id = "67580433954619fa5e9c838c"
#
# url = url1 + id
#
# # print(url)
# crud = Crud(id_roomchat=id, url_rename=url1, url_delete=url1)
# crud.display()