from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    
    return {
        'data':{
            'name':'Samake',
            'last_name':'Mohamed',
        }
    }