import openai

# Set up the OpenAI API client
openai.api_key = "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"

# Set up the model and prompt
model_engine="text-davinci-003"
prompt = str(input("Enter your command: "))


# Generate a response

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1, stop=None,
    temperature=0.5,
)

response = completion.choices[0].text

print (response)