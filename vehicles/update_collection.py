import chromadb 

client = chromadb.PersistentClient(path='../chroma_db')

collection =  client.get_collection('vehicles')

collection.update(
    ids=['bus'],
    documents=['Bus carries more than 30 people and it travel on road transport']
)

print(collection.get(ids=['bus']))