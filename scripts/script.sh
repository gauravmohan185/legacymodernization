#!/bin/bash

#!/bin/bash

# Set your API key and endpoint
API_KEY="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"
ENDPOINT="https://api.openai.com/v1/chat/completions"

# Define the model and prompt
MODEL="gpt-4o-mini"
PROMPT="How big is sun"

# Prepare the JSON payload
JSON_PAYLOAD=$(cat <<EOF
{
  "model": "$MODEL",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "$PROMPT"}
  ]
}
EOF
)

# Make the API request
RESPONSE=$(curl -s -X POST $ENDPOINT \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d "$JSON_PAYLOAD")

# Print the response
echo "Response from OpenAI:"
echo "$RESPONSE"