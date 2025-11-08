import gradio as gr
from image_encoder import search_similar_images  # or just import the function if in same file
import os

def find_similar(uploaded_image):
    image_path = uploaded_image

    # Get the 3 most similar image paths
    similar_results = search_similar_images(image_path)

    # If tuples like (path, score), extract only path
    similar_paths = []
    for item in similar_results:
        if isinstance(item, (list, tuple)):
            similar_paths.append(item[0])
        else:
            similar_paths.append(item)

    # Ensure they exist
    similar_paths = [os.path.abspath(p) for p in similar_paths if os.path.exists(p)]

    return similar_paths


# Create the interface
demo = gr.Interface(
    fn=find_similar,
    inputs=gr.Image(type="filepath", label="Upload an Image"),
    outputs=[
        gr.Image(label="Most Similar Image 1"),
        gr.Image(label="Most Similar Image 2"),
        gr.Image(label="Most Similar Image 3")
    ],
    title="FaunAI — Image Similarity Search",
    description="Upload an image to find visually similar ones from the dataset.",
)

if __name__ == "__main__":
    demo.launch()
