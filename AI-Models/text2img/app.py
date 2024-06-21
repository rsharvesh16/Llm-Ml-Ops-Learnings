import boto3
import json
import streamlit as st
from PIL import Image
from io import BytesIO
import base64

# Initialize the AWS client
bedrock_runtime = boto3.client(service_name="bedrock-runtime")

def get_amazon_llm(text_input):
    body = json.dumps(
        {
            "taskType": "TEXT_IMAGE",
            "textToImageParams": {
                "text": text_input, 
            },
            "imageGenerationConfig": {
                "numberOfImages": 1,   # Range: 1 to 5 
                "quality": "premium",  # Options: standard or premium
                "height": 768,         # Supported height list in the docs 
                "width": 1280,         # Supported width list in the docs
                "cfgScale": 7.5,       # Range: 1.0 (exclusive) to 10.0
                "seed": 42             # Range: 0 to 214783647
            }
        }
    )
    
    try:
        response = bedrock_runtime.invoke_model(
            body=body, 
            modelId="amazon.titan-image-generator-v1",
            accept="application/json", 
            contentType="application/json"
        )
        
        # Read the StreamingBody and decode it to a string
        response_body = response['body'].read().decode('utf-8')
        
        return response_body
    except bedrock_runtime.exceptions.ValidationException as e:
        st.error("The prompt was flagged by content filters. Please adjust your prompt and try again.")
        return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    st.set_page_config(page_title="Image Generator")

    st.header("Image Generator AWS Bedrock💁")

    text_input = st.text_input("Ask a prompt to generate an image")
    
    if st.button("Generate Image"):
        if text_input:
            response = get_amazon_llm(text_input)
            if response:
                try:
                    response_json = json.loads(response)
                    st.json(response_json)  # Print the JSON response for debugging
                    
                    # Check if the response contains a list of images
                    images_data = response_json.get('images')
                    if images_data and isinstance(images_data, list):
                        for image_data in images_data:
                            image = Image.open(BytesIO(base64.b64decode(image_data)))
                            st.image(image, caption="Generated Image")
                    else:
                        st.error("No image data found in the response.")
                except json.JSONDecodeError:
                    st.error("Failed to decode JSON response.")
                # except KeyError as e:
                #     st.error(f"Key error: {e}")
                # except Exception as e:
                #     st.error(f"An error occurred while processing the response: {e}")
            else:
                st.error("Failed to generate image. Please try again with a different prompt.")

if __name__ == "__main__":
    main()
