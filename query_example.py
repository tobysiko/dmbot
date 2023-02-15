import openai
openai.api_key = "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"
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="describe a character",
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
)
text = response.choices[0].text
