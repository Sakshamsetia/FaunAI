# FaunAI

FaunAI is a visual intelligence system that lets you upload an animal image and instantly discover visually similar species from a curated wildlife dataset.

## Tech Stack
- **Python**: Core programming language.
- **SentenceTransformers**: For generating image embeddings using the `clip-ViT-B-32` model.
- **FAISS**: For efficient similarity search and clustering of image embeddings.
- **Pillow (PIL)**: For image processing.
- **NumPy**: For numerical operations.

## Features
- Generate embeddings for a dataset of animal images.
- Create a FAISS index for fast similarity searches.
- Search for visually similar images given an input image.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd FaunAI
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Database**:
   Use the `download_db.py` script to download the required database:
   ```bash
   python download_db.py
   ```

4. **Prepare the Dataset**:
   Place your dataset of animal images in the `all_animals/` directory. Ensure the images are in `.jpg` format.

5. **Replace Input and Output Directories**:
   Update the input and output directories in the scripts as needed.

6. **Organize Files**:
   Run the `filemanage.py` script to organize the files:
   ```bash
   python filemanage.py
   ```

7. **Generate Embeddings and Create FAISS Index**:
   Run the following command to generate embeddings and create the FAISS index:
   ```bash
   python image_encoder.py
   ```

8. **Run the Application**:
   Use this command to open the Gradio interface for running the app:
   ```bash
   python app.py
   ```

## Usage
1. **Search for Similar Images**:
   Use the `search_similar_images` function in `image_encoder.py` to find similar images. Example:
   ```python
   from image_encoder import search_similar_images

   results = search_similar_images('path_to_query_image.jpg')
   for path, score in results:
       print(f"Image: {path}, Similarity Score: {score}")
   ```

2. **Output**:
   The system will return the top-k most similar images along with their similarity scores.

## Explanation
FaunAI leverages the `clip-ViT-B-32` model from SentenceTransformers to generate embeddings for images. These embeddings are stored in a FAISS index, which allows for efficient similarity searches. The system normalizes the embeddings to ensure accurate similarity calculations. When a query image is provided, its embedding is compared against the FAISS index to retrieve the most similar images.

## Future Enhancements
- Add support for additional image formats.
- Improve the user interface for non-technical users.
- Expand the dataset to include more species.
