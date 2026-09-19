import chromadb 

client = chromadb.PersistentClient(path='../chroma_db')

collection =  client.get_collection('vehicles')

#query using id
# print(collection.get(ids=['bus']))

#query using metadata
print(collection.get(where= {'fuel':'petrol'}))
