import setuptools

setuptools.setup(
    name="streamlit-option-menu",
    version="0.1.2",
    author="Victor Yan",
    author_email="victoryhb@163.com",
    description="streamlit-option-menu is a simple Streamlit component that allows users to select a single item from a list of options in a menu.",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
