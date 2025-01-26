#!/bin/bash

#!/bin/bash

# Set your API key and endpoint
API_KEY="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"
ENDPOINT="https://api.openai.com/v1/chat/completions"

# Define the model and prompt
MODEL="gpt-4o-mini"
PROMPT="Provide java code for this cobol program in a single line: IDENTIFICATION DIVISION. PROGRAM-ID. AddNumbersFunction. ENVIRONMENT DIVISION. INPUT-OUTPUT SECTION. DATA DIVISION. WORKING-STORAGE SECTION. 01 NUM1 PIC 9(5) VALUE 12345. 01 NUM2 PIC 9(5) VALUE 54321. 01 RESULT PIC 9(5) VALUE 0. LINKAGE SECTION. 01 PARAM1 PIC 9(5). 01 PARAM2 PIC 9(5). 01 FUNCTION-RESULT PIC 9(5). PROCEDURE DIVISION. MAIN-PARA. CALL 'ADD-FUNCTION' USING NUM1 NUM2 RESULT. DISPLAY RESULT. STOP RUN. ADD-FUNCTION SECTION. ADD-PARA. ADD PARAM1 TO PARAM2 GIVING FUNCTION-RESULT. EXIT SECTION. " 
#PROMPT="Provide java code for this cobol program in a single line: $(cat ../src/cobol/addnumbers.cbl | tr -d '\n' | sed 's/"/\\"/g' | sed 's/^/"/;s/$/"/')"       
echo $PROMPT
# Prepare the JSON payload
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

# Print the response
echo "Raw response $RESPONSE"

#FORMAT_RESPONSE=$(echo "$RESPONSE" | sed '1d;$d' | sed '1d;$d' | sed '1d;$d' | sed '/^```/d' |sed '/###/,$d' | sed -e 's/{/ {\n    /g' -e 's/;[ ]*/;\n    /g' -e 's/}/\n}/g' -e 's/    }/}/g')
echo "$RESPONSE"  | jq -r '.choices[0].message.content' | sed -n '/```/,/```/p' | sed 's/```[a-z]*//g' | sed -e 's/{/ {\n    /g' -e 's/;[ ]*/;\n    /g' -e 's/}/\n}/g' -e 's/    }/}/g' | sed '/^$/d' >  ../src/java/AddNumbersFunction.java
