import chromadb 

client = chromadb.PersistentClient(path='./chroma_db')

collection =  client.create_collection('vehicles')

#add data
collection.add(
    documents=[
        'planes fly in the sky',
        'cars drives on land',
        'boats travels on water',
        'buses use road transport'
    ],
    ids=['plane','car','boat','bus'],

)

print('Database collection created successfully')