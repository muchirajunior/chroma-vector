import chromadb

client = chromadb.PersistentClient('./chroma_db')

collections = client.list_collections()

if __name__=='__main__':
    print('All collections:')
    for c in collections:
        print('-', c.name)