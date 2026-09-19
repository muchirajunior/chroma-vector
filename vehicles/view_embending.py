import chromadb 

client = chromadb.PersistentClient(path='../chroma_db')

collection =  client.get_collection('vehicles')
data = collection.get(include=['embeddings','documents'])

for id, document, embedding in zip(data['ids'], data['documents'], data['embeddings']):
    print(id,':', document)
    print('Embedings:', embedding[:10],'\n') 