from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

app = FastAPI()

model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                                            load_in_4bit=False, # this is only for bitandbytes
                                            torch_dtype="auto",)

tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                                          torch_dtype="auto")

pipe = pipeline("text-generation",
                model=model,
                tokenizer=tokenizer,
                torch_dtype=torch.bfloat16,
                device_map="auto")

def generate_response(text): 
    messages = [
        {
            "role": "system",
            "content": "You are a friendly chatbot who always responds in the style of a pirate",
        },
        {"role": "user", "content": text},
    ]


    prompt = pipe.tokenizer.apply_chat_template(messages,
                                                tokenize=False,
                                                add_generation_prompt=True)

    outputs = pipe(prompt,
                max_new_tokens=256,
                do_sample=True,
                temperature=0.7,
                top_k=50,
                top_p=0.95)
    
    output = outputs[0]["generated_text"]

    response = output.split("<|assistant|>",1)[1]

    return {"response": response}

@app.post("/request")
def query_request(request: str):
    return generate_response(request)
