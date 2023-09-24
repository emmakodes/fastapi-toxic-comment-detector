## fastapi-toxic-comment-detector
This Project detects if a comment is toxic or not. It is built using FastAPI
## How to setup the project locally
- Clone the project 
`git clone https://github.com/emmakodes/fastapi-toxic-comment-detector.git`
- cd `fastapi-toxic-comment-detector`
- Create a virtual environment .venv
`python -m venv .venv`
- Activate the virtual environment
`.venv\Scripts\activate`
- run `pip install -r requirements.txt` on the terminal to install the project requirements
- start the project using the following command:
`uvicorn app.main:app --reload`

## How the project works
- Start the project using the following command:
`uvicorn app.main:app --reload`
- Go to Postman, change the method to POST, access the following path `http://127.0.0.1:8000/comments/` pass your comment to the body of the request, and click Send. The API should respond with a response
![fastapi1](https://github.com/emmakodes/fastapi-toxic-comment-detector/assets/34986076/d999a46c-379f-4845-928b-1851dccd782d)
