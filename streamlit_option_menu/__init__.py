import streamlit as st
import streamlit.components.v1 as components

import os

_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        "option_menu",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _component_func = components.declare_component(
        "option_menu", path=build_dir)

# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.


def option_menu(menu_title, options, default_index=0, menu_icon=None, icons=None, orientation="vertical",
                styles=None, key=None):
    component_value = _component_func(options=options, 
                key=key, defaultIndex=default_index, icons=icons, menuTitle=menu_title, 
                menuIcon=menu_icon, default=options[default_index], 
                orientation=orientation, styles=styles)
    return component_value

# Create a second instance of our component whose `name` arg will vary
# based on a text_input widget.
#
# We use the special "key" argument to assign a fixed identity to this
# component instance. By default, when a component's arguments change,
# it is considered a new instance and will be re-mounted on the frontend
# and lose its current state. In this case, we want to vary the component's
# "name" argument without having it get recreated.
if __name__ == "__main__":
    st.set_page_config(page_title="Option Menu", layout="wide")
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", "Upload","---", "Tasks", 'Settings'], 
        icons=['house', 'cloud-upload', None, "list-task", 'gear'], menu_icon="cast", default_index=1)

    selected2 = option_menu(None, ["Home", "Upload", "---", "Tasks", 'Settings'], 
        icons=['house', 'cloud-upload', None, "list-task", 'gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal")

    selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
        icons=['house', 'cloud-upload', "list-task", 'gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "green"},
        }
    )