# Core Pkgs
import streamlit as st

# Utils Pkgs
import codecs

# Components Pkgs
import streamlit.components.v1 as components

# st.set_page_config(layout="wide")
prcnt_width = 100
max_width_str = f"max-width: {prcnt_width}%;"
st.markdown(f"""
               <style>
               .block-container{{{max_width_str} ; background-color:white; padding-x:auto; height: auto; padding-y:auto; }}
                header {{visibility: hidden;}}   
                footer {{visibility: hidden;}}
                   
               """,
            unsafe_allow_html=True, )

def ID_Tool(ID_html, height= 1000):
	ID_file = codecs.open(ID_html,'r')
	page = ID_file.read()
	components.html(page, height=height, scrolling=1)



def main():

	ID_Tool('ID.html')



if __name__ == '__main__':

	main()
