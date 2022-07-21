from fastapi import FastAPI
import uvicorn

from textblob import TextBlob
app=FastAPI()
#Routes
@app.get('/')
async def index():
    return {'text':'Hey, FastAPI'}

@app.get('/sentiment/{text}')
async def get_sentiment(text):
    blob = TextBlob(text).sentiment
    results = {'original_text':text,'polarity':blob.polarity,'subjectivity':blob.subjectivity}
    return results


if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=3000)