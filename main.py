from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title='SCR1M',
    description='SCR1M-Server',
    version='0.0.1',
    terms_of_service='https://github.com/ParkHyeonSeong/SCR1M-Server',
    doc_url='/docs',
    redoc_url='/redoc',
    contract={
        'name': 'ParkHyeonSeong',
        'url': 'https://github.com/ParkHyeonSeong',
        'email': '9707.hyeon@gmail.com'
    },
    # openapi_url=None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    expose_headers=['*']
)

# 
@app.get('/')
def index():
    return 0