
# Set your API key and endpoint
API_KEY="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"
ENDPOINT="https://api.openai.com/v1/chat/completions"

# Define the model and prompt
MODEL="gpt-4o-mini"
#PROMPT="Generate test case for this java code"
PROMPT="Generate test case code in java in single line: $(cat src/java/AddNumbersFunction.java | tr -d '\n')" 
       
echo "prompt is $PROMPT"
 #Prepare the JSON payload
REQUEST_BODY=$(cat <<EOF
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
  -d "$REQUEST_BODY" )


echo "Raw response $RESPONSE"

echo "filtered response"
echo "$RESPONSE"  |  tr -d '\000-\037' | jq -r '.choices[0].message.content'  | echo
#echo "$RESPONSE"  | jq -r '.choices[0].message.content'  | jq '.text | @json'| sed -n '/```/,/```/p' | sed 's/```[a-z]*//g' | sed -e 's/{/ {\n    /g' -e 's/;[ ]*/;\n    /g' -e 's/}/\n}/g' -e 's/    }/}/g' | sed '/^$/d' >  tests/java/AddNumbersFunctionTest.java
#echo "$RESPONSE"  |  tr -d '\000-\037' | jq -r '.choices[0].message.content' | sed 's/```java//g' | sed 's/```//g'  > tests/java/AddNumbersFunctionTest.java
echo "$RESPONSE"  |  tr -d '\000-\037' | jq -r '.choices[0].message.content' | sed -n '/```/,/```/p' | sed 's/```[a-z]*//g' | sed -e 's/{/ {\n    /g' -e 's/;[ ]*/;\n    /g' -e 's/}/\n}/g' -e 's/    }/}/g' | sed '/^$/d' > tests/java/AddNumbersFunctionTest.java
