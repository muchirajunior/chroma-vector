import chromadb 

client = chromadb.PersistentClient(path='../chroma_db')

collection =  client.get_or_create_collection('vehicles')

#add data
collection.add(
    documents=[
        'planes fly in the sky',
        'cars drives on land',
        'boats travels on water',
        'buses use road transport'
    ],
    ids=['plane','car','boat','bus'],
    metadatas=[
        {'type':'air_transport', 'fuel':'jet fuel'},
        {'type':'private_transport', 'fuel':'petrol'},
        {'type':'water_transport', 'fuel':'petrol'},
        {'type':'public_transport', 'fuel':'diesel'},
    ]

)

print('Database collection created successfully')