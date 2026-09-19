import chromadb 

client = chromadb.PersistentClient(path='../chroma_db')

collection =  client.get_collection('vehicles')

collection.delete(ids=['car'])

print(collection.get())