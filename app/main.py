from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

import model
from database import engine
from router import noun, home

app = FastAPI(
    title="German Gender API",
    description="""
        German Gender API helps you to find out the grammatical gender of several nouns of the German language.
        
        ### Nouns
        
        In German, nouns can be masculine, ferminine or neuter. There are some basic definition rules, but, in general, 
        you would have to figure it out by yourself. That's where *German Gender API* comes in.
        
        It'll return the grammatical gender of the noun you are looking for. The database will take a long time to be
         complete, so, if you find a noun with a gender "tbd (to be defined)", please, let me know.
         
        ** ALL NOUNS in PLURAL are FEMININE in the German language! So, this only works for nouns in *singular*. **
    """,
    version="1.0.0",
    contact={
        "name": "Andrew Monteiro da Silva",
        "url": "https://github.com/Andrew-2609",
        "email": "andrew.agoravai@gmail.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://github.com/Andrew-2609/german-gender-api/blob/main/LICENSE"
    }
)

app.mount("/static", StaticFiles(directory="static"), name="static")

model.Base.metadata.create_all(engine)

app.include_router(router=noun.router)
app.include_router(router=home.router)
