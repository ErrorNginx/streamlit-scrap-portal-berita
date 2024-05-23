from setuptools import setup, find_packages

setup(
    name="scraping_news_portal",
    version="0.1",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'streamlit',
        'requests',
        'beautifulsoup4',
        'pandas',
    ],
)
