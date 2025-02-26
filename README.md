# WebSearch Demo (AI Agent + Streamlit)
![Python](https://img.shields.io/badge/Python-Compatible-green.svg)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)

## Requirements
- Run the following command to install required packages
```bach
pip install -r requirements.txt
```

## Environment variables setup:
- Create the .env file that contains the following variables:
```bash
CREDENTIALS_PROFILE_NAME= "aws_profile_name"

```
- Load them via the following code:
```python
from dotenv import load_dotenv

load_dotenv()                   # Loading environment variables from .env file
```
## Demo

![Alt text](docs/demo.png)
