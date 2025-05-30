#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 29 14:52:50 2025

@author: madiraasch
"""

import json
import time
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


INPUT_FILE = "toxic_empathy_prompt_dataset.json"
OUTPUT_FILE = "model_responses.json"
MODEL_NAME = "gpt-3.5-turbo"  

client = OpenAI()  # uses OPENAI_API_KEY from environment

def query_openai(prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error querying OpenAI: {e}")
        return None

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        prompts = json.load(f)

    results = []
    for item in prompts:
        print(f"Processing prompt ID {item['id']} scenario '{item['scenario']}' version '{item['version']}'")
        response = query_openai(item['prompt'])
        if response is None:
            response = "Error: No response"
        results.append({
            "id": item['id'],
            "scenario": item['scenario'],
            "version": item['version'],
            "prompt": item['prompt'],
            "model_response": response,
        })
        time.sleep(1)  # To respect rate limits; adjust as needed

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f_out:
        json.dump(results, f_out, indent=2, ensure_ascii=False)

    print(f"Responses saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()





