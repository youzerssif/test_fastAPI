from fastapi import FastAPI


app = FastAPI()

@app.get('/')
# @app.get('/api')
def index():
    
    return {
        'data':{
            'name':'Samake',
            'last_name':'Mohamed',
        }
    }