




import paralleldots
paralleldots.set_api_key('lpdFlYw2ZthAIklOkNNaddQd8hCHJRDzfAI3hJHtKe0')
def ner(text):
    ner = paralleldots.ner(text)
    return ner