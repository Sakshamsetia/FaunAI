from sentence_transformers import SentenceTransformer
import os
from glob import glob
from PIL import Image
import numpy as np
import faiss

model = SentenceTransformer('clip-ViT-B-32')

def generate_embeddings(directory):
    img_path = glob(os.path.join(directory,'*.jpg'),recursive=True)
    embeddings = []
    i = 0
    print("Embedding started")
    for img in img_path:
        embedding = model.encode(Image.open(img))
        embeddings.append(embedding)
        i += 1
        print(f"{i} embedding done")
    print("All embeddings Done!")
    return embeddings,img_path

def create_faiss_index(embeddings, image_paths, output_path):

    dimension = len(embeddings[0])
    index = faiss.IndexFlatIP(dimension)
    index = faiss.IndexIDMap(index)

    vectors = np.array(embeddings).astype(np.float32)
    vectors /= np.linalg.norm(vectors, axis=1, keepdims=True)


    index.add_with_ids(vectors, np.array(range(len(embeddings))))

    faiss.write_index(index, output_path)
    print(f"Index created and saved to {output_path}")

    with open(output_path + '.paths', 'w') as f:
        for img_path in image_paths:
            f.write(img_path + '\n')
    print("Completed Vector DB creation")

def search_similar_images(img_path, index_path='./faiss_db', paths_path='./faiss_db.paths', top_k=3):
    embedding = model.encode(Image.open(img_path))
    index = faiss.read_index(index_path)
    print(f"Loaded FAISS index from {index_path}")

    with open(paths_path, 'r') as f:
        image_paths = [line.strip() for line in f.readlines()]
    print(f"Loaded {len(image_paths)} image paths")

    query = np.atleast_2d(np.array(embedding, dtype=np.float32))  # ensures shape (1, 512)
    query /= np.linalg.norm(query, axis=1, keepdims=True)


    distances, indices = index.search(query, top_k)

    results = []
    for i, idx in enumerate(indices[0]):
        if idx == -1:  
            continue
        results.append((image_paths[idx], float(distances[0][i])))

    return results

if __name__ == '__main__':
    paths = "./all_animals"
    embeddings,img_paths = generate_embeddings(paths)
    create_faiss_index(embeddings,img_paths,"./faiss_db")