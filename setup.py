from setuptools import setup

setup(
    name="bullet",
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "bullet = bullet:main"
        ]
    }
)
