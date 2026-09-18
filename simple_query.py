import chromadb

client =  chromadb.Client()

#create a collection
collection = client.create_collection(name='vehicles')

print('Created collection:: ', collection.name)

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

#query 
results =  collection.query(query_texts=['what can carry more than 20 people'], n_results=2)

print(results)